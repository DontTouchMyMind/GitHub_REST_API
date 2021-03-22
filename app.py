import logging

from flask import Flask

from controllers import get_repos_info, get_all_pulls, get_pulls_not_merged, get_all_forks, get_issues

app = Flask(__name__)


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('log/errors.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


logger = setup_logger()


@app.route('/api/v1.0/repos/<path:repos_name>', methods=['GET'])
def get_repos_info_route(repos_name):
    """Маршрут для получения деталей репозитория."""
    return get_repos_info(repos_name)


@app.route('/api/v1.0/pulls/<path:repos_name>', methods=['GET'])
def get_all_pulls_route(repos_name):
    """Маршрут для получения всех пул реквестов репозитория."""
    return get_all_pulls(repos_name)


@app.route('/api/v1.0/pulls-not-merged/<path:repos_name>', methods=['GET'])
def get_pulls_not_merged_route(repos_name):
    """Маршрут для получения всех пул реквестов, которые не были смёрджены 2 недели и более."""
    return get_pulls_not_merged(repos_name)


@app.route('/api/v1.0/forks/<path:repos_name>', methods=['GET'])
def get_all_forks_route(repos_name):
    """Маршрут для получения всех форков репозитория"""
    return get_all_forks(repos_name)


@app.route('/api/v1.0/issues/<path:repos_name>', methods=['GET'])
def get_issues_route(repos_name):
    """Маршрут для получения всех Issues репозитория."""
    return get_issues(repos_name)


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as err:
        logger.error(f'{err}')
