import logging
import os
from datetime import datetime


DG_FILE=f" ((datetime.now().strftime('%m-%d_XY_XH_XM_XS')).log"
logs_path = os.path.join(os.getcwd(), "logs", "LOG FILED")
os.makedirs (logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, "LOG FILE")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] X(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)    