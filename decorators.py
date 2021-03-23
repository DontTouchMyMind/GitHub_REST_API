import functools


def base_controllers(func):
    """Decorator for handling exceptions in controllers."""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as err:
            return {'message': str(err)}, 400
        except KeyError as err:
            return {'message': str(err)}, 400
        except TypeError as err:
            return {'message': str(err)}, 400

    return inner
