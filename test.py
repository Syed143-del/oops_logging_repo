import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("This is my first logging file")
l=[1,2,3,4,5,6,7,8]
for i in l:
    if i==4:
        logging.info(l)
        logging.critical("We have stored what you gave please check once and then proceed")
        logging.info("So logging is nothing but at the end of the day we are just trying to store the messge ")

logging.shutdown()