from settings import settings
import pandas as pd
import numpy as np

def find_dependent_columns(df, tol=1e-5):
	A = np.array(df)
	Q,R = np.linalg.qr(A)
	where = np.abs(R.diagonal()) <= tol
	return df.columns[where]

def find_constant_columns(df):
	return df.columns[df.std()==0.]

def find_duplicate_columns(df):
	pass

class DataFactory(object):
	def __init__(self):
		self._clean_function = None

	def gen_clean(self,df_train):
		"""Here we put the code for the cleaning function. The function is generated from the train set
		and reused on the test set."""

		constant_columns = find_constant_columns(df_train)
		# duplicate_columns = find_duplicate_columns(df_train)
		dependent_columns = find_dependent_columns(df_train)

		def clean_df(df):
			columns_to_keep = [col for col in df.columns if col not in constant_columns|dependent_columns]
			return df[columns_to_keep].copy()

		return clean_df


	def clean(self,df):
		if self._clean_function is None:
			self._clean_function = self.gen_clean(df)
		return self._clean_function(df)

	def from_url(self,url):
		raw = pd.read_csv(url,index_col=0)
		clean = self.clean(raw)
		return clean,raw

_DF = DataFactory()
training, training_raw = _DF.from_url(settings.locs.train_data)
test, test_raw = _DF.from_url(settings.locs.test_data)

X = training.iloc[:,:-1].values
y = training.TARGET.values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)