from api import *
import urllib

# Override the default key generation
# this for url with query string
def cache_key():
   args = request.args
   key = request.path + '?' + urllib.urlencode([
     (k, v) for k in sorted(args) for v in sorted(args.getlist(k))
   ])
   return key

# General inform that user may need
@app.route('/', methods = ['GET'])
def general_msg():
    return jsonify({
        "trending_github_languages_url"		: "%slanguages" %(request.base_url),
        "trending_github_repositories_url"	: "%srepositories" %(request.base_url),
        "trending_github_devlopers_url"		: "%sdevelopers/{language}{?since, daily, weekly, monthly}" %(request.base_url),
        "documentation_url"					: "%sdocs" %(request.host_url)
    }), 200


# return list of languages in 100 trending repo on github based on number of
# stars and forks of the project each languages with list of repos created in it
@app.route('/languages', methods = ['GET'])
@cache.cached()
def laguages_list():
    return jsonify(langs.trending_languages()), 200, limiter.header_mapping


# return trending developer
@app.route('/developers', methods = ['GET'])
@cache.cached(key_prefix=cache_key)
def trending_developers():
    range = request.args['since'] if 'since' in request.args else 'daily'
    # check range validity
    if range not in ['daily', 'weekly', 'monthly']:
        return jsonify({
                    "status"				: "422",
                    "title"					: "Invalid Attribute",
                    "detail"				: "range must be one of ['daily', 'weekly', 'monthly']",
                    "documentation_url"		: "%sdocs" %(request.host_url)
                }), 422
    return jsonify(developers.trending_developers(range=range)), 200


@app.route('/developers/<lang>', methods = ['GET'])
@cache.cached(key_prefix=cache_key)
def trending_developers_lang(lang):
    range = request.args['since'] if 'since' in request.args else 'daily'
    # check range validity
    if range not in ['daily', 'weekly', 'monthly']:
        return jsonify({
                    "status"				: "422",
                    "title"					: "Invalid Attribute",
                    "detail"				: "range must be one of ['daily', 'weekly', 'monthly']",
                    "documentation_url"		: "%sdocs" %(request.host_url)
                }), 422
    return jsonify(developers.trending_developers(language=lang, range=range,)), 200