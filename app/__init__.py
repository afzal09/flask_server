from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape
import dotenv


app = Flask(__name__)
env = Environment(
    loader=PackageLoader(__name__),
    autoescape=select_autoescape()
)
dotenv.load_dotenv()

from app import routes