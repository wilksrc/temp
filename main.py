import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info("this is a message")

# Add a console handler
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

df = pd.DataFrame({"col1": [1, 2, 3]})


logger.info("DataFrame length: %d", len(df))


print("end")
