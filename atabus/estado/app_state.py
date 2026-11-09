import reflex as rx
from typing import List, Dict, Any
from ..dados.seed import PONTOS_INICIAIS
from ..services.osm_service import buscar_pontos_reais_aracatuba

class AppState(rx.State):
    view_atual: str = "home"
    erro_busca: str = ""
    pontos_disponiveis: List[str] = []
    todos_os_pontos_mapa: List[Dict[str, Any]] = []
    
    origem_selecionada: str = ""
    destino_selecionado: str = ""
    rotas_encontradas: List[Dict] = []
    trajeto_ativo: List[List[float]] = []
    
    ponto_selecionado_nome: str = ""
    ponto_selecionado_codigo: str = ""
    ponto_selecionado_avaliacao: str = ""
    ponto_selecionado_fluxo: str = ""
    ponto_selecionado_linhas: str = ""
    ponto_selecionado_tipo: str = "Parada Comum"
    ponto_selecionado_tags_positivas: List[str] = []
    ponto_selecionado_tags_negativas: List[str] = []

    avisos: List[Dict[str, str]] = [
        {"id": "1", "tipo": "Interrupção", "titulo": "Linha 102 Suspensa", "desc": "Devido a obras da prefeitura na via.", "regiao": "Centro", "cor": "red"},
        {"id": "2", "tipo": "Desvio", "titulo": "Mudança de Trajeto (L 205)", "desc": "Desvio provisório pela Rua Cristiano Olsen.", "regiao": "Zona Leste", "cor": "orange"},
        {"id": "3", "tipo": "Informativo", "titulo": "Nova Frota com Wi-Fi", "desc": "A linha 104 recebeu ônibus com acessibilidade e internet.", "regiao": "Geral", "cor": "blue"}
    ]

    def dispensar_aviso(self, id_aviso: str):
        self.avisos = [a for a in self.avisos if a["id"] != id_aviso]

    def carregar_dados_iniciais(self):
        if len(self.todos_os_pontos_mapa) > 0:
            return

        self.pontos_disponiveis = [p["nome"] for p in PONTOS_INICIAIS]
        
        lista_banco = [{"nome": p["nome"], "lat": p["lat"], "lon": p["lon"], "tipo": p["tipo"]} for p in PONTOS_INICIAIS]
        
        pontos_osm_raw = buscar_pontos_reais_aracatuba()
        lista_osm = [{"nome": p["nome"], "lat": p["lat"], "lon": p["lon"], "tipo": "Parada Comum"} for p in pontos_osm_raw]
        
        self.todos_os_pontos_mapa = lista_banco + lista_osm

    def set_origem(self, valor: str):
        self.origem_selecionada = valor
        self.erro_busca = ""

    def set_destino(self, valor: str):
        self.destino_selecionado = valor
        self.erro_busca = ""

    def simular_busca(self):
        if not self.origem_selecionada or not self.destino_selecionado:
            self.erro_busca = "Selecione origem e destino."
            return
        if self.origem_selecionada == self.destino_selecionado:
            self.erro_busca = "A origem e o destino não podem ser iguais."
            return
            
        self.erro_busca = ""
        self.rotas_encontradas = [
            {"id": 1, "tipo": "Equilibrada", "linhas": "Linha 104", "tempo_total": "18 min", "caminhada": "300m (4 min)", "onibus": "4.2 km", "baldeacao": False, "recomendada": True},
            {"id": 2, "tipo": "Menos Caminhada", "linhas": "Linha 102 ➔ Linha 205", "tempo_total": "26 min", "caminhada": "150m (2 min)", "onibus": "5.1 km", "baldeacao": True, "recomendada": False},
            {"id": 3, "tipo": "Mais Rápida", "linhas": "Linha 110", "tempo_total": "15 min", "caminhada": "850m (11 min)", "onibus": "3.0 km", "baldeacao": False, "recomendada": False}
        ]
        
        self.trajeto_ativo = [[-21.2185, -50.4350], [-21.2155, -50.4320], [-21.2120, -50.4290], [-21.2089, -50.4253]]
        self.view_atual = "rotas"

    def preparar_selecao_ponto(self):
        self.view_atual = "selecionar_ponto"

    def abrir_detalhe_ponto(self, p: dict):
        self.ponto_selecionado_nome = p.get("nome", "Ponto")
        self.ponto_selecionado_tipo = p.get("tipo", "Parada Comum")
        self.ponto_selecionado_codigo = f"PT-{str(p.get('lat', '0000'))[-4:]}"
        self.ponto_selecionado_avaliacao = "4.2"
        self.ponto_selecionado_fluxo = "Alto (Aprox. 450 pass/dia)"
        self.ponto_selecionado_linhas = "102, 104, 205"
        self.ponto_selecionado_tags_positivas = ["Boa Iluminação", "Assentos Inteiros"]
        self.ponto_selecionado_tags_negativas = ["Sem acessibilidade PCD"]
        self.view_atual = "parada_detalhe"
        
    def ir_para_avaliacao(self):
        self.view_atual = "parada_avaliar"

    def salvar_avaliacao(self):
        self.voltar_home()

    def voltar_home(self):
        self.view_atual = "home"
        self.erro_busca = ""
        self.trajeto_ativo = []
        
    def navegar(self, nova_view: str):
        self.view_atual = nova_view
        self.erro_busca = ""