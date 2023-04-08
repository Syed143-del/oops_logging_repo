import logging
logging.basicConfig(filename="testing3.log",level=logging.INFO,format='%(levelname)s,%(message)s,%(asctime)s,%(level)s')

def divide(a,b) :
    logging.info("The numbers entered by the user is %s and %s", a,b)
    return a/b

print(divide(10,20))
