import logging
logging.basicConfig(filename="test1.log",level=logging.INFO)
logging.info("Hello this is my first log file which i have created")
l=[1,2,3,4,5]
for i in l:
    if i==3:
        logging.info("This is working fine now")

logging.shutdown()
logging.info("Hello there")
logging.shutdown()