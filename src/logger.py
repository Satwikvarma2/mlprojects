import logging
import os
from datetime import datetime

# Create the logs directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create a log file with the current date and time
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(log_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format=" [%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s "
)
if __name__=="__main__":
    logging.info("Logging has Started")