# Build e execute o AtaBus em um único container.
# Compatível com serviços Docker que encaminham HTTP para a variável PORT
# (Render usa 10000 por padrão).

ARG PORT=10000
ARG API_URL

# ---------- Etapa de build ----------
FROM python:3.13-slim AS builder

# uv instala as dependências Python; Bun é copiado para evitar que o Reflex
# tente baixá-lo durante o build.
COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /bin/uv
COPY --from=oven/bun:1.4.4 /usr/local/bin/bun /usr/local/bin/bun

ENV UV_COMPILE_BYTECODE=1 \
    UV_NO_CACHE=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Instala dependências antes de copiar o código para aproveitar o cache.
COPY requirements.txt ./requirements.txt
RUN uv venv && uv pip install -r requirements.txt

# O .dockerignore evita copiar ambientes locais e builds antigos.
COPY . .

ARG PORT API_URL

# Gera o frontend estático. Quando API_URL não é informado, usa localhost;
# o Reflex substitui esse host pelo domínio que serve a aplicação.
RUN REFLEX_API_URL="${API_URL:-http://localhost:${PORT}}" \
    reflex export --frontend-only --no-zip

# ---------- Imagem final ----------
FROM python:3.13-slim

# Redis é usado internamente pelo Reflex para gerenciar estado/sessões;
# não é o banco de dados de negócio da aplicação.
RUN apt-get update \
    && apt-get install -y --no-install-recommends redis-server \
    && rm -rf /var/lib/apt/lists/*

COPY --from=caddy:2 /usr/bin/caddy /usr/bin/caddy

ARG PORT=10000
ENV PORT=${PORT} \
    HOME=/app \
    PATH="/app/.venv/bin:$PATH" \
    REFLEX_REDIS_URL=redis://127.0.0.1:6379 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# O Reflex precisa escrever o diretório de estado dentro de /app.
RUN adduser --disabled-password --gecos "" --home /app reflex \
    && chown reflex:reflex /app

COPY --chown=reflex:reflex --from=builder /app/.venv .venv
COPY --chown=reflex:reflex --from=builder /app/.web/backend .web/backend
COPY --from=builder /app/.web/build/client /srv
COPY --chown=reflex:reflex . .

USER reflex

EXPOSE ${PORT}

# Caddy publica o frontend na PORT e encaminha endpoints do Reflex
# (incluindo WebSocket) para o backend na porta 8000.
CMD ["sh", "-c", "caddy start --config /app/Caddyfile && redis-server --daemonize yes --save '' --appendonly no && exec reflex run --env prod --backend-only --backend-port 8000"]
