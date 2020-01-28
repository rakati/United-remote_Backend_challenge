# This file containe errors view for better separation of code

from api import *


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
                    "status"               : "404",
                    "title"                : "Page Not Found",
                    "documentation_url"    : "%sdocs" %(request.host_url)
                    }), 404


@app.errorhandler(429)
def ratelimit_exceed(e):
    return jsonify({
                    "status"                : "429",
                    "title"                 : "Ratelimit exceeded",
                    "message"               : "You exceed rate limit for this entrypoint check documentation for more info about rate limit",
                    "documentation_url"     : "%sdocs" %(request.host_url)
                    }), 429
    
@app.errorhandler(405)
def method_error(e):
    return jsonify({
                    "status"                : "405",
                    "title"                 : "Method %s not allowed",
                    "message"               : "the api accept only GET method check docs for more info",
                    "documentation_url"     : "%sdocs" %(request.host_url)
                    }), 405
