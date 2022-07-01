from _pytest.fixtures import fixture

from setup.simple import SimpleSuite


@fixture(scope='function')
def simple_suite_fixture():
    """
    All required modules for simple test suite
    :return: the scope of required modules
    """
    simple_test_suite = SimpleSuite()
    yield simple_test_suite
    simple_test_suite.tear_down()
    del simple_test_suite
