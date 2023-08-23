from main import SingletonLogger

first_logger = SingletonLogger("first_logger.txt","first logger")

first_logger.critical("This is a message")

print(first_logger)

second_logger = SingletonLogger("second_logger.txt", "second logger")

second_logger.error("Thiss is other message")
print(first_logger, SingletonLogger.instances["first logger"])
print(second_logger, SingletonLogger.instances["second logger"])
print(SingletonLogger.instances)