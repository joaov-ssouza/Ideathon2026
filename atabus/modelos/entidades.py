import reflex as rx
from typing import Optional

class Ponto(rx.Model, table=True):
    nome: str
    lat: float
    lon: float
    tipo: str
    acessivel: bool = False
    cobertura: bool = False
    iluminacao: bool = False

class Linha(rx.Model, table=True):
    codigo: str
    nome: str
    origem: str
    destino: str

class Ocorrencia(rx.Model, table=True):
    categoria: str
    descricao: str
    linha_afetada: Optional[str] = None
    severidade: str
    valido_ate: Optional[str] = None