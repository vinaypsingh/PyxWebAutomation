# logging means -  capture details. which are useful while debugging
# and show the user details about execution of the program.

# warning to the users
# information to the users
# errors, critical errors users.

import logging

def test_logs():
    Logger= logging.getLogger(__name__)

    Logger.info("This is information log")
    Logger.warning("This is warning log")
    Logger.error("This is error log")
    Logger.critical("This is critical log")
