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
# Daten von https://survey.stackoverflow.co
import pandas as pd

pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", None)

df = pd.read_csv("survey_results_public.csv")
sc = pd.read_csv("survey_results_schema.csv").set_index("qname")

# %%
# Wie viel Programmiererfahrung haben Teilnehmer:innen nach Alterssegment in Jahren?
# Interpretieren Sie die Ergebnisse. Finden Sie inkonsistente Werte?
df["YearsCodeNumeric"] = pd.to_numeric(df.YearsCode, errors="coerce")
df.groupby("Age").YearsCodeNumeric.describe()

# %%
# Welcher Anteil der Teilnehmer:innen arbeitet mit Python?
df.LanguageHaveWorkedWith.str.contains("Python").value_counts(
    dropna=False, normalize=True
)

# %%
# Wie beliebt sind die verschiedenen Programmiersprachen unter den Teilnehmer:innen?
df.LanguageHaveWorkedWith.fillna("n/a").str.split(";").explode().value_counts() / len(
    df
)

# %%
# Welcher Anteil der Teilnehmer:innen der Umfrage hat bereits mit ChatGPT gearbeitet?
df.AISearchDevHaveWorkedWith.str.contains("ChatGPT").value_counts(
    dropna=False, normalize=True
)

# Mit wie vielen Programmiersprachen haben die Teilnehmer:innen bereits gearbeitet?
# %%
df.LanguageHaveWorkedWith.str.get_dummies(";").sum(axis=1).value_counts(
    normalize=True
).sort_index()
