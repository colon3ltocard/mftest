# Intro

FastAPI programming test.

# TODO

POST /foobar
body de la requête HTTP POST:
{
"movie_title_search_string": "met",
"release_year": 2000,
"type": "movie"
}
aucun parametre n'est obligatoire, le premier est une chaine,
le deuxième est un entier le troisieme (si présent) est "movi
e", "series" ou "episode"

le WS ainsi spécifié exploitera dynamiquement le WS en ligne O
MDB pour faire la recherche et retourner les résultats en JSON
avec un content_type "qui va bien"

le WS gèrera les cas d'erreurs les plus courants (erreur du cl
ient, erreur du serveur...) avec des codes retours HTTP approp
riés

montrer une invocation du WS ainsi développé avec "curl"

# Install and run

```shell script
pyenv virtualenv 3.8.3 mftestenv
pyenv activate mftestenv
pip install -r mftest/requirements.txt
uvicorn mftest.main:app --reload
```

Navigate to http://127.0.0.1:8000/docs


