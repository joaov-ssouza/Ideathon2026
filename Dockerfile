ARG PORT=10000
ARG API_URL

FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /bin/uv
COPY --from=oven/bun:1.4.4 /usr/local/bin/bun /usr/local/bin/bun

ENV UV_COMPILE_BYTECODE=1 \
    UV_NO_CACHE=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN uv venv && uv pip install -r requirements.txt

COPY . .

ARG PORT API_URL

RUN REFLEX_API_URL="${API_URL:-http://localhost:${PORT}}" \
    reflex export --frontend-only --no-zip --no-ssr

FROM python:3.13-slim

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

RUN adduser --disabled-password --gecos "" --home /app reflex \
    && chown reflex:reflex /app

COPY --chown=reflex:reflex --from=builder /app/.venv .venv
COPY --chown=reflex:reflex --from=builder /app/.web/backend .web/backend
COPY --from=builder /app/.web/build/client /srv
COPY --chown=reflex:reflex . .

USER reflex

EXPOSE ${PORT}

CMD ["sh", "-c", "caddy start --config /app/Caddyfile && redis-server --daemonize yes --save '' --appendonly no && exec reflex run --env prod --backend-only --backend-port 8000"]
