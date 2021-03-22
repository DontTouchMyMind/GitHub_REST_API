import requests

from app import app


SOURCE_URL = 'https://api.github.com/'
REPO = '/PyGithub/PyGithub'
API_URL = '/api/v1.0/'

client = app.test_client()


def pytest_connection_to_source():
    r = requests.get(SOURCE_URL)
    assert r.status_code == 200


def pytest_connection_error_to_source():
    r = requests.get("https://api.github.com/2;3k4m;219")
    assert r.status_code == 404


def pytest_get_repos_info():
    rv = client.get(f'{API_URL}repos{REPO}')
    assert rv.status_code == 200
    assert rv.get_json() != []


def pytest_get_all_pulls_route():
    rv = client.get(f'{API_URL}pulls{REPO}')
    assert rv.status_code == 200
    assert rv.get_json() != []


def pytest_get_pulls_not_merged_route():
    rv = client.get(f'{API_URL}pulls-not-merged{REPO}')
    assert rv.status_code == 200
    assert rv.get_json() != []


def pytest_get_all_forks_route():
    rv = client.get(f'{API_URL}forks{REPO}')
    assert rv.status_code == 200
    assert rv.get_json() != []


def pytest_get_issues_route():
    rv = client.get(f'{API_URL}issues{REPO}')
    assert rv.status_code == 200
    assert rv.get_json() != []
