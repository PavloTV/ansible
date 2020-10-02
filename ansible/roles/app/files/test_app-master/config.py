import os
import logging

LOG_TO_DIR = os.environ.get("FLASK_LOG_TO_DIR")
LOG_LEVEL = logging.getLevelName(os.environ.get("FLASK_LOG_LEVEL", "INFO"))

CALCULATE_WAIT_TIME = float(os.environ.get("FLASK_CALCULATE_WAIT_TIME"))
BID_CREATION_WAIT_TIME = float(os.environ.get("FLASK_BID_CREATION_WAIT_TIME"))
