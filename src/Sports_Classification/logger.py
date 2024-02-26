import os, sys
import logging
from datetime import datetime as dt

logging_str = "[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s"
log_filename = f"{dt.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
log_dir = "logs"
log_filepath = os.path.join(log_dir, log_filename)

os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(level=logging.INFO,
                    format=logging_str,
                    filename=log_filepath
)
