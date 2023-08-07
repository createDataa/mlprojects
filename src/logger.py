#logger is for the purpose that any exeecution that probabaly happen
#we should be able to log all those information the execution everything 
#in some ffiles so that  will be able to track if there is 
# error even the custom exception error we il try to 
#you know any custom  exception that basicall y comes will ty to log that 
# into the text file and we need to implemenet logger 


import logging 
import  os 
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)