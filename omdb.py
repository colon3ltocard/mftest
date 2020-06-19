"""
Utility module to query omdb.
http://www.omdbapi.com/
http://www.omdbapi.com/?apikey=[yourkey]&
"""

import requests

SECRET_TOKEN = "b1f1cb14"  # never do that in production
OMDB_URL = "http://www.omdbapi.com"


def get_movies(movie_title_search_string="met", release_year="", mtype="movie"):
    """
    Utility function to retrieve results from the omdb website
    :param title:
    :param release_year:
    :param mtype:
    :return:
    """
    params = {"t": movie_title_search_string,
              "y": release_year, "type": mtype, "apikey": SECRET_TOKEN}
    response = requests.get(f"{OMDB_URL}", params=params)
    return response.json()


if __name__ == "__main__":
    response = get_movies()
    print(response.json())


