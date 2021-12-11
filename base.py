import abc


class Middleware(abc.ABC):

    @abc.abstractmethod
    def __call__(self, environ, start_response):
        pass
