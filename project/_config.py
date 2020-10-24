from pathlib import Path

BASEDIR = Path(__file__).resolve().parent
basedir = str(Path(__file__).resolve().parent)

DATABASE = BASEDIR / "data.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{str(DATABASE)}"
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = "bf*WR9*9R&9snwwL?3HmaE*e"

DEBUG = False