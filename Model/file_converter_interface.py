from abc import ABC, abstractmethod


class FileToFrameConverterInterface(ABC):

    @abstractmethod
    def create_df(self, dataset_filepath: str):
        pass
