import logging

logger = logging.getLogger("catalog")
logger.setLevel(logging.INFO)

file = logging.FileHandler("app.log")
fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file.setFormatter(fmt)

logger.addHandler(file)
