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
import numpy as np

np.array([1, 2, 3])

# %%
# Erstellen eines Arrays mit Werten von 0 bis 9,
# ähnlich wie mit `range(10)`
values = np.arange(10)

# %%
# Umformen des Arrays in eine 2x5-Matrix.
matrix = values.reshape(2, 5)
matrix.shape

# %%
# Mit -1 wird die Form des Arrays vervollständigt.
# Das Ergebnis ist dasselbe wie im oberen Beispiel.
matrix = values.reshape(2, -1)
matrix.shape

# %%
# Aggregationen werden auf dem gesamten Array durchgeführt.
matrix.mean()

# %%
# Mittelwert für jede Spalte
matrix.mean(axis=0)

# %%
# Mittelwert für jede Zeile
matrix.mean(axis=1)

# %%
# weitere Aggregationsfunktionen
matrix.sum()
matrix.max()
matrix.argmax()
matrix.std()

# %%
# Transponieren der Matrix
matrix.T

# %%
# Multiplikation der Matrix mit einem Skalar
matrix * 2

# %%
# Beim Broadcasting werden Arrays mit unterschiedlichen Formen kombiniert.
# Die erste Zeile der Matrix wird mit 2 multipliziert,
# die zweite Zeile mit 3.
matrix * np.array([2, 3]).reshape(2, 1)

# %%
# Auswählen der ersten Zeile
# Die beiden Schreibweisen sind äquivalent.
# Der Doppelpunkt dient hier als unbeschränkte Selektion.
matrix[0]
matrix[0, :]

# %%
# Auswählen der ersten Spalte
matrix[:, 0]

# %%
# Auswahl der zweiten Zeile, dritte und vierte Spalte
matrix[1, 2:4]

# %%
# Überschreiben der Werte
matrix[1, 2:4] = 0

# %%
# Erstellen eines 3D-Arrays mit den Werten von 0 bis 29
arr = np.arange(30).reshape(2, 5, 3)

# %%
# Aggregationen sind über alle Achsen möglich.
# Die resultierende Form hat die Achsen, die nicht aggregiert wurden.
arr.sum(axis=0)  # ergibt ein 5x3-Array
arr.sum(axis=1)  # ergibt ein 2x3-Array
arr.sum(axis=2)  # ergibt ein 2x5-Array
