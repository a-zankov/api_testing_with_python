
import pytest
import logging as logger

from apitest.src.utilities.genericUtilities import generate_random_email_and_password
from apitest.src.helpers.customers_helper import CustomerHelper
from apitest.src.dao.customers_dao import CustomersDAO
from apitest.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
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


    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', "Create customer api return value for first name" \
                                              "but it should be empty"


    # verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID'] ###Verify che za prikol
    assert  id_in_api == id_in_db, 'Create customer response "id" not same as "ID" in database' \
                                   f'Email: {email}'


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    #get existing email from db
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']
    #call the API
    req_helper = RequestsUtility()
    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == f"registration-error-email-exists', 'Create customer with existing email' \
                                    'error code is not correct. Expected: registration-error-email-exists, ' \
                                                                       'Actual: {cust_api_info['code']}"

