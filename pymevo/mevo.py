import requests
from pymevo import user_agents


class MevoException(Exception):
    pass


class Mevo(object):
    stationmap_url = "https://rowermevo.pl/mapa-stacji/"
    locationjs_url = "https://rowermevo.pl/locations.js"

    def __init__(self, init=True, user_agent=None, https_proxy=None):
        self.cookies = None
        self.key = None
        self.user_agent = user_agent
        self.https_proxy = https_proxy
        if init:
            self.retrieve_key_and_cookies()

    def retrieve_key_and_cookies(self):
        session = requests.Session()
        mapstation_result = session.get(Mevo.stationmap_url,
                                        headers=self._create_user_agent_header(),
                                        proxies=self._create_proxies())
        if mapstation_result.status_code != 200:
            raise MevoException(mapstation_result.status_code, mapstation_result.text)
        self.key = [elem for elem in mapstation_result.text.split() if elem.startswith("src=\"/locations.js?")][0][18:-11]
        self.cookies = session.cookies.get_dict()

    def get_locationjs(self):
        url = Mevo.locationjs_url + self.key
        response = requests.get(url,
                                cookies=self.cookies,
                                headers=self._create_user_agent_header(),
                                proxies=self._create_proxies())
        if response.status_code != 200:
            raise MevoException(response.status_code, response.text)
        return response.text

    def _create_user_agent_header(self):
        self.user_agent = self.user_agent if self.user_agent is not None else user_agents.random_pick()
        return {
            "user-agent": self.user_agent
        }

    def _create_proxies(self):
        return {
            "https": self.https_proxy
        }
