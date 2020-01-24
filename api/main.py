from flask import Flask, jsonify
from langs import languages
import langs

app = Flask(__name__)
# this for keeping the order of json data
app.config['JSON_SORT_KEYS'] = False

# General message to inform user how to use api
# and let user know about documentaiont available
@app.route('/')
def general_msg():

	return {"general" : "info"}
# return list of languages in 100 trending repo on github
# with the number of repos for each languages and list of repos created in it
@app.route('/languages')
def laguages_list():
	return jsonify(langs.trending_languages()), 200

# return only trending repos name ,owner_name, repo_url, stars_number, forked_number
# based on must starred 
@app.route('/repositories')
def trending_repo():
	return "trending repo"

# return trending developer

@app.route('/devlopers')
def trending_devlopers():
	return "trending devlopers"

@app.route('/rate_limit')
def famous_devloper():
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