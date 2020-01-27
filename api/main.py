from api import *


# General inform that user may need
@app.route('/')
@limiter.limit("2 per minute")
def general_msg():
	return jsonify({
		"trending_github_languages_url"		: "%s/languages" %(request.base_url),
		"trending_github_repositories_url"	: "%s/repositories" %(request.base_url),
		"trending_github_devlopers_url"		: "%s/developers/{language}{?since, daily, weekly, monthly}" %(request.base_url),
		"trending_github_rate_limit_url"	: "%s/rate_limit" %(request.base_url),
		"documentation_url"					: "%s/docs" %(request.base_url)
	}), 200


# return list of languages in 100 trending repo on github based on number of
# stars and forks of the project each languages with list of repos created in it
@app.route('/languages')
def laguages_list():
	return jsonify(langs.trending_languages()), 200, limiter.header_mapping


# return trending developer
@app.route('/developers')
def trending_developers():
	range = request.args['since'] if 'since' in request.args else 'daily'
	# check range validity
	if range not in ['daily', 'weekly', 'monthly']:
		return jsonify({
					"status": "422",
					"title":  "Invalid Attribute",
					"detail": "range must be one of ['daily', 'weekly', 'monthly']"
				}), 422
	return jsonify(developers.trending_developers(range=range)), 200


@app.route('/developers/<lang>')
def trending_developers_lang(lang):
	range = request.args['since'] if 'since' in request.args else 'daily'
	# check range validity
	if range not in ['daily', 'weekly', 'monthly']:
		return jsonify({
					"status": "422",
					"title":  "Invalid Attribute",
					"detail": "range must be one of ['daily', 'weekly', 'monthly']"
				}), 422
	return jsonify(developers.trending_developers(language=lang, range=range,)), 200


@app.route('/rate_limit')
def famous_developer():
	# return information about rate limit : rateLimit_remaining,
	# rateLimit_limit
	return "rate limit"


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
					"status": "404",
					"title":  "Page Not Found",
					"documentation_url": "localhost:8100/docs"
				}), 404


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(
		{
			"status"	:	"429",
			"title"		:	"Ratelimit exceeded",
			"message"	:	"You exceed rate limit for this entrypoint check documentation for more info about rate limit"
		}), 429
