from bs4 import BeautifulSoup
import requests as req
import json


def get_developers(html):
	'''
		Parameter :
			html : the html content of trending developers in Github page
		Return :
			list of trending developers parased from html content, With name,
			profile url, profile image, rank
	'''
	developers_list = []
	# Initalize BeautifulSoup objet
	soup = BeautifulSoup(html, 'html.parser')

	# the developers name is inside h1 with class name 'h3 lh-condensed'
	# we find heading with this class
	h1_tags = soup.findAll(class_='h3 lh-condensed')

	# Loop through all tags and extract developer name and url profile
	for h1_tag in h1_tags:
		a_tag = h1_tag.find('a')
		developer = {
			"name" : a_tag.string.strip(),
			"url" : "https://github.com%s" %(a_tag['href'])
		}

		# add the developer to the list
		developers_list.append(developer)
	return developers_list


def get_repositories(html):
	'''
		Parameter :
			html : the html content of trending developers in Github page
		Return :
			list of trending developers's repositorie parased from html content,
			With name, profile url, profile image, rank
	'''
	developers_repo_list = []
	# Initalize BeautifulSoup objet
	soup = BeautifulSoup(html, 'html.parser')

	# the repositorie name is inside h1 with class name 'h4 lh-condensed'
	# we find heading with this class
	h1_tags = soup.findAll(class_='h4 lh-condensed')
	# Loop through all tags and extract developer name and url profile
	for h1_tag in h1_tags:
		a_tag = h1_tag.find('a')
		repositorie = {
			"name" : a_tag.text.strip(),
			"url" : "https://github.com%s" %(a_tag['href'])
		}

		# add the developer to the list
		developers_repo_list.append(repositorie)
	return developers_repo_list


def trending_developers(range='daily', language=None):
	'''
		parameters:
			range : can take one value [default = daily, weekly, monthly]
			language: language name [default : all languges]
		Returns :
			json data with trending developers on range given, in one langugage
			or all languages, the json containe:
				developer_name, developer_github_profile, developer, trending_repo
	'''
	# check range validity
	if range not in ['daily', 'weekly', 'monthly']:
		return {
					"error": [
						{
						"status": "422",
						"title":  "Invalid Attribute",
						"detail": "range must be one of ['daily', 'weekly', 'monthly']"
						}
					]
				}
	
	# Get page html content
	if language != None:
		html = req.get("https://github.com/trending/developers/%s?since=%s" %(language, range)).text
	else:
		html = req.get("https://github.com/trending/developers?since=%s" %(range)).text
	
	# add list of trending developers
	result = {"trending_developers" : get_developers(html)}
	
	# get trending repositories list
	repos_list = get_repositories(html)
	# Add eatch repo to it's owner
	for dev, repo in zip(result['trending_developers'], repos_list):
		dev['trending_repositories'] = repo
	print(json.dumps(result, indent=2))
	return result
