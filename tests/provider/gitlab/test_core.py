import os
import pytest
from src.provider import gitlab


def test_fetch_slug():
	if 'GITLAB_TOKEN' in os.environ:
		result = gitlab.fetch('https://gitlab.com', '7311836', os.environ['GITLAB_TOKEN'])

		assert result[0]['provider'] == 'gitlab'
		assert result[0]['active'] is True
		assert result[0]['status']
	else:
		pytest.skip('GITLAB_TOKEN not defined')


def test_fetch_invalid():
	result = gitlab.fetch(None, None, None)

	assert result == []