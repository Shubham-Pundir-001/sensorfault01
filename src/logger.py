import logging
import os ## it provide method to read and write in file
from datetime import datetime



LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True) 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    file_name=LOG_FILE,
    format="[%(asctime)s]%(lineno)d %d(name)s -%(level_name)s -%(message)s",
    level=logging.INFO
)