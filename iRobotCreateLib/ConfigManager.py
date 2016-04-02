import json
from Errors import IRobotCreateError, ErrorCode

class ConfigManager:
    configuration = {}

    @staticmethod
    def __readConfig():
        try:
            # TODO: Change the follwoing to a relative path. Temporary fix.
            fp = open("/home/pi/workspace/PyCharmRemote/iRobotCreateLib/configuration/SerialConfig.json", "r")
            jsonString = fp.read()
            serialConfig = json.loads(jsonString)

            ConfigManager.configuration["SerialPortAddress"] = serialConfig["SerialPortAddress"]
            ConfigManager.configuration["BaudRate"] = serialConfig["BaudRate"]

            fp.close()
        # TEMPORARILY DISABLING THIS TILL WE UPGRADETP PYTHON 3
        # except FileNotFoundError as ex:
        #     raise IRobotCreateError(ErrorCode.ConfigurationFileMissing, ex.strerror)
        # except IOError as ex:
        #     if ex.errno == IOError.errno.EACCESS:
        #         raise IRobotCreateError(ErrorCode.ConfigFileError, "Configuration file not found: " + ex.strerror)
        #     if ex.errno == 13:
        #         raise IRobotCreateError(ErrorCode.ConfigFileError, "You don't have permission to access the configuration file" + ex.strerror)
        except ValueError as ex:
            raise IRobotCreateError(ErrorCode.ConfigFileCorrupted, "Configuration file may be corrupted.: " + ex.strerror)

    @staticmethod
    def getConfig(configName):
        ConfigManager.__readConfig()
        return ConfigManager.configuration[configName]


def main():
    print(ConfigManager.getConfig("SerialPortAddress"))
    print(ConfigManager.getConfig("BaudRate"))

if __name__ == "__main__":
    main()