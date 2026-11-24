import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
file_handler = logging.FileHandler("app.log")

console.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)

logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
