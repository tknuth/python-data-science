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
from vega_datasets import data
import pandas as pd
import numpy as np

airports = data.airports()

# %%
# In einem Notebook lässt sich der DataFrame tabellarisch anzeigen
airports.head()

# %%
# Auswahl bestimmter Spalten mit deren Namen
airports.head()[["iata", "name", "city"]]

# %%
# Auswahl bestimmter Spalten via Index
airports.head().iloc[:, 0:3]

# %%
# Auswahl bestimmter Zeilen via Index
airports.head().iloc[0:5]

# %%
# Kombination der Methoden
airports.loc[0:4, ["iata", "name", "city"]]

# %%
# Ausgabe der Menge einer Spalte
airports.country.unique()

# %%
# allgemeine Informationen
airports.info()

# %%
# deskriptive Statistik numerischer Spalten
airports.describe()

# %%
# Selektion mithilfe eines booleschen Index
# Welche Flughäfen liegen östlich des Nullmeridians?
airports[airports.longitude > 0]

# %%
# Wie viele Flughäfen liegen östlich des Nullmeridians?
sum(airports.longitude > 0)
(airports.longitude > 0).sum()
len(airports[airports.longitude > 0])

# %%
# Wie viel Prozent der Flughäfen im Datensatz liegen in Kalifornien?
(airports.state == "CA").mean()*100

# %%
# Welcher Staat hat die meisten Flughäfen?
airports.state.value_counts().head()

# %%
# Bei welchen Flughäfen fehlen Angaben zum Staat?
airports[airports.state.isna()]

# %%
# Bei welchen Variablen fehlen Werte?
airports.isna().mean()

# %%
# Welche Flughäfen tragen "International" im Namen?
airports[airports.name.str.contains("International")]

# %%
# Welche Namen existieren mehrfach?
# Achtung, `keep=False` kann verwirren, vgl. Dokumentation
# https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html
airports[airports.duplicated(subset=["name"], keep=False)].sort_values("name")

# %%
# Welche Flughäfen liegen in New York oder Kalifornien?
airports[(airports.state == "CA") | (airports.state == "NY")]
airports[airports.state.isin(["CA", "NY"])]

# %%
# Welche Flughäfen liegen außerhalb der USA?
airports[airports.country != "USA"]
