import json
import requests
from datetime import date, timedelta

def	get_repositories_of_lagugage(search_lang, repos_list):
	'''
		Parameters:
			repos_list (string): list of repositories
			search_lang (string): languages name
		Returns:
			list of repositories with search_lang as primary language
	'''
	languga_repos = []
	for repo in repos_list:
		if repo['language'] == search_lang:
			# construct repo with information we need
			temp_repo = {
				"repositorie_name" : repo['name'],
				"owner_name" : repo['owner']['login'],
				"repositorie_url" : repo['html_url'],
				"forks" : repo['forks'],
				"watchers" : repo['watchers'],
				"stars" : repo['stargazers_count']
			}
			languga_repos.append(temp_repo)
	return languga_repos


def trending_languages():
	'''
		Use the github api for finding most trending repositories
		Based on number of stars and forks, then filter this 
		data and 
		Rretuns : 
			json data with info below
			list of languages:
				language name
				number of repositories
				list of repositories
					repos name
					repositorie owner name
					repositorie url
					repositorie number of forks
					repositorie number of stars
					repositorie number of watchers

	'''
	# get date of Previous month
	prev_month = (date.today().replace(day=1) - timedelta(days=1))
	url = "https://api.github.com/search/repositories?q=created:>=%s&sort=stars&order=desc&per_page=100" %(prev_month.strftime("%Y-%m-%d"))
	resp = requests.get(url)
	data = resp.json()
	
	# Extract trending languages
	languages_set = {item['language'] for item in data['items'] if item['language'] != None}

	res = {
		"languages_count" : len(languages_set),
		"incomplete_results": data['incomplete_results'],
		"languages" : []
	}
	for language in languages_set:
		language_repos = get_repositories_of_lagugage(language, data['items'])
		res['languages'].append({
			"name" : language,
			"repositories_count" : len(language_repos),
			"repositories" : language_repos
		})
	return res