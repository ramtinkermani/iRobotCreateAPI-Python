#! /usr/bin/env python

import struct
import serial
import json
import time
import binascii

from Errors import IRobotCreateError, ErrorCode
from OpenInterface import OpCode, SensorPacket
from ConfigManager import ConfigManager

class IRobotCreate():
    def __init__(self):
        self.serialConnection = None
        self.serialPortAddress = ConfigManager.getConfig("SerialPortAddress")
        self.serialBaudRate = ConfigManager.getConfig("BaudRate")
        self.__connect()

    @property
    def SerialPort(self):
        return self.serialConnection.port

    @property
    def SerialBaudrate(self):
        return self.serialConnection.baudrate

    # Private Methods

    def __connect(self):
        try:
            self.serialConnection = serial.Serial(self.serialPortAddress, self.serialBaudRate)
            print("Connected to port {} with baudrate {}".format(self.serialConnection.port, self.serialConnection.baudrate))
        except serial.SerialException as ex:
            #raise IRobotCreateError(ErrorCode.SerialPortNotFound, ex.strerror)
            return ErrorCode.SerialPortNotFound
        else:
            return True

    def disconnect(self):
        self.serialConnection.close()

    def __sendCommand(self, cmdTuple):
        try:
            commandBytes = ""
            for i in cmdTuple:
                commandBytes += str(struct.pack("!B", i))
            self.serialConnection.write(str(commandBytes))
            print("Command: " + str(cmdTuple))
        except Exception as ex:
            print(str(ex))

    def __readResponse(self, numberOfBytes):
        a = self.serialConnection.read(numberOfBytes)
        #b = serial.Serial(self.serialPortAddress, self.serialBaudRate).read(5).decode("utf-8")
        #print(binascii.hexlify(a))
        res = ""
        for c in a:
            #res += " " + str(int(binascii.hexlify(c), 16))
            res += " " + str(int(binascii.hexlify(c), 16))

            #print(int(binascii.hexlify(c), 16))
        print(res)

    def readSensor(self):
        commandTuple = (OpCode.Input.Sensors, SensorPacket.Buttons)
        garbage = self.serialConnection.read_all()
        self.__sendCommand(commandTuple)
        while True:
            self.__readResponse(6)
            time.sleep(1)


    def __getBytes(self, decimalValue):
        if decimalValue >=0:
            lowByteHex = (hex(decimalValue)[-2:]).split('x')[1] if len(hex(decimalValue)[-2:].split('x')) == 2 else (hex(decimalValue)[-2:]).split('x')[0]
            highByteHex = hex(decimalValue)[:-2] if hex(decimalValue)[:-2] != '0x' else '0x0'

        else:
            twosComplementValue = hex(int(hex(abs(decimalValue) ^ 0xFFFF), 16)+1) # e.g. '0xFF38' for -200
            highByteHex = twosComplementValue[0:4]
            lowByteHex = '0x' + twosComplementValue[4:6]

        highByte = int(highByteHex, 16)
        lowByte = int(lowByteHex, 16)

        return highByte, lowByte


    # Public Native Methods

    def drive(self, rightWheelSpeed, leftWheelSpeed):
        if rightWheelSpeed > 500 or rightWheelSpeed < -500 or leftWheelSpeed > 500 or leftWheelSpeed < -500:
            raise IRobotCreateError(ErrorCode.ValueOutOfRange)
        try:
            speedRightValue = self.__getBytes(int(rightWheelSpeed))
            speedLeftValue = self.__getBytes(int(leftWheelSpeed))
            print(speedRightValue)
            print(speedLeftValue)
            commandTuple = (OpCode.Actuator.DriveDirect, speedRightValue[0], speedRightValue[1], speedLeftValue[0], speedLeftValue[1])
            self.__sendCommand(commandTuple)
        except Exception as ex:
            return str(ex)

    def start(self):
        # Start the Open Interface
        commandTuple = (OpCode.Operation.Start, )
        self.__sendCommand(commandTuple)

    def stop(self):
        # Stop the Open Interface
        commandTuple = (OpCode.Operation.Stop, )
        self.__sendCommand(commandTuple)

    def fullMode(self):
        commandTuple = (OpCode.Mode.Full, )
        self.__sendCommand(commandTuple)

    def safeMode(self):
        commandTuple = (OpCode.Mode.Safe, )
        self.__sendCommand(commandTuple)

    def powerOff(self):
        commandTuple = (OpCode.Operation.Power,)
        self.__sendCommand(commandTuple)

    def digitLedAscii(self, d3=32, d2=32, d1=32, d0=32): # 32 -> show nothing
        commandTuple = (OpCode.Display.DigitLEDsASCII, d3, d2, d1, d0)
        self.__sendCommand(commandTuple)

    def digitLEDsRaw(self, digitBits3, digitBits2, digitBits1, digitBits0):
        raise NotImplementedError
        #commandTuple = (OpCode.Display.DigitLEDsRaw, digitBits3, digitBits2, digitBits1, digitBits0)
        #self.__sendCommand(commandTuple)


    #Public Auxiliary High Level Methods

    # def drawSquare(self, sideLength):
    #     for i in range(4):
    #         self.drive(45, 45)
    #         time.sleep(sideLength)
    #         self.drive(100, 0)
    #         time.sleep(sideLength)

    def printMessage(self, msg, repeat=1, delay=0.5):
        if len(msg) <= 4:
            commandTuple = (OpCode.Display.DigitLEDsASCII,)
            for i in msg:
                commandTuple += (ord(i),)
            self.__sendCommand(commandTuple)
        else:
            msg = "    " + msg + "    "
            for i in range(repeat):
                displayValue = ""
                for i in range(len(msg) - 3):
                    displayValue = msg[i:i+4]
                    commandTuple = (OpCode.Display.DigitLEDsASCII,)
                    for i in displayValue:
                        commandTuple += (ord(i),)
                    self.__sendCommand(commandTuple)
                    time.sleep(delay)

    def CleanSpot(self):
        commandTuple = (OpCode.CleaningMode.Spot)
        self.__sendCommand(commandTuple)


def main():
    try:

        myRobot = IRobotCreate()
        myRobot.start()
        myRobot.fullMode()


        # while True:
        #myRobot.readSensor()
        #time.sleep(10)

        #myRobot.digitLedAscii(54, 55, 56, 57)           ### 3<--- HERE
        #time.sleep(3)
        #myRobot.printMessage("Hello World", 2, .2)
        #myRobot.printMessage("my name is Ramtin")
        #time.sleep(3)
        #myRobot.digitLedAscii(48, 49, 50, 51)

        # myRobot.drawSquare(3)

        # time.sleep(2)
        myRobot.drive(30,30)
        time.sleep(2)
        myRobot.drive(0,0)
        # #myRobot.digitLedAscii(54, 55, 56, 57)           ### 3<--- HERE
        # time.sleep(2)
        # myRobot.drive(-30,-30)
        # time.sleep(2)
        # myRobot.drive(0,0)

        myRobot.stop()
        myRobot.powerOff()

        myRobot.disconnect()


    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    main()

# TODO:
# - Close Serial connection properly
# - Create Configuration Manager Class
# - Check mode changes for opcodes