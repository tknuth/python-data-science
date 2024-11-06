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

# https://github.com/fivethirtyeight/data/blob/master/bad-drivers/bad-drivers.csv
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/bad-drivers/bad-drivers.csv")

# %%
df.columns = [
    "state",
    "fatalities",
    "speeding",
    "alcohol",
    "not_distracted",
    "no_prev_accidents",
    "insurance",
    "losses",
]

# %%
df.head()

# %% [markdown]
# ## Aufgaben
#
# 1. Benennen Sie die Spalten mit passenden Kurznamen.
# 2. Legen Sie Spalten an, sodass alle Aussagen positiv formuliert werden können (z.B. `not_distracted` zu `distracted`).
# 3. In welchen Staaten ist der Anteil der tödlichen Unfälle überdurchschnittlich hoch?
# 4. In welchen Staaten ist der Anteil der tödlichen Unfälle durch überhöhte Geschwindigkeit besonders hoch?
# 5. Wie viele Fahrerinnen und Fahrer waren in tödliche Unfälle mit überhöhter Geschwindigkeit involviert?
# 6. Welche ist pro Staat die größte Ursache von tödlichen Unfällen (Geschwindigkeit, Alkohol, Ablenkung)?
