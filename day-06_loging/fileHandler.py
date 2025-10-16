import logging
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger("rotating_logger")
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler(
    "app.log", 
    maxBytes=200,          # rotate every 200 bytes
    backupCount=3          # keep 3 old files
)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler
logger.addHandler(handler)

# Generate some logs
for i in range(30):
    logger.info(f"Log message {i}")
