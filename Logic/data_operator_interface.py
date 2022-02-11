from abc import ABC, abstractmethod


class DataReaderInterface(ABC):

    @abstractmethod
    def get_std_dev(self, column_name: str):
        pass

    @abstractmethod
    def get_mean_value(self, column_name: str):
        pass

    @abstractmethod
    def get_outliers(self,):
        pass

