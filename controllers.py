from datetime import datetime, timedelta

import requests
from flask import jsonify

from decorators import base_controllers
from response_structure import PullRequest, Issue, Fork

source_url = 'https://api.github.com/repos/'


def form_response(data, function_name):
    """Формируем ответ, согласно структуре."""
    result = []
    if function_name == 'get_all_pulls':
        for entity in data:
            result.append(PullRequest(
                id=entity['id'],
                title=entity['title'],
                creation_date=entity['created_at'],
                state=entity['state']
            ))
    elif function_name == 'get_issues':
        for entity in data:
            result.append(Issue(
                id=entity['id'],
                title=entity['title'],
                description=entity['body'],
                creation_date=entity['created_at']

            ))
    elif function_name == 'get_all_forks':
        for entity in data:
            result.append(Fork(
                id=entity['id'],
                owner=entity['owner']['html_url'],
                creation_date=entity['created_at']
            ))
    return result


@base_controllers
def get_repos_info(repos_name):
    """Получить детали репозитория."""
    r = requests.get(f'{source_url}{repos_name}')
    data = r.json()
    return jsonify(data)


@base_controllers
def get_all_pulls(repos_name):
    """Получить все пулл реквесты."""
    r = requests.get(f'{source_url}{repos_name}/pulls?state=all')
    data = r.json()
    return jsonify(form_response(data, get_all_pulls.__name__))


@base_controllers
def get_pulls_not_merged(repos_name):
    """Получить все пулл реквесты, не смерженные две недели."""
    r = requests.get(f'{source_url}{repos_name}/pulls?state=all')
    data = r.json()
    check_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=14)
    results = []
    for entity in data:
        created_date = datetime.strptime(entity['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if created_date <= check_day and entity['merged_at'] is None:
            results.append(PullRequest(
                id=entity['id'],
                title=entity['title'],
                creation_date=entity['created_at'],
                state=entity['state']
            ))
    return jsonify(results)


@base_controllers
def get_issues(repos_name):
    """Получить список Issues"""
    r = requests.get(f'{source_url}{repos_name}/issues?state=all')
    data = r.json()
    return jsonify(form_response(data, get_issues.__name__))


@base_controllers
def get_all_forks(repos_name):
    """Получить количество форков."""
    r = requests.get(f'{source_url}{repos_name}/forks')
    data = r.json()
    return jsonify(form_response(data, get_all_forks.__name__))
