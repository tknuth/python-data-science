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
# - Aggregationen über verschiedene Achsen
# - Umbenennung von Indizes und Spalten
# - Verkettung von Aggregationen
# - Funktionen `.idxmax()` und `.idxmin()`
# - Aggregation über Gruppen mit `.groupby()`
# - boolesche Series für Aggregation

# %%
import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.randint(10, size=20).reshape(-1, 4)
df = pd.DataFrame(data, columns=list("abcd"))
df

# %%
# Die Spaltennamen lassen sich z.B. durch Angabe einer Liste mit neuen Namen ersetzen.
# Eine Alternative ist die Verwendung der Funktion `.rename()`
df.columns = ["e", "f", "g", "h"]
df

# %%
# Der Index kann ebenso wie die Spaltennamen überschrieben werden.
# Auch hier kann alternativ die Funktion `.rename()` eingesetzt werden.
df.index = ["v", "w", "x", "y", "z"]
df

# %%
# Aggregationsfunktionen auf Series (Spalten) geben ein Skalar zurück.
df.e.mean()

# %%
# Aggregationsfunktionen auf DataFrames (Tabellen) geben eine Series zurück.
df.mean()

# %%
# Die Richtung der Aggregation kann verändert werden.
df.mean(axis=1)

# %%
# Kleinstes Spaltenmaximum
df.max().min()

# %%
# Größter Zeilenmittelwert
df.mean(axis=1).max()

# %%
# In welcher Zeile befindet sich der maximale Wert?
df.idxmax()

# %%
# In welcher Spalte befindet sich der maximale Wert?
df.idxmax(axis=1)

# %%
# Wir erstellen Gruppen
df["group"] = list("a" * 2 + "b" * 3)
df

# %%
# Mittelwert pro Gruppe
df.groupby("group").mean()

# %%
# Zeilen mit Maximalwerten pro Gruppe
df.groupby("group").idxmax()

# %%
# Verschiedene Aggregationen für alle Spalten
df.groupby("group").agg(["mean", "std", "max", "min"])

# %%
# Zuordnung von Aggregationen zu bestimmten Spalten
df.groupby("group").agg({"e": "mean", "f": "std", "g": "max", "h": "min"})

# %%
# Wir fügen Klassen hinzu.
df["class"] = [1, 2, 3, 3, 4]
df

# %%
# Verschachtelte Gruppierung
df.groupby(["group", "class"]).mean()

# %%
# Die Gruppen werden können als Spalten erhalten bleiben.
df.groupby("group", as_index=False).mean()

# %%
# Gruppierung ist auch mithilfe einer booleschen Series möglich.
df.groupby(df["class"] > 2).mean(numeric_only=True)

# %%
# Auswahl von Spalten vor der Aggregation
df.groupby(df["class"] > 2)[["e", "f", "g", "h"]].mean()

# %%
# Zur Gruppierung kann auch eine Funktion angegeben werden.
# Diese erhält den Index als Argument und gibt den Gruppennamen zurück.
df.reset_index(drop=True).groupby(lambda x: x % 2)[["e", "f", "g", "h"]].mean()
