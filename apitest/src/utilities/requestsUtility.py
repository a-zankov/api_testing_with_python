
import requests
from apitest.src.configs.hosts_config import API_HOSTS

class RequestsUtility(object):

    def __init__(self):

        self.base_url = "http://localhost:10003/wp-json/wc/v3/"
        pass


    def post(self):

        rs_api = requests.post(url, data, headers)


    def get(self):
        pass

