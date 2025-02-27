import allure
from loguru import logger

from lesson1.api_tests.services.case.models import Priority, Case
import lesson1.api_tests.services.case.data as d
from lesson1.api_tests.utils.api_client import client
x = d.create_case_dict
y = d.update_case_dict

@allure.feature('TC')
@allure.story('Create a TC')
def test_create_tc(json=x):
    response = client.make_request(handle="/testcases", method="POST", json=json)
    assert response.json_should_be_eq(x)

@allure.feature('TC')
@allure.story('Get a list of TC')
def test_get_tc():
    response = client.make_request(handle="/testcases", method="GET")
    assert response.status_code_should_be_eq(200)

@allure.feature('TC')
@allure.story('Update a TC')
def test_upd_tc(json = y):
    response = client.make_request(handle=f"/testcases/{x['id']}", method="PUT", json=json)
    assert response.status_code_should_be_eq(200)
    assert response.json_should_be_eq(y)

@allure.feature('TC')
@allure.story('Delete a TC')
def test_del_test():
    response = client.make_request(handle=f"/testcases/{x['id']}", method="DELETE")
    assert response.status_code_should_be_eq(200) or response.status_code_should_be_eq(404)
