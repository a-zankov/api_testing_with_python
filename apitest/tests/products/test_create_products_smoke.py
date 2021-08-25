from apitest.src.utilities.genericUtilities import generate_random_string
from apitest.src.helpers.products_helper import ProductHelper
from apitest.src.dao.products_dao import ProductsDAO
import pytest

@pytest.mark.tcid26
@pytest.mark.products
def test_create_1_simple_product():
    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    products_rs = ProductHelper().call_create_product(payload=payload)

    # verify the response is not empty
    assert products_rs, f"Create product api response is empty. Payload: {payload}"
    assert products_rs['name'] == payload['name'], "Create product response has unexpected name" \
                                                   f"Expected: {payload['name']}. Actual: {products_rs['name']} "
    # verify the product exists in db
    products_id = products_rs['id']
    db_product = ProductsDAO().get_product_by_id(products_id)

    assert payload['name'] == db_product[0]['post_title'], "Created product title in db does not match" \
                                                           "title in API payload"
