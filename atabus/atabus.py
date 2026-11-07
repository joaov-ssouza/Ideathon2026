import reflex as rx
from .estado.app_state import AppState
from .componentes.mapa import mapa_simples
from .componentes.home_ui import painel_home
from .componentes.avisos_ui import painel_avisos
from .componentes.rotas_ui import painel_rotas
from .componentes.paradas_ui import painel_detalhe_ponto, painel_avaliacao_ponto

ESTILO_PAINEL_LATERAL = {
    "position": "absolute", "top": ["80px", "7%", "7%"], "left": ["10px", "8%", "10%"], 
    "width": ["calc(100% - 20px)", "450px", "450px"], 
    "height": "85vh", 
    "bg": "rgba(255, 255, 255, 0.95)", "backdrop_filter": "blur(16px)",
    "border_radius": "2xl", "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    "padding": "2em", "overflow_y": "auto", "z_index": "10", "transition": "all 0.3s ease-in-out"
}

ESTILO_PAINEL_REDUZIDO = {
    "position": "absolute", "top": "20px", "left": "50%", "transform": "translateX(-50%)", 
    "width": "auto", "bg": "#0052CC", "color": "white", "backdrop_filter": "blur(10px)",
    "border_radius": "2xl", "padding": "1em 2em", "z_index": "10", "transition": "all 0.3s ease-in-out",
    "box_shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.3)"
}

def index() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.image(src="/logo.png", height="40px", alt="Logo AtaBus", cursor="pointer", on_click=AppState.voltar_home),
            ),
            position="absolute", top="20px", left="20px", z_index="20",
            bg="rgba(255, 255, 255, 0.95)", padding="0.5em 1.5em", border_radius="full", box_shadow="sm"
        ),

        rx.match(
            AppState.view_atual,
            ("selecionar_ponto", rx.box(
                rx.hstack(
                    rx.icon(tag="map-pin", color="white"),
                    rx.text("Selecione um local no mapa para interagir", color="white", weight="bold"),
                    rx.icon(tag="x", color="white", cursor="pointer", on_click=AppState.voltar_home, margin_left="3")
                ),
                style=ESTILO_PAINEL_REDUZIDO
            )),
            
            rx.box(
                rx.match(
                    AppState.view_atual,
                    ("home", painel_home()),
                    ("avisos", painel_avisos()),
                    ("rotas", painel_rotas()),
                    ("parada_detalhe", painel_detalhe_ponto()),
                    ("parada_avaliar", painel_avaliacao_ponto()),
                    painel_home() 
                ),
                style=ESTILO_PAINEL_LATERAL
            )
        ),

        rx.box(
            mapa_simples(
                centro=[-21.2089, -50.4253], zoom=14, 
                pontos=AppState.todos_os_pontos_mapa, trajeto=AppState.trajeto_ativo
            ),
            position="absolute", top="0", left="0", right="0", bottom="0", width="100vw", height="100vh", z_index="0"
        ),
        position="relative", width="100vw", height="100vh", overflow="hidden", font_family="system-ui, -apple-system, sans-serif"
    )

app = rx.App(stylesheets=["https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"])


app.add_page(
    index, 
    route="/", 
    title="AtaBus", 
    image="/logo.png",
    on_load=AppState.carregar_dados_iniciais
)