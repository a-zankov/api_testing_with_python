
import pytest
import logging as logger

from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.helpers.customers_helper import CustomerHelper


@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")

    random_info = generate_random_email_and_password()
    logger.info(random_info)
    email = random_info['email']
    password = random_info['password']

    #create payload
    # payload = {'email': email, 'password': password}

    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    import pdb; pdb.set_trace()

    #verify status code of the call

    #verify email in the response

    # verify customer is created in database