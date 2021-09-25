import requests
from urllib.parse import urljoin
from functools import lru_cache
from .baseapi import BaseApi

class RedditHandler(BaseApi):
    """Class for handling reddit api calls.

    Attributes
    ----------
    access_token_info : str
        The access token used for api calls `access_token_info`.

    """

    access_token_info = None

    @classmethod
    def _refresh_access_token(cls):
        """Refreshes the access token which expires after a while.
        """
        base_url = 'https://www.reddit.com/'
        access_token_data = {'grant_type': 'password', 'username': 'XXXX', 'password': "XXXX"}
        auth = requests.auth.HTTPBasicAuth('XXXX', 'XXXX')
        res = requests.post(urljoin(base_url, 'api/v1/access_token'),
            data=access_token_data,
            headers={'user-agent': 'fun and games by gry1448'},
            auth=auth)
        response_dict = res.json()
        cls.access_token_info = response_dict

    @classmethod
    def _fetch(cls, query, relative_endpoint):
        """Makes a query to given end point in reddit api.

        Parameters
        ----------
        query : str
            The query string `query`. Example: corona
        relative_endpoint : str
            The end point to make the request to `relative_endpoint`. Example : '/r/news/search'

        Returns
        -------
        requests.models.Response
            The response from the reddit api.

        """
        token = 'bearer ' + cls.access_token_info['access_token']

        api_url = 'https://oauth.reddit.com'

        # headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
        headers = {'Authorization': token, 'User-Agent': 'fun and games by gry1448'}

        payload = {'q': query, 'limit': 100, 'sort': 'relevance', 'restrict_sr':'on'}
        response = requests.get(urljoin(api_url, relative_endpoint), headers=headers, params=payload)
        return response

    @classmethod
    def _get_content(cls, *args):
        """A wrapper around _fetch function to overcome expiring access token issue.
        Refreshes the access_token if it must. Then retrieves the content from the api.

        Parameters
        ----------
        *args : type
            All the arguments to pass down `*args`.

        Returns
        -------
        requests.models.Response
            The response from the reddit api.

        """
        if cls.access_token_info is None:
            cls._refresh_access_token()

        response = cls._fetch(*args)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            cls._refresh_access_token()
            return cls._fetch()


    @classmethod
    @lru_cache(32)
    def search(cls, query):
        """Makes a search query using reddit api. Only in news catergory.

        Parameters
        ----------
        query : str
            The query string `query`. Example: corona

        Returns
        -------
        list
            List of query results.

        """
        content = cls._get_content(query, '/r/news/search')
        return cls._extract_info(content)

    @classmethod
    @lru_cache(32)
    def list_news(cls):
        """List of news from the reddit api Only real news are returned.

        Returns
        -------
        list
            List of news.

        """
        content = cls._get_content(None, '/r/news')
        return cls._extract_info(content)

    @classmethod
    def _extract_info(cls, response):
        """Extracts desired fields from all the data coming from reddit api.

        Parameters
        ----------
        res_json : dict
            A dictionary object for response json `res_json`.

        Returns
        -------
        type
            Extracted fields from given json.
        """
        return [{'headline':child['data']['title'],
                 'link': child['data']['url'],
                 'source':'reddit'} for child  in response['data']['children']]
