from flask import Flask, jsonify
import process_data

app = Flask(__name__)

# General message to inform user how to use api
# and let user know about documentaiont available
@app.route('/')
def general_msg()
	return "general info"
# return list of languages in 100 trending repo on github
# with the number of repos for each languages and list of repos created in it
@app.route('/languages')
def laguages_list():
	return "list of language in 100 trending repo"

# return only trending repos name ,owner_name, repo_url, stars_number, forked_number
# based on must starred 
@app.route('/repositories')
def trending_repo():
	return "trending repo"

# return trending developer
@app.route('/devlopers')
def trending_devlopers():
	return "trending devlopers"

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 8100)