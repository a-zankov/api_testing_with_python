
from apitest.src.utilities.requestsUtility import RequestsUtility


class ProductHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)