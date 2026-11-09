import reflex as rx

config = rx.Config(
    app_name="atabus",
    backend_host="0.0.0.0",
    disable_plugins=[rx.plugins.SitemapPlugin],
)