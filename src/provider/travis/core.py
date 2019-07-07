import requests
from .normalize import normalize_data

args = None


def init(program):
	global args

	program.add_argument('--travis-host', default = 'https://api.travis-ci.org')
	program.add_argument('--travis-slug', action = 'append', required = True)
	args = program.parse_known_args()[0]


def run():
	host = args.travis_host
	slugs = args.travis_slug
	result = []

	for slug in slugs:
		result.extend(fetch(host, slug))
	return result


def fetch(host, slug):
	response = None

	if host and slug:
		response = requests.get(host + '/repos/' + slug, headers =
		{
			'Accept': 'application/vnd.travis-ci.2.1+json'
		})

	# process response

	if response and response.status_code == 200:
		data = response.json()
		if 'repo' in data:
			return normalize_data(data['repo'])
		if 'repos' in data:
			result = []
			for project in data['repos']:
				result.extend(normalize_data(project))
			return result
	return []
