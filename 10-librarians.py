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
import altair as alt
import pandas as pd
import numpy as np

# Daten von 538, CC-BY-4.0
# https://github.com/fivethirtyeight/data/tree/master
DATASET_URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/librarians/librarians-by-msa.csv"

# area_name
# tot_emp: total employees
# emp_prse: employment percent relative standard error
# loc_quotient: location quotient
# jobs_1000: librarians per 1000 people
df = pd.read_csv(DATASET_URL)
df = df.replace("**", np.nan)
df.iloc[:, 2:] = df.iloc[:, 2:].astype("float")
df.head()

# %%
dg = df.groupby("prim_state").tot_emp.sum().reset_index()

c = alt.Chart(dg.sort_values("tot_emp", ascending=False).head(10)).encode(
    alt.X("tot_emp").title("Personal").axis(grid=False).scale(domain=[0, 14000]),
    alt.Y("prim_state").title("Bundesstaat").sort("-x").axis(ticks=False, labels=False),
)

numbers = c.mark_text(xOffset=-5, align="right").encode(text="tot_emp")
bars = c.mark_bar(opacity=0.15, color="#2980b9")
states = c.mark_text(xOffset=5, fontStyle="bold", align="left").encode(
    text="prim_state"
)

chart = bars + numbers + states

(
    chart.configure_view(strokeWidth=0)
    .configure_scale(bandPaddingInner=0.3, bandPaddingOuter=0.5)
    .properties(height=300, width=500)
)

# %%
dg = df.groupby("prim_state")[["tot_emp", "jobs_1000"]].sum().reset_index()

dg["product"] = dg.tot_emp * dg.jobs_1000

c = alt.Chart(dg).encode(
    alt.X("tot_emp").title("Personal"),
    alt.Y("jobs_1000").title("Jobs pro 1000 Personen"),
)

circles = c.mark_circle(color="#2980b9")

text = c.mark_text(align="left", dx=5, dy=-5).encode(
    text="prim_state",
    opacity=alt.condition(
        alt.datum.product > dg["product"].mean(), alt.value(1), alt.value(0)
    ),
)

(circles + text).properties(width=500, height=500)

# %% [markdown]
# - Wie viele Bibliotheken werden aufgeführt?
# - Wie viele Menschen arbeiten insgesamt in Bibliotheken?
# - In welchen Regionen arbeiten die meisten Menschen in Bibliotheken?
# - Wie hoch ist der Anteil Bibliothekspersonal je Bundesstaat?
# - Welcher Bundesstaat hat die meisten Bibliotheken?
