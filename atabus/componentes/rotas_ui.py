import reflex as rx
from ..estado.app_state import AppState

def painel_rotas() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="arrow-left", size=24, color="#0F172A", cursor="pointer", on_click=AppState.voltar_home),
            rx.heading("Opções de Rota", size="6", color="#0F172A", weight="bold"),
            align_items="center", width="100%", margin_bottom="4"
        ),
        
        rx.text(f"{AppState.origem_selecionada} ➔ {AppState.destino_selecionado}", size="2", color="#0F172A", weight="bold", margin_bottom="4"),
        
        rx.vstack(
            rx.foreach(AppState.rotas_encontradas, render_rota),
            spacing="4", width="100%"
        ),
        width="100%"
    )

def render_rota(rota: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rota["tipo"], 
                    color_scheme=rx.cond(rota["recomendada"], "green", "gray"), 
                    color="#0F172A", 
                    variant="soft"
                ),
                rx.spacer(),
                rx.text(rota["tempo_total"], weight="bold", size="4", color="#0F172A"),
                width="100%", align_items="center"
            ),
            rx.heading(rota["linhas"], size="4", color="#0F172A", margin_top="2"),
            rx.divider(margin_y="2"),
            rx.grid(
                rx.hstack(rx.icon(tag="footprints", size=16, color="#0F172A"), rx.text(f"A Pé: {rota['caminhada']}", size="1", color="#0F172A")),
                rx.hstack(rx.icon(tag="bus", size=16, color="#0F172A"), rx.text(f"Ônibus: {rota['onibus']}", size="1", color="#0F172A")),
                rx.hstack(rx.icon(tag="git-merge", size=16, color="#0F172A"), rx.text(rx.cond(rota["baldeacao"], "Com Baldeação", "Direto"), size="1", color="#0F172A")),
                columns="2", spacing="2", width="100%"
            ),
            width="100%"
        ),
        width="100%", 
        padding="1.2em", 
        border=rx.cond(rota["recomendada"], "2px solid #0052CC", "1px solid #E2E8F0"), 
        bg="white"
    )