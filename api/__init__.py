from flask import Flask, jsonify, request
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address

# Import modules that we create
from api import developers, langs


app = Flask(__name__)
# Initialize limiter
limiter = Limiter( app, key_func=get_remote_address)
# Rate limit headers
limiter.header_mapping = {
    HEADERS.LIMIT : "X-My-Limit",
    HEADERS.RESET : "X-My-Reset",
    HEADERS.REMAINING: "X-My-Remaining"
}

# this for keeping the order of json data
app.config['JSON_SORT_KEYS'] = False

from api import main