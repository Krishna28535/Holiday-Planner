from logger.logger import setup_logger
logger = setup_logger()

a=int(input("Enter number: "))
logger.info(f"Input value is {a}")
b=int(input("Enter number: "))
logger.info(f"Input value is {b}")
print(a/b)
