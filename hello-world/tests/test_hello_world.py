from hello_world import __version__
from hello_world.hello import Hello


def test_version():
    assert __version__ == '0.1.0'

def test_hello():
    hello = Hello()
    assert hello.hello() == "Hello"
