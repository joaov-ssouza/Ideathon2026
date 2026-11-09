import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="atabus",
    backend_host="0.0.0.0",
    frontend_packages=["leaflet"],
    disable_plugins=[SitemapPlugin],
)