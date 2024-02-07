#!/usr/bin/env python
# coding: utf-8
# %%
import numpy as np
import pandas as pd
import altair as alt

np.random.seed(19)

n = 50

a = (np.random.randn(n) + 7.8).reshape(-1, 1)
b = (np.random.randn(n) + 8.5).reshape(-1, 1)

c = np.concatenate([a, b], axis=1)

df = pd.DataFrame(c, columns=["A", "B"])
df.head()


# %%
dg = df.melt(value_vars=["A", "B"], var_name="Gruppe", value_name="Wert")
dg.head()


# %%
domain = [3, 11]
width_small = 100

stripplot = (
    alt.Chart(dg)
    .mark_circle()
    .encode(
        x=alt.X("Gruppe:N", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("Wert:Q", scale=alt.Scale(domain=domain)),
        color="Gruppe:N"
    ).properties(width=width_small)
)

boxplot = (
    alt.Chart(dg)
    .mark_boxplot()
    .encode(
        x=alt.X("Gruppe:N", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("Wert:Q", scale=alt.Scale(domain=domain), title=None),
        color="Gruppe:N"
    ).properties(width=width_small)
)

histogram = (
    alt.Chart(dg)
    .mark_bar()
    .encode(
        x=alt.X("Wert:Q", title="Wert").bin(maxbins=20),
        y=alt.Y("count()", title="Anzahl"),
        color=alt.Color("Gruppe:N").legend(None)
    )
    
)
stripplot | boxplot | histogram

