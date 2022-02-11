import pandas as pd
from Model.file_converter_interface import FileToFrameConverterInterface


'''
This class will handle the way we read data, in the future we may want to create from other files or even apis
I made this from an interface to show my skills but I didn't want to go too crazy with it 
'''


class FileToFrameConverter(FileToFrameConverterInterface):

    def __init__(self, dataset_filepath : str):
        self.data_frame = dataset_filepath

    def create_df(self):
        if self.data_frame.endswith('.csv'):
            return pd.read_csv(self.data_frame)

    # seeing as we only accept a csv file format for now I am going to leave this as is
        print("Wrong file format used")
