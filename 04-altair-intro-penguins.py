#!/usr/bin/env python
# coding: utf-8
# %%
import pandas as pd
import altair as alt
import seaborn as sns

# https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv
# https://github.com/allisonhorst/palmerpenguins
df = sns.load_dataset("penguins")


# %%
alt.Chart(df).mark_point()


# %%
alt.Chart(df).mark_point().encode(x="bill_length_mm")


# %%
alt.Chart(df).mark_point().encode(x="bill_length_mm", y="bill_depth_mm")


# %%
(
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("bill_length_mm", scale=alt.Scale(domain=[30, 60])),
        y=alt.Y("bill_depth_mm", scale=alt.Scale(domain=[12, 22]))
    )
)


# %%
xscale = alt.Scale(domain=[30, 60])
yscale = alt.Scale(domain=[12, 22])

(
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("bill_length_mm", scale=xscale),
        y=alt.Y("bill_depth_mm", scale=yscale),
        color=alt.Color("species").legend(direction="horizontal", orient="bottom")
    )
    .properties(width=200)
)


# %%
(
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("bill_length_mm", scale=xscale),
        y=alt.Y("bill_depth_mm", scale=yscale),
        color=alt.Color("species").legend(direction="horizontal", orient="bottom"),
        column=alt.Column("island")
    )
    .properties(width=200)
)


# %%
# https://altair-viz.github.io/user_guide/encodings/index.html#aggregation-functions
(
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("body_mass_g").bin(maxbins=30),
        y="count()",
    )
)


# %%
(
    alt.Chart(df)
    .mark_bar()
    .encode(
        y=alt.X("body_mass_g").bin(maxbins=30),
        x=alt.Y("count()"),
        color=alt.Color("sex"),
        column="sex"
    )
).properties(height=300, width=100)


# %%
(
    alt.Chart(df)
    .mark_boxplot()
    .encode(
        x="body_mass_g"
    )
)


# %%
(
    alt.Chart(df)
    .mark_boxplot()
    .encode(
        x="body_mass_g",
        y="species",
        color="species",
        row="island"
    )
)


# %%
a = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("body_mass_g").bin(maxbins=30),
        y="count()",
    )
) 
b = (
    alt.Chart(df)
    .mark_boxplot()
    .encode(
        x="body_mass_g"
    )
)

a & b


# %%
xscale = alt.Scale(domain=(2500, 6500))

a = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("body_mass_g").bin(maxbins=30, extent=xscale.domain),
        y="count()",
    )
)
b = (
    alt.Chart(df)
    .mark_boxplot()
    .encode(
        x=alt.X("body_mass_g").scale(xscale),
        y="species"
    )
)

a & b


# %%
yscale1 = alt.Scale(domain=[12, 22])
xscale1 = alt.Scale(domain=[30, 60])
yscale2 = alt.Scale(domain=[160, 240])
xscale2 = alt.Scale(domain=[2000, 6500])
bin_domain = [0, 60]

brush = alt.selection_interval(encodings=["x", "y"])

a = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("bill_length_mm").scale(xscale1),
        y=alt.Y("bill_depth_mm").scale(yscale1),
        color=alt.condition(brush, "species", alt.value("grey")),
        shape="island"
    )
    .add_params(brush)
)

b = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("count()").scale(domain=bin_domain),
        y=alt.Y("bill_depth_mm", title=None).bin(maxbins=30, extent=yscale1.domain),
        color="species"
    )
    .properties(
        width=50
    )
    .transform_filter(brush)
)

c = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("body_mass_g").scale(xscale2),
        y=alt.Y("flipper_length_mm").scale(yscale2),
        color=alt.condition(brush, "species", alt.value("grey")),
        shape="island"
    )
    .add_params(brush)
)

d = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("count()").scale(domain=bin_domain),
        y=alt.Y("flipper_length_mm", title=None).bin(maxbins=30, extent=yscale2.domain),
        color="species"
    )
    .transform_filter(brush)
    .properties(
        width=50
    )
)

e = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        y=alt.Y("count()").scale(domain=bin_domain),
        x=alt.X("bill_length_mm", title=None).bin(maxbins=30, extent=xscale1.domain),
        color="species"
    )
    .transform_filter(brush)
    .properties(
        height=50
    )
)

f = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        y=alt.Y("count()").scale(domain=bin_domain),
        x=alt.X("body_mass_g", title=None).bin(maxbins=30, extent=xscale2.domain),
        color="species"
    )
    .transform_filter(brush)
    .properties(
        height=50
    )
)

e & (a | b) | f & (c | d)


# %% [markdown]
# - Laden Sie aus `vega_datasets` den Datensatz `data.cars()`.
# - Erstellen Sie einen Scatter-Plot und zeigen Sie Horsepower, Miles_per_Gallon und Origin an.
# - Kodieren Sie die Farbe mit `Cylinders:Q`, `Cylinders:N` und `Cylinders:O`. Was passiert?
# - Erstellen Sie ein Balkendiagramm mit Horsepower auf der y-Achse und Year auf der x-Achse.
# - Was passiert, wenn Sie im vorherigen Chart Year durch Year:O ersetzen?
# - Erstellen Sie zwei Charts und stellen diese mittels | nebeneinander oder mittels & untereinander dar.
