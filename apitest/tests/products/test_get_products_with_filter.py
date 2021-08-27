
from apitest.src.helpers.products_helper import ProductHelper
from apitest.src.dao.products_dao import ProductsDAO
import pytest
from datetime import datetime, timedelta
import pdb
@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        #create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = tmp_date.strftime('%Y-%m-%dT%H:%m:%S')

        payload = dict()
        payload['after'] = after_created_date


        #make the call
        rs_api = ProductHelper().call_get_products_list(payload=payload)
        assert rs_api, "Empty response for list of products"

        #get data from db
        db_products = ProductsDAO().get_product_created_after_given_date(after_created_date)

        #verify response
        assert len(rs_api) == len(db_products), "List of product returned un expected amount of products:" \
                                                f"Expected: {len(db_products)}. Actual: {len(rs_api)}"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]
        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, "List products with filter after. IDs in api response mismatch response in db"

