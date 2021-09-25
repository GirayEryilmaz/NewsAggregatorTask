from authentication import  check_credentials
from public_apis.api_config import registry

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from typing import Optional

import importlib


app = FastAPI()

security = HTTPBasic()


@app.get("/news")
def get_news(query: Optional[str]=None, credentials: HTTPBasicCredentials = Depends(security)):
    """Endpoint for news search from 3rd party apis with basic authentication. Servers json over http.

    Parameters
    ----------
    query : Optional[str]
        Optional query string `query`.
    credentials : HTTPBasicCredentials
        credentials provided by fastapi basic authentication `credentials`.

    Returns
    -------
    list
        List of aggregated results.

    """
    if not check_credentials(credentials.username, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    if not query:
        all_news = []
        for module_name, class_name in registry:

            module = importlib.import_module('public_apis.'+module_name)
            my_class = getattr(module, class_name)
            news = my_class.list_news()
            all_news.extend(news)
        return all_news
    else:
        news_api_search_results = NewsApiHandler.search(query)
        reddit_search_results = RedditHandler.search(query)
        return news_api_search_results + reddit_search_results
