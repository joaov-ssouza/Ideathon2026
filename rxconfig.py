import os
import reflex as rx

config = rx.Config(
    app_name="atabus",
    db_url="sqlite:///reflex.db",
    api_url=os.environ.get("API_URL", "http://localhost:8000"),
)