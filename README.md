# NewsAggregator

A news aggregator built on top of the news api and reddit api.

Developed on Ubuntu 16.04 with Anaconda Python 3.9.1

Some specifications can be found [here](https://github.com/meddyco/news-aggregator-v2/blob/master/README.md)

## How to run
#### Requirements:
python, fastapi, requests, uvicorn and of course their dependencies.

I used a conda environment but you can use a virtual environment instead.
If you are using conda, you can setup the environment as:

```
conda create -n newsagg
conda activate newsagg
conda install -c conda-forge fastapi
conda install -c conda-forge uvicorn
conda install requests
```

After installing the requirements, please go to the project folder and run `uvicorn main:app --reload` in a terminal or cmd.
The `--reload` flag is to be able to see changes made to the source code instantly.

Then open up a browser and head to `http://127.0.0.1:8000/news` to see the `list` functionality in action.
Head to `http://127.0.0.1:8000/news?query=corona` to see the `search` functionality.

In the first time a popup will open and ask for username and password for HTTP basic authentication. For demonstration purposes only one user is allowed for now. `username = please, password = open`. If other pairs are provided the popup will ask again.

I would like to mention some details for they may be useful to whom ever interested.  
In the public_apis folder there is a module for each public api used. Each module has a handler class that implements search and list_news methods for desired 2 functionalities. The results from these are combined in get_news method / endpoint in main.py

It is possible to combine the two above mentioned handler classes in one module. And discard public_apis package but if things are to get larger in the future, current design may be a better choice. That is why I left things this way.

I have used built-in lru cache support on individual api calls. I set cache size to 32 for now. Since we are not using any databases I did not setup a different persistent storage for caching but that is of course also possible.

I used standard unittest. You can run all tests as `python -m unittest discover`

I have not published my password and api keys for apis for the sake of security and privacy. They are in newsapi.py and reddit.py inside public_apis package. I replaced those with the string 'XXXX' so that you can find them easily and replace them with your own.

newsapi.py only need an api key in two places.

reddit.py needs username, password, an api key and an id. Which are all in _refresh_access_token method.

If you need further help please open up an issue or contact me.
Giray
