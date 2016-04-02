class IRobotCreateError(Exception):
    def __init__(self, errorCode = 0, errorMsg = ""):
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        # self.super()

class ErrorCode():
    SerialPortNotFound = 1
    SerialConnectionTimeout = 2

    ConfigFileError = 3
    ConfigFileCorrupted = 4

    ValueOutOfRange = 5



