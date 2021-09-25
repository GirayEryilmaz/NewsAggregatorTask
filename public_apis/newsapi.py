import requests
from urllib.parse import urljoin
from functools import lru_cache
from .baseapi import BaseApi

class NewsApiHandler(BaseApi):
    """Class for handling the news api calls.

    """

    @classmethod
    def _extract_info(cls, res_json):
        """Extracts desired fields from all the data coming from news api.

        Parameters
        ----------
        res_json : dict
            A dictionary object for response json `res_json`.

        Returns
        -------
        type
            Extracted fields from given json.
        """
        return [{'headline':art['title'],
             'link': art['url'],
             'source':'newsapi'} for art in res_json['articles']]

    @classmethod
    @lru_cache(32)
    def list_news(cls):
        """List of news from the news api. Only gets top headlines from general category for now.

        Returns
        -------
        list
            List of news.

        """
        main_url = "https://newsapi.org/v2/top-headlines"

        params = [('category', 'general'), ('pageSize', 100), ('sortBy', 'popularity'), ('apiKey','XXXX')]
        res = requests.get(main_url, params=params)
        info = cls._extract_info(res.json())
        return info

    @classmethod
    @lru_cache(32)
    def search(cls, query):
        """Makes a search in top headlines from general category with given query

        Parameters
        ----------
        query : str
            The query string `query`. Example: corona

        Returns
        -------
        list
            List of query results.

        """
        main_url = "https://newsapi.org/v2/top-headlines"
        params = [('q', query), ('category', 'general'), ('pageSize', 100), ('apiKey','XXXX')]
        res = requests.get(main_url, params=params)
        info = cls._extract_info(res.json())
        return info
