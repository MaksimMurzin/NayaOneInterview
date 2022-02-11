import pandas
import pandas as pd
from Logic.data_operator_interface import DataReaderInterface

# import Logic.DataOperatorInterface

'''
I implemented an interface so that you could swap how you would calculate methods in the future

I will be using snake_case for my methods and variables
methods will start with a verb like "get/create" etc, 
variables will start with a noun 


'''
# read the file into data frame (could be from a range of files
# perform opeations on the data once it is a dataframe


class DataOperator(DataReaderInterface):

    def __init__(self, data_frame: pd.DataFrame):
        self.df = data_frame

    def get_std_dev(self, column_name):
        return self.df[column_name].std()

    def get_mean_value(self, column_name: str):
        return self.df[column_name].mean()

    # I wasn't able to figure out how to get a list of these outliers for *all* the columns
    def get_zscores(self, column_name: str):
        return pandas.Series.abs(self.df[column_name] - self.df[column_name].mean())/self.df[column_name].std(ddof=0)

    def get_outliers(self, column_name: str):
        series = self.get_zscores(column_name)
        return list(series.loc[series > 3])

