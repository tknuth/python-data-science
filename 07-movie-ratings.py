# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import altair as alt

# https://grouplens.org/datasets/movielens/
movies = pd.read_csv("./movies.csv")
movies["title_with_year"] = movies.title
movies[["title", "year"]] = movies.title_with_year.str.strip().str.extract("(.+) \((\d{4})\)$")

ratings = pd.read_csv("ratings.csv")
ratings.timestamp = pd.to_datetime(ratings.timestamp, unit="s")

# %%
# Welche Filme enthalten das Wort "Island"?
idx = []
for i, series in movies.iterrows():
    if pd.notna(series.title) and "Island" in series.title:
        idx.append(i)

movies.loc[idx]

# %%
movies[movies.title.notna() & movies.title.str.contains("Island")]

# %%
# Welcher Film hat die meisten Genres?
genres = [
    "Action",
    "Adventure",
    "Animation",
    "Children",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "IMAX",
    "War",
    "Western",
]

l = []

for i, series in movies.iterrows():
    c = 0
    for genre in genres:
        if genre in series.genres:
            c += 1
    l.append(c)
    
movies["n_genres"] = l

# %%
# Zählen Sie, wie oft die einzelnen Genres vorkommen
d = {}

for genre_list in movies.genres.str.split("|"):
    for genre in genre_list:
        if genre in d:
            d[genre] = d[genre] + 1
        else:
            d[genre] = 1

d

# %%
d = {}

for genre_list in movies.genres.str.split("|"):
    for genre in genre_list:
        d[genre] = d.get(genre, 0) + 1

d

# %%
l = []

for i, series in movies.iterrows():
    l.append(len(series.genres.split("|")))
    
movies["n_genres"] = l


# %%
def count_genres(text):
    return len(text.split('|'))

movies["n_genres"] = movies.genres.apply(count_genres)

# %% [markdown]
# - Wie viele Filme gibt es?
# - Welcher Titel kommt am häufigsten vor?
# - Wie viele Filme sind nicht eindeutig benannt, d.h. sie haben Duplikate?
# - Wie viele Filmtitel kommen mehrfach vor?
# - Erstellen Sie ein Balkendiagramm der Anzahl Filme pro Jahr.
# - Wie sind Durchschnitt, Median und Modus der Bewertungen (pro Genre)?
# - Wie viele Action-Filme gibt es?
# - Wie viele Dokumentationen gibt es?
# - Wie viele Action-Dokumentationen gibt es?
# - Gibt es User, deren Bewertungen als Ausreißer gelten?
# - Wie ist die durchschnittliche Bewertung der Action-Dokumentationen?
# - Welcher Film wurde am häufigsten bewertet (auch: "alterskorrigiert")?
# - Welcher Film erhielt 2018 die häufigsten Bewertungen?
# - Stellen Sie eine eigene Frage und Antwort vor.
# - Welche Wörter sind in den Filmtiteln am häufigsten?
# - Visualisieren Sie die Bewertungen eines einzelnen Users
# - In welchem Jahr wurden die meisten Filme bewertet?
# - Erstellen Sie ein Histogramm der durchschnittlichen Bewertungen für einzelne User.
# - Erstellen Sie einen Boxplot der durchschnittlichen Bewertungen für einzelne User.
# - Erstellen Sie ein Balkendiagramm der Anzahl Filmbewertungen pro Jahr.
# - Visualisieren Sie für ein paar Filme die Anzahl Bewertungen nach Jahren seit Veröffentlichung.
# - Wählen Sie zwei beliebige Filme und visualisieren die Bewertungen der Nutzer, z.B. mit `df.pivot`.
