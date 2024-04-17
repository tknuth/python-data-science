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
import altair as alt

# %%
pd.to_datetime(-10, unit="s")

# %%
pd.to_datetime("2023-10-10")

# %%
pd.Timestamp("2023-10-10")

# %%
pd.Timedelta("2d4h3m")

# %%
pd.Timedelta("2 days 1 hour")

# %%
pd.Timestamp("2024").is_leap_year

# %%
d = pd.Timestamp("2023-11-06")

# %%
offset = pd.Timedelta("3 days")

# %%
d.day_name()

# %%
d.month_name()

# %%
(d + offset).day_name()

# %%
df = data.seattle_weather()

# %%
df["month_number"] = df.date.dt.month
df["month_name"] = df.date.dt.month_name()
df["day_number"] = df.date.dt.day
df["year"] = df.date.dt.year

alt.Chart(df).mark_rect().encode(
    x="day_number:O",
    y="month_number:O",
    color="max(temp_max)"
)

# %%
# https://altair-viz.github.io/user_guide/transform/timeunit.html
alt.Chart(df).mark_rect().encode(
    x="date(date)",
    y="month(date)",
    color="max(temp_max)",
    row="year"
).configure_view(strokeWidth=0, step=20).properties(width=600, height=200)

# %%
# https://altair-viz.github.io/user_guide/transform/timeunit.html
alt.Chart(df).mark_bar().encode(
    x="yearmonth(date)",
    y="max(temp_max)",
    color="year(date):N"
).configure_view(strokeWidth=0, step=20).properties(width=600, height=200)
