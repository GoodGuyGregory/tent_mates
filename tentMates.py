import pandas as pd

# read the tents-preference list csv
tentPrefsDataFrame = pd.read_csv("tents-prefs.csv", header=None)

# convert to a new datastructure with just names
names = []
for name in tentPrefsDataFrame[0]:
    if name not in names:
        names.append(name)


# read the tent sizes list csv
tentSizesDataFrame = pd.read_csv("tents-sizes.csv", header=None)
# print(tentSizesDataFrame.head())

## learn to
