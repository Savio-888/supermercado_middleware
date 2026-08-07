import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "Ady+piLg/ENMxTcrOT9zln7LnBphBe9kfR+N5upaZ5E=")
    DATABASE = os.environ.get("DATABASE", str(BASE_DIR / "instance" / "supermercado.db"))
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"