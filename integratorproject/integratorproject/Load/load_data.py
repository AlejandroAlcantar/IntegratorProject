
import pandas as pd
from utilities.custom_loggin import CustomLogging

logger = CustomLogging()
logger = logger.CreateLogger(file_name='load_data.log')


class DataRetriever:
    """
    A class for retrieving data from a given URL and processing it for further analysis.

    Parameters:
        url (str): The URL from which the data will be loaded.

    Attributes:
        url (str): The URL from which the data will be loaded.

    Example usage:
    ```
    URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    data_retriever = DataRetriever(URL)
    result = data_retriever.retrieve_data()
    print(result)
    ```
    """

    DROP_COLS = ['name', 'ticket', 'boat', 'body', 'home.dest']
    # DATASETS_DIR = './data/'  # Directory where data will be saved.
    RETRIEVED_DATA = 'retrieved_data.csv'  # File name for the retrieved data.

    def __init__(self, data_path):
        self.DATASETS_DIR = data_path

    def retrieve_data(self):
        """
        Retrieves data from the specified URL, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """
        # Loading data from specific URL
        data = pd.read_csv(self.DATASETS_DIR)

        # Drop irrelevant columns
        # data.drop(self.DROP_COLS, axis=1, inplace=True)

        data = data.fillna(data.mean())
        logger.info("data was loaded")
        return data

# Usage Example:
# URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
# data_retriever = DataRetriever(URL)
# result = data_retriever.retrieve_data()
# print(result)
