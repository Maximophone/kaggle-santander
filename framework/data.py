import pandas as pd
from framework import settings

train = pd.DataFrame.from_csv(settings.locs.train_data)
test = pd.DataFrame.from_csv(settings.locs.test_data)

