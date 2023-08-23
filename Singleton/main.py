from typing import Any


class SingletonLogger(object):
    class __LoggerObject():
        def __init__(self,file_name: str) -> None:
            self.file_name = file_name
        def __str__(self) -> str:
            return "{0!r} {1}".format(self, self.file_name)
        def _write_log(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))
        def critical(self, msg):
            self._write_log("CRITICAL", msg)
        def error(self, msg):
            self._write_log("ERROR", msg)
        def warn(self, msg):
            self._write_log("WARN", msg)
        def info(self, msg):
            self._write_log("INFO", msg)
        def debug(self, msg):
            self._write_log("DEBUG", msg)
        
    instances: dict[str, __LoggerObject] = {}
    # This method is called when SingletonLogger is instanciated
    def __new__(cls, file_name, logger_name)->__LoggerObject:
        if not SingletonLogger.instances.get(logger_name):
            #Saves the instance of the object in the dict 'instantes'.
            SingletonLogger.instances[logger_name] = SingletonLogger.__LoggerObject(file_name)
            
        return SingletonLogger.instances[logger_name]
    def __getattribute__(self, __name: str) -> Any:
        return getattr(self.instance, __name)
    def __setattr__(self, __name: str, __value: Any) -> None:
        return setattr(self.instance, __name)