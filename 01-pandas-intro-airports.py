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

# %% [markdown]
# ## Themen
#
# - Nutzung von pandas und vega_datasets
# - DataFrames und Series, `.shape` und `.dtypes`
# - Auswahl von Spalten und Zeilen mit `[]`, `.loc[]` und `.iloc[]`
# - Übersicht mit `.describe()` und `.info()`
# - Aggregationen: `.mean()`, `.sum()` und `.value_counts()`
# - fehlende Werte: `.isna()`, `.notna()` und `.fillna()`
# - Nutzung der String-Methoden mit `series.str`
# - Duplikation von Daten: `.duplicated()` und `.drop_duplicates()`
# - boolesche Series für Filterung
# - Arbeit mit der pandas-Dokumentation

# %%
from vega_datasets import data
import pandas as pd
import numpy as np

airports = data.airports()

# %%
# In einem Notebook lässt sich der DataFrame tabellarisch anzeigen.
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
(airports.state == "CA").mean() * 100

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

# %%
# Setzen eines Index zum schnellen Abrufen
airports.set_index("iata").loc[["JFK", "LAX"]]

# %%
# Löschen von Spalten oder Zeilen
airports.drop(columns=["latitude", "longitude"])

# %%
# Selektion der Staaten mit den meisten Flughäfen
airports.state.value_counts().nlargest(5)

# %%
# `apply` führt eine Funktion entlang einer Achse aus
# und wird typischerweise zur Aggregation verwendet.
airports[["longitude", "latitude"]].apply(np.mean)

# %%
# Ersetzen von Werten in einer Series
airports.country.replace("USA", "United States").value_counts()

# %%
# Mapping von Werten in einer Series
airports.country.map({"USA": "United States"}).value_counts(dropna=False)

# %%
# `map` ersetzt `applymap` bei DataFrames.
airports[["name", "city"]].fillna("").map(str.upper)

# %% [markdown]
# ## Aufgaben
#
# 1. Welche Flughäfen liegen oberhalb des Breitengrads (latitude) 70 Grad N?
# 2. Welche Städte haben die meisten Flughäfen?
# 3. Welche Staaten haben Flughäfen, die unterhalb 40 Grad N liegen?
# 4. Wie viele Flughäfen liegen nicht in den USA?
# 5. Wie viele Flughäfen tragen "Airport" im Namen?
# 6. Welche Flughäfen sind verwechslungsgefährdet?
# 7. Gibt es Flughäfen in Texas, die "International" im Namen Tragen?
# 8. Entwickeln Sie eine eigene Frage zum Datensatz und analysieren Sie.

# %% [markdown]
# ## API-Übungen
#
# - Wie können in `.describe()` Perzentile gewählt werden?
# - Wie kann bei Aggregationen über Spalten bzw. Zeilen aggregiert werden?
# - Wie kann bei `.value_counts()` die ursprüngliche Sortierung erhalten werden?
