import reflex as rx
from ..estado.app_state import AppState

def painel_avisos() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="arrow-left", size=24, color="#0F172A", cursor="pointer", on_click=AppState.voltar_home),
            rx.heading("Avisos Oficiais", size="6", color="#0F172A", weight="bold"),
            align_items="center", width="100%", margin_bottom="4"
        ),
        
        rx.cond(
            AppState.avisos.length() > 0,
            rx.vstack(
                rx.foreach(AppState.avisos, render_aviso),
                spacing="4", width="100%"
            ),
            rx.vstack(
                rx.icon(tag="check-circle", size=40, color="green"),
                rx.text("Tudo certo! Nenhum aviso ativo.", color="#0F172A", weight="bold"),
                align_items="center", width="100%", padding_top="8"
            )
        ),
        width="100%"
    )

def render_aviso(aviso: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(aviso["tipo"], color_scheme=aviso["cor"], variant="soft"),
                rx.spacer(),
                rx.icon(tag="x", size=18, color="#64748B", cursor="pointer", on_click=lambda: AppState.dispensar_aviso(aviso["id"])),
                width="100%", align_items="center"
            ),
            rx.heading(aviso["titulo"], size="4", color="#0F172A", margin_top="2"),
            rx.text(aviso["desc"], size="2", color="#0F172A"),
            rx.hstack(
                rx.icon(tag="map-pin", size=14, color="#64748B"),
                rx.text(aviso["regiao"], size="1", color="#64748B", weight="bold"),
                margin_top="2", align_items="center"
            ),
            width="100%", align_items="start"
        ),
        width="100%", padding="1.5em", bg="white", border="1px solid #E2E8F0"
    )