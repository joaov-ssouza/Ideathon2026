import reflex as rx
from ..estado.app_state import AppState

class MapContainer(rx.Component):
    library = "react-leaflet"
    tag = "MapContainer"
    center: rx.Var[list[float]]
    zoom: rx.Var[int]
    zoomControl: rx.Var[bool]

class TileLayer(rx.Component):
    library = "react-leaflet"
    tag = "TileLayer"
    url: rx.Var[str]
    attribution: rx.Var[str]

class Marker(rx.Component):
    library = "react-leaflet"
    tag = "Marker"
    position: rx.Var[list[float]]

class Popup(rx.Component):
    library = "react-leaflet"
    tag = "Popup"

class Polyline(rx.Component):
    library = "react-leaflet"
    tag = "Polyline"
    positions: rx.Var[list[list[float]]]
    pathOptions: rx.Var[dict]

def render_marcador(p: rx.Var[dict]) -> rx.Component:
    return Marker.create(
        Popup.create(
            rx.vstack(
                rx.text(p["nome"], weight="bold", color="#0F172A", margin_bottom="1", text_align="center"),
                rx.button(
                    rx.icon(tag="info", size=16),
                    "Ver Detalhes", 
                    size="1", margin_top="2", width="100%", bg="#0052CC", color="white",
                    on_click=lambda: AppState.abrir_detalhe_ponto(p)
                ),
                align_items="center",
                padding="1",
            )
        ),
        position=[p["lat"], p["lon"]]
    )

def mapa_simples(centro: list[float], zoom: int = 14, pontos: rx.Var[list[dict]] = None, trajeto: rx.Var[list[list[float]]] = None) -> rx.Component:
    return MapContainer.create(
        TileLayer.create(url="https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png", attribution='&copy; OSM'),
        
        rx.cond(trajeto.length() > 0, Polyline.create(positions=trajeto, pathOptions={"color": "#0052CC", "weight": 5, "opacity": 0.8})),
        
        rx.foreach(pontos, render_marcador),
        
        center=centro, zoom=zoom, zoomControl=False,
        style={"height": "100%", "width": "100%", "zIndex": "1"}
    )