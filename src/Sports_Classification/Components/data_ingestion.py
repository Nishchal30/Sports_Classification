import os, zipfile
from src.Sports_Classification.logger import logging
from src.Sports_Classification.exception import CustomException
import urllib.request as request
from src.Sports_Classification.utils.utils import *
from src.Sports_Classification.Config.configuration import DataIngestionConfig


class DataIngestion:

    logging.info("Data ingestion will start here")

    def __init__(self, config : DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        The function will download the files from the given url

        source_path (url) : The url for the file to be downloaded
        local_data_file (path) : The path where the file should be downloaded

        """
        try:

            if not (os.path.exists(self.config['local_data_file'])):
                filename, headers = request.urlretrieve(
                    url=self.config['source_path'],
                    filename=self.config['local_data_file']
                )

                logging.info(f"Download the {filename} with the info: \n{headers}")
        
            else:
                logging.info(f"the file already exists of size: {get_size(Path(self.config['local_data_file']))}")
        
        except Exception as e:
            logging.info("Error occured in download_file method in data ingestion file")
            raise CustomException(e, sys)

    
    def extract_zip_file(self):
        """
        The function unzip the downloaded zip file

        unzip_dir (path) : The path where the zip file should be unzipped
        """
        try:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
                zip_file.extractall(unzip_dir)

            logging.info(f"Zip file extracted successfully at {unzip_dir}")
        
        except Exception as e:
            logging.info("Error occured in extract zip file method in data ingestion file")
            raise CustomException(e, sys)

        