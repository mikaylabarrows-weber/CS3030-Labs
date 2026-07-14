# Code: Create system_logger.py in section5/task2/.

# Configuration: Set up a logger that saves to app.log and uses a professional format: 
    # [Timestamp] [Level] [Message].
    # Tip: Python defaults to ignoring INFO logs. You must explicitly set level=logging.INFO 
    # inside your logging.basicConfig() setup!

# Leveled Logic: Trigger at least three distinct levels in your script:
    # logging.info() for routine tasks (e.g., "Script started").
    # logging.warning() for non-critical issues (e.g., "Low disk space").
    # logging.error() for outright failures (e.g., "Database connection failed").

import logging

logging.basicConfig(
    filename = "app.log",
    filemode = "a",
    level=logging.INFO,
    format = "[%(asctime)s] [%(levelname)s] [%(message)s]",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

logging.info("Normal Operation - Script started.")
logging.warning("Potential Issue - Low Disk Space.")
logging.error("Failed Operation - Database connection failed.")