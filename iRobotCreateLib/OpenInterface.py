'''
Based on the iRobot Roomba/Create Open Interface (OI) Specification
https://www.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf
'''

# TODO: The OpCode class's subclasses make more sense be implemented as Enums provided we upgrade to Python 3.4

class OpCode():

    # Operation Commands
    class Operation():
        Start = 128
        Reset = 7
        Stop = 173
        Power = 133
        Baud = 129

    # Mode Commands
    class Mode():
        Safe = 131
        Full = 132
        Passive = ""

    # Cleaning Modes
    class CleaningMode():
        Clean = 135
        Max = 136
        Spot = 134
        SeekDock = 143

    # Date and Time
    class DateTime():
        Schedule = ""
        SetDayTime = ""

    # Actuator Commands
    class Actuator():
        Drive = 137
        DriveDirect = 145
        DrivePWM = 146
        Motors = 138
        PWMMotors = 144

    # Display
    class Display():
        LEDs = 139
        SchedulingLEDs = 162
        DigitLEDsRaw = 163
        DigitLEDsASCII = 164

    # Sound and Music
    class Sound():
        Sound = 140
        Play = 141

    # Input Commands
    class Input():
        Sensors = 142
        QueryList = 149
        Stream = 148
        PauseResumeStream = 150

# Sensor packet IDs used in Input Commands
class SensorPacket():
    BumpsAndWheelDrops = 7
    Wall = 8
    CliffLeft = 9
    CliffFrontLeft = 10
    CliffFrontRight = 11
    CliffRight = 12
    VirtualWall = 13

    WheelOvercurrents = 14

    DirtDetect = 15
    UnusedByte = 16

    InfraredCharacterOmni = 17
    InfraredCharacterLeft = 52
    InfraredCharacterRight = 53

    Buttons = 18

    # Encoder values
    Distance = 19
    Angle = 20

    # Electronics
    ChargingState = 21
    Voltage = 22
    Current = 23
    Temperature = 24
    BatteryCharge = 25

    WallSignal = 27
    CliffLeftSignal = 28
    CliffFrontLeftSignal = 29
    CliffFrontRightSignal = 30
    CliffRightSignal = 31

    #Unused = 32, 33

    ChargingSourcesAvailable = 34
    OIMode = 35

    # class OIModeValue():
    #     Off = 0
    #     Passive = 1
    #     Safe = 2
    #     Full = 3

    SongNumber  = 36
    SongPlaying = 37

    NumberOfStreamPackets = 38

    RequestedVelocity = 39
    RequestedRadius = 40
    RequestedRightVelocity = 41
    RequestedLeftVelocity = 42
    LeftEncoderCounts = 43
    RightEncoderCounts = 44

    # Bumper
    LightBumper = 45
    LightBumpLeftSignal = 46
    LightBumpFrontLeftSignal = 47
    LightBumpCenterLeftSignal = 48
    LightBumpCenterRightSignal = 49
    LightBumpFrontRightSignal = 50
    LightBumpRightSignal = 51

    LeftMotorCurrent = 54
    RightMotorCurrent = 55
    MainBrushMotorCurrent = 56
    SideBrushMotorCurrent = 57
    Stasis = 58





















