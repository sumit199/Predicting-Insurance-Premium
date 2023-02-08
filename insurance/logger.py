import logging
import os
from datetime import datetime 

#log file name
Log_File_Name = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log file directory
Log_File_Dir = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(Log_File_Dir, exist_ok=True)

#log file path
Log_File_Path = os.path.join(Log_File_Dir,Log_File_Name)

logging.basicConfig(
    filename=Log_File_Path,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)