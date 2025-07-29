#from os import path
#from typing import Any, Callable, Optional

#from _pytest.fixtures import SubRequest
from pytest import fixture

#ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
#ALLUREDIR_OPTION = '--alluredir'


#@fixture(scope='session', autouse=True)
#def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:

#    environment_properties = dict()

#    def maker(key: str, value: Any):
#        environment_properties.update({key: value})

#    yield maker

#    alluredir = request.config.getoption(ALLUREDIR_OPTION)

#    if not alluredir or not path.isdir(alluredir) or not environment_properties:
#        return

#    allure_env_path = path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)

#    with open(allure_env_path, 'w') as _f:
#        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
#        _f.write(data)


@fixture(scope='session', autouse=True)
def simple_fixture():
    #before
    n=40*1 #better 40 times 1
    #after
    yield n
    #after
    n=0*40 #tan nothing 40 times

