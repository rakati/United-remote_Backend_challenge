from flask import Flask, jsonify, request
from flask_limiter import Limiter, HEADERS
from flask import send_from_directory

# For rate limit
from flask_limiter.util import get_remote_address

# For our api documentation using swagger
from flask_swagger_ui import get_swaggerui_blueprint

# for caching result
from flask_caching import Cache

# Import modules that we create
from api import developers, langs

import os 



config = {
    "DEBUG": True,          		# some Flask specific configs
    "CACHE_TYPE": "simple", 		# Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 60,	# Set default timeout to 60 minute
    "JSON_SORT_KEYS" : False		# this for keeping the order of json data
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# Initialize limiter with default 
limiter = Limiter(
    app,
    key_func=get_remote_address,
    headers_enabled=True,
    default_limits=["40 per hour"],
)

# Rate limit headers
limiter.header_mapping = {
    HEADERS.LIMIT : "X-My-Limit",
    HEADERS.RESET : "X-My-Reset",
    HEADERS.REMAINING: "X-My-Remaining",
}


# app.config['JSON_SORT_KEYS'] = False


@app.route('/docs/<path:path>')
def send_static(path):
    return send_from_directory('../docs', path)

# API Documentation config
SWAGGER_URL = '/docs'
API_URL = '/docs/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Github_Trendings"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from api import main
from api import errors_view