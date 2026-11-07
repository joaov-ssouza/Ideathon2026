import reflex as rx
from ..estado.app_state import AppState

def painel_detalhe_ponto() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="arrow-left", size=24, color="#0F172A", cursor="pointer", on_click=AppState.preparar_selecao_ponto),
            rx.heading("Raio-X do Local", size="6", color="#0F172A", weight="bold"),
            align_items="center", width="100%", margin_bottom="4"
        ),
        
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="map-pin", size=40, color="#0052CC"),
                    rx.vstack(
                        rx.heading(AppState.ponto_selecionado_nome, size="5", color="#0F172A", weight="bold"),
                        rx.text(f"Cód: {AppState.ponto_selecionado_codigo} • Nota Geral: ⭐ {AppState.ponto_selecionado_avaliacao}", size="2", color="#0F172A"),
                        spacing="1"
                    ),
                    align_items="center", spacing="4", margin_bottom="2"
                ),
                rx.divider(margin_y="2"),
                rx.text("Linhas atendidas:", weight="bold", size="2", color="#0F172A"),
                rx.text(AppState.ponto_selecionado_linhas, size="2", color="#0F172A", margin_bottom="2"),
                
                rx.text("Fluxo de Passageiros:", weight="bold", size="2", color="#0F172A"),
                rx.text(AppState.ponto_selecionado_fluxo, size="2", color="#0F172A", margin_bottom="2"),
                
                rx.text("Características Reportadas:", weight="bold", size="2", color="#0F172A"),
                rx.foreach(AppState.ponto_selecionado_tags_positivas, lambda tag: rx.hstack(rx.icon(tag="check", color="green", size=16), rx.text(tag, color="#0F172A", size="2"))),
                rx.foreach(AppState.ponto_selecionado_tags_negativas, lambda tag: rx.hstack(rx.icon(tag="x", color="red", size=16), rx.text(tag, color="#0F172A", size="2"))),
                
                rx.button(
                    rx.icon(tag="clipboard-pen", size=18), "Contribuir / Avaliar", 
                    on_click=AppState.ir_para_avaliacao, 
                    bg="#0052CC", color="white", width="100%", size="3", margin_top="4"
                ),
                width="100%", align_items="start"
            ),
            width="100%", padding="1.5em", bg="white", border="1px solid #E2E8F0"
        ),
        width="100%"
    )

def checkbox_preto(texto: str) -> rx.Component:
    return rx.hstack(
        rx.checkbox(color_scheme="blue"),
        rx.text(texto, color="#0F172A", size="2", weight="medium"),
        align_items="center", spacing="2"
    )

def painel_avaliacao_ponto() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="arrow-left", size=24, color="#0F172A", cursor="pointer", on_click=lambda: AppState.navegar("parada_detalhe")),
            rx.heading("Nova Avaliação", size="6", color="#0F172A", weight="bold"),
            align_items="center", width="100%", margin_bottom="4"
        ),
        rx.text(f"Avaliando: {AppState.ponto_selecionado_nome}", size="2", color="#0F172A", weight="bold", margin_bottom="4"),
        
        rx.card(
            rx.vstack(
                checkbox_preto("O local é bem iluminado à noite"),
                checkbox_preto("Possui cobertura em bom estado"),
                checkbox_preto("Tem assentos disponíveis"),
                checkbox_preto("Possui guia rebaixada (Acessibilidade)"),
                checkbox_preto("Me sinto seguro(a) neste local"),
                
                rx.text("Observações adicionais:", weight="bold", size="2", color="#0F172A", margin_top="3"),
                rx.text_area(placeholder="Ex: Poste está com a luz queimada...", bg="white", color="#0F172A", border="1px solid #CBD5E1", width="100%"),
                
                rx.button(
                    rx.icon(tag="save", size=18), "Salvar Relato", 
                    on_click=AppState.salvar_avaliacao, 
                    bg="#0052CC", color="white", width="100%", size="3", margin_top="4"
                ),
                spacing="3", width="100%", align_items="start"
            ),
            width="100%", padding="1.5em", bg="white", border="1px solid #E2E8F0"
        ),
        width="100%"
    )