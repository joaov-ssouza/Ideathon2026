import reflex as rx
from .estado.app_state import AppState
from .componentes.mapa import mapa_simples
from .componentes.home_ui import painel_home
from .componentes.avisos_ui import painel_avisos
from .componentes.rotas_ui import painel_rotas
from .componentes.paradas_ui import painel_detalhe_ponto, painel_avaliacao_ponto

ESTILO_CONTAINER_GERAL = {
    "display": ["flex", "flex", "block", "block"],
    "flex_direction": "column",
    "width": "100vw",
    "height": "100vh",
    "overflow_x": "hidden",
    "overflow_y": ["auto", "auto", "hidden", "hidden"],
    "bg": ["#F1F5F9", "#F1F5F9", "transparent", "transparent"],
    "position": "relative",
    "font_family": "system-ui, -apple-system, sans-serif"
}

ESTILO_MAPA = {
    "position": ["relative", "relative", "absolute", "absolute"],
    "top": ["0", "0", "0", "0"],
    "left": ["0", "0", "0", "0"],
    "width": ["100%", "100%", "100vw", "100vw"],
    "height": ["45vh", "45vh", "100vh", "100vh"],
    "padding": ["1em", "1em", "0", "0"],
    "z_index": "0"
}

ESTILO_PAINEL = {
    "position": ["relative", "relative", "absolute", "absolute"],
    "top": ["0", "0", "7%", "7%"],
    "left": ["0", "0", "10%", "10%"],
    "width": ["100%", "100%", "450px", "450px"],
    "height": ["auto", "auto", "85vh", "85vh"],
    "bg": ["transparent", "transparent", "rgba(255, 255, 255, 0.95)", "rgba(255, 255, 255, 0.95)"],
    "backdrop_filter": ["none", "none", "blur(16px)", "blur(16px)"],
    "border_radius": ["0", "0", "2xl", "2xl"],
    "box_shadow": ["none", "none", "0 25px 50px -12px rgba(0, 0, 0, 0.25)", "0 25px 50px -12px rgba(0, 0, 0, 0.25)"],
    "padding": ["1em", "1em", "2em", "2em"],
    "overflow_y": ["visible", "visible", "auto", "auto"],
    "z_index": "10",
    "transition": "all 0.3s ease-in-out"
}

ESTILO_ALERTA_TOPO = {
    "position": "absolute", 
    "top": ["48vh", "48vh", "20px", "20px"],
    "left": "50%", "transform": "translateX(-50%)", 
    "width": ["90%", "90%", "auto", "auto"], 
    "bg": "#0052CC", "color": "white", "backdrop_filter": "blur(10px)",
    "border_radius": "2xl", "padding": "1em 2em", "z_index": "30", "transition": "all 0.3s ease-in-out",
    "box_shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.3)",
    "text_align": "center"
}

ESTILO_DISCLAIMER = {
    "position": "absolute",
    "bottom": "10px",
    "right": ["50%", "50%", "15px", "15px"],
    "transform": ["translateX(50%)", "translateX(50%)", "none", "none"],
    "bg": "rgba(255, 255, 255, 0.85)",
    "backdrop_filter": "blur(4px)",
    "padding": "0.5em 1em",
    "border_radius": "md",
    "box_shadow": "sm",
    "z_index": "20",
    "width": ["90%", "90%", "auto", "auto"],
    "text_align": "center",
    "border": "1px solid #E2E8F0"
}

def index() -> rx.Component:
    return rx.box(
        
        rx.box(
            rx.box(
                mapa_simples(
                    centro=[-21.2089, -50.4253], zoom=14, 
                    pontos=AppState.todos_os_pontos_mapa, trajeto=AppState.trajeto_ativo
                ),
                width="100%", height="100%", 
                border_radius=["xl", "xl", "0", "0"], 
                overflow="hidden", 
                box_shadow=["0 10px 15px -3px rgba(0,0,0,0.1)", "0 10px 15px -3px rgba(0,0,0,0.1)", "none", "none"]
            ),
            style=ESTILO_MAPA
        ),

        rx.match(
            AppState.view_atual,
            ("selecionar_ponto", rx.box(
                rx.hstack(
                    rx.icon(tag="map-pin", color="white"),
                    rx.text("Selecione um local no mapa", color="white", weight="bold"),
                    rx.icon(tag="x", color="white", cursor="pointer", on_click=AppState.voltar_home, margin_left="3")
                ),
                style=ESTILO_ALERTA_TOPO
            )),
        ),

        rx.box(
            rx.center(
                rx.image(
                    src="/logo.png", 
                    height="65px", 
                    border_radius="xl", 
                    alt="Logo AtaBus", 
                    cursor="pointer", 
                    on_click=AppState.voltar_home,
                    margin_bottom="1.5em"
                ),
                width="100%"
            ),
            
            rx.match(
                AppState.view_atual,
                ("home", painel_home()),
                ("avisos", painel_avisos()),
                ("rotas", painel_rotas()),
                ("parada_detalhe", painel_detalhe_ponto()),
                ("parada_avaliar", painel_avaliacao_ponto()),
                painel_home() 
            ),
            style=ESTILO_PAINEL
        ),

        rx.box(
            rx.text(
                "MVP Ideathon • Dados puramente ilustrativos, sem precisão operacional.", 
                size="1", color="#0052CC", weight="bold"
            ),
            style=ESTILO_DISCLAIMER
        ),

        style=ESTILO_CONTAINER_GERAL
    )

app = rx.App(stylesheets=["https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"])
app.add_page(
    index, 
    route="/", 
    title="AtaBus", 
    on_load=AppState.carregar_dados_iniciais
)