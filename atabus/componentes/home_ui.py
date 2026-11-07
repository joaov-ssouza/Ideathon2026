import reflex as rx
from ..estado.app_state import AppState

ESTILO_DROPDOWN = {
    "& .rt-SelectTrigger": {
        "background_color": "#FFFFFF !important",
        "color": "#0F172A !important",
        "border": "1px solid #CBD5E1 !important",
    },
    "& .rt-SelectTrigger:focus": {
        "border_color": "#0052CC !important",
        "box_shadow": "0 0 0 1px #0052CC !important"
    }
}

def painel_home() -> rx.Component:
    return rx.theme(
        rx.vstack(
            rx.heading("Para onde vamos?", size="7", color="#0F172A", weight="bold", margin_bottom="2"),
            rx.card(
                rx.vstack(
                    rx.cond(AppState.erro_busca != "", rx.callout(AppState.erro_busca, icon="alert-triangle", color_scheme="red", width="100%")),
                    rx.select(
                        AppState.pontos_disponiveis, 
                        placeholder="Ponto de Partida", 
                        value=AppState.origem_selecionada,
                        on_change=AppState.set_origem, 
                        size="3", width="100%", style=ESTILO_DROPDOWN
                    ),
                    rx.select(
                        AppState.pontos_disponiveis, 
                        placeholder="Destino", 
                        value=AppState.destino_selecionado,
                        on_change=AppState.set_destino, 
                        size="3", width="100%", style=ESTILO_DROPDOWN
                    ),
                    rx.button("Simular Viagem", on_click=AppState.simular_busca, bg="#0052CC", color="white", size="3", width="100%"),
                    spacing="3", width="100%"
                ),
                padding="1.5em", width="100%", bg="white", box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1)", border="none"
            ),
            
            rx.heading("Explorar", size="3", color="#475569", margin_top="4", margin_bottom="2"),
            rx.grid(
                card_atalho("Avisos Oficiais", "triangle-alert", lambda: AppState.navegar("avisos")),
                card_atalho("Avaliar Pontos", "map-pinned", AppState.preparar_selecao_ponto),
                columns="2", spacing="3", width="100%"
            ),
            width="100%"
        ),
        appearance="light", has_background=False
    )

def card_atalho(titulo: str, icone: str, acao) -> rx.Component:
    return rx.card(
        rx.vstack(rx.icon(tag=icone, size=24, color="#0052CC"), rx.text(titulo, size="2", weight="bold", color="#0F172A"), align_items="center", spacing="2"),
        cursor="pointer", padding="1em", bg="white", _hover={"transform": "translateY(-2px)", "box_shadow": "md"}, transition="all 0.2s ease", on_click=acao, border="1px solid #E2E8F0"
    )