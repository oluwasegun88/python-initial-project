import contextlib


@contextlib.contextmanager
def manage_context():
    print("Entering the context manager")
    yield 1
    print("Existing the context manager")


with manage_context() as one:
    print(one)


class ContextManager:
    def __enter__(self):
        print("Entering the context manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
