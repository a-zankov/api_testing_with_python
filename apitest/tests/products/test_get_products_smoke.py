
import pytest
from apitest.src.utilities.requestsUtility import RequestsUtility
from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductHelper

@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():

    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')

    assert rs_api, "Response of list all products is empty"

@pytest.mark.products
@pytest.mark.tcid25
def test_get_product_by_id():
    #get product form db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']
    #make thr call
    product_helper = ProductHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']
    assert db_name == api_name, "Get product by id returned wrong product"


