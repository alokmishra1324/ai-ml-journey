import logging 

# ## Configur the basic logging settings
# logging.basicConfig(level=logging.DEBUG)

# ## Log messages

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

## configuring logging 

logging.basicConfig(
    filename ='app.log',
    filemode='w',
    level =logging.DEBUG ,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

