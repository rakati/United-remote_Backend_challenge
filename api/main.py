from flask import Flask, jsonify
from langs import trending_languages

import langs				# file containe code for trending languages
import developers 	# file containe code for trending developers

app = Flask(__name__)
# this for keeping the order of json data
app.config['JSON_SORT_KEYS'] = False

# General message to inform user how to use api
# and let user know about documentaiont available
@app.route('/')
def general_msg():
	return {"general" : "info"}


# return list of languages in 100 trending repo on github based on number of
# stars and forks of the project each languages with list of repos created in it
@app.route('/languages')
def laguages_list():
	return jsonify(langs.trending_languages()), 200


# return trending developer
@app.route('/developers')
def trending_developers():
	return jsonify(developers.trending_developers()), 200


@app.route('/rate_limit')
def famous_developer():
	# return information about rate limit : rateLimit_remaining,
	# rateLimit_limit
	return "rate limit"


@app.route('/rate_limit')
def rate_limit():
	# return information about rate limit : rateLimit_remaining,
	# rateLimit_limit
	return "rate limit"

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 8100)