import logging

from flask import Flask

from controllers import get_repos_info, get_all_pulls, get_pulls_not_merged, get_all_forks, get_issues

app = Flask(__name__)


def setup_logger():
    """Logger configuration."""
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
    """The route to get the details of the repository."""
    return get_repos_info(repos_name)


@app.route('/api/v1.0/pulls/<path:repos_name>', methods=['GET'])
def get_all_pulls_route(repos_name):
    """The route to get all the pull requests list for the repository."""
    return get_all_pulls(repos_name)


@app.route('/api/v1.0/pulls-not-merged/<path:repos_name>', methods=['GET'])
def get_pulls_not_merged_route(repos_name):
    """The route to get a list of all pull requests which have not been merged for two weeks or more."""
    return get_pulls_not_merged(repos_name)


@app.route('/api/v1.0/forks/<path:repos_name>', methods=['GET'])
def get_all_forks_route(repos_name):
    """The route to get a list of all forks of the repository."""
    return get_all_forks(repos_name)


@app.route('/api/v1.0/issues/<path:repos_name>', methods=['GET'])
def get_issues_route(repos_name):
    """The route to get a list of all issues."""
    return get_issues(repos_name)


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as err:
        logger.error(f'{err}')
