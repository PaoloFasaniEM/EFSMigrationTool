# utils/flag_converter.py

from enum import IntEnum


class EfsPanelFlag(IntEnum):
    NoneFlag                    = 0
    YellowFlag                  = 1
    DoubleYellowFlag            = 2
    YellowRedFlag               = 3
    BlueFlag                    = 4
    RedFlag                     = 5
    WhiteFlag                   = 6
    SCFlag                      = 7
    BlackFlag                   = 8
    GreenFlag                   = 9
    ChequeredFlag               = 10
    BlackOrangeFlag             = 11
    BlackWhiteFlag              = 12
    UndefinedFlag               = 13
    CustomFlag                  = 14
    MessageFlag                 = 15
    VSCFlag                     = 16
    VSCEndingFlag               = 17
    CommError                   = 18
    Code60Flag                  = 19
    SlowDownZoneNext            = 20
    SlowDownZone                = 21
    SlowDownZoneEnd             = 22
    CustomLogo                  = 23
    GoToPitFlag                 = 24
    FullCourseYellowFlag        = 25
    FiaRainFlag                 = 26
    FimRainFlag                 = 27
    FimRainSlipperyFlag         = 28
    FimPushFlag                 = 29
    FimChequeredFlag            = 30
    FullCourseYellowEndingFlag  = 31
    Clock                       = 32
    CountdownStart              = 33
    Countdown                   = 34
    CountdownEnd                = 35
    LastLap                     = 36
    LapNumber                   = 37
    CountryFlag                 = 38
    StandingStartFlag           = 39
    RollingStartFlag            = 40
    RoadClosedSign              = 41
    TurnLeftSign                = 42
    TurnRightSign               = 43
    GoLeftSign                  = 44
    GoRightSign                 = 45
    GoAheadSign                 = 46
    BlueYellowBandFlag          = 47
    BlackWhiteDiagonalCrossFlag = 48
    PitlaneClosedFlag           = 49
    BlackWhiteCrossFlag         = 50
    SafetyVehicleSign           = 51
    ElapsedTime                 = 52
    PitRedFlag                  = 53
    StopSign                    = 54
    HoldSign                    = 55
    GoSign                      = 56
    FimBikeChangeAllowed        = 57
    FimLongLap                  = 58
    FimLongLapx2                = 59
    DriveThrough                = 60
    RideThrough                 = 61
    ChangePosition              = 62
    Warning                     = 63
    Equipment                   = 64
    TimePenalty                 = 65
    PanelIdentifier             = 66
    InPit                       = 67
    Loudness                    = 68
    YellowSlipperyFlag          = 69
    CustomSign                  = 70
    SCPreparePassAround         = 71
    SCPassAround                = 72
    StopAndGo                   = 73
    Behaviour                   = 74


class CircuitPanelConfigurationFlag(IntEnum):
    NoneFlag                = 0
    Green                   = 1
    White                   = 2
    SlowDownZoneNext        = 3
    SlowDownZone            = 4
    SlowDownZoneEnd         = 5
    FimRain                 = 6
    FimRainSlippery         = 7
    YellowRed               = 8
    YellowSlippery          = 9
    Yellow                  = 10
    DoubleYellow            = 11
    Red                     = 12
    SC                      = 13
    VSC                     = 14
    VSCEnding               = 15
    FCY                     = 16
    FCYEnding               = 17
    Code60                  = 18
    StandingStart           = 19
    RollingStart            = 20
    Blue                    = 21
    Black                   = 22
    BlackOrange             = 23
    BlackWhite              = 24
    Chequered               = 25
    FimChequered            = 26
    FiaRain                 = 27
    FimPush                 = 28
    GoToPit                 = 29
    RoadClosed              = 30
    TurnLeft                = 31
    TurnRight               = 32
    GoLeft                  = 33
    GoRight                 = 34
    GoAhead                 = 35
    BlueYellowBand          = 36
    BlackWhiteDiagonalCross = 37
    PitlaneClosed           = 38
    BlackWhiteCross         = 39
    SafetyVehicle           = 40
    PitRed                  = 41
    Stop                    = 42
    Hold                    = 43
    Go                      = 44
    CustomSign              = 45
    PanelIdentifier         = 46
    SCPreparePassAround     = 47
    SCPassAround            = 48
    Undefined               = 49

class SpeedLimitFlag(IntEnum):
    NoneFlag           = 0
    GreenFlag          = 1
    WhiteFlag          = 2
    YellowFlag         = 3
    DoubleYellowFlag   = 4
    BlueFlag           = 5
    YellowRedFlag      = 6
    SCOutFlag          = 7
    SCInFlag           = 8
    RedFlag            = 9
    BlackFlag          = 10
    ChequeredFlag      = 11
    BlackWhiteFlag     = 12
    BlackOrangeFlag    = 13
    VSCFlag            = 14
    VSCEndingFlag      = 15
    FCYFlag            = 16
    FCYEndingFlag      = 17
    Code60Flag         = 18
    SlowZoneFlag       = 19
    Code60EndingFlag   = 20
    YellowSlippery     = 21
    Rain               = 22
    YellowSpeedOffender = 23
    GoToPit            = 24
    LongLap            = 25
    ChangePosition     = 26
    LongLapx2          = 27
    DriveThrough       = 28
    RideThrough        = 29
    Warning            = 30
    Equipment          = 31
    TimePenalty        = 32
    Loudness           = 33
    InPit              = 34
    StopAndGo          = 35
    Behaviour          = 36

class FlagPageParams(IntEnum):
    NoneFlag       = 0
    Green          = 1
    Red            = 2
    Yellow         = 3
    White          = 4
    Black          = 5
    BlackOrange    = 6
    BlackWhite     = 7
    Chequered      = 8
    Code60         = 9
    ChequeredBlue  = 10
    Country        = 11
    LongLap        = 12
    LongLapx2      = 13
    DriveThrough   = 14
    RideThrough    = 15
    ChangePosition = 16
    TimePenalty    = 17
    Warning        = 18
    Equipment      = 19
    InPit          = 20
    Loudness       = 21
    StopAndGo      = 22
    Behaviour      = 23

_SPEED_LIMIT_FLAG_MAP: dict[SpeedLimitFlag, CircuitPanelConfigurationFlag] = {
    SpeedLimitFlag.NoneFlag:            CircuitPanelConfigurationFlag.NoneFlag,
    SpeedLimitFlag.GreenFlag:           CircuitPanelConfigurationFlag.Green,
    SpeedLimitFlag.WhiteFlag:           CircuitPanelConfigurationFlag.White,
    SpeedLimitFlag.YellowFlag:          CircuitPanelConfigurationFlag.Yellow,
    SpeedLimitFlag.DoubleYellowFlag:    CircuitPanelConfigurationFlag.DoubleYellow,
    SpeedLimitFlag.BlueFlag:            CircuitPanelConfigurationFlag.Blue,
    SpeedLimitFlag.YellowRedFlag:       CircuitPanelConfigurationFlag.YellowRed,
    SpeedLimitFlag.SCOutFlag:           CircuitPanelConfigurationFlag.SC,
    SpeedLimitFlag.SCInFlag:            CircuitPanelConfigurationFlag.SC,
    SpeedLimitFlag.RedFlag:             CircuitPanelConfigurationFlag.Red,
    SpeedLimitFlag.BlackFlag:           CircuitPanelConfigurationFlag.Black,
    SpeedLimitFlag.ChequeredFlag:       CircuitPanelConfigurationFlag.Chequered,
    SpeedLimitFlag.BlackWhiteFlag:      CircuitPanelConfigurationFlag.BlackWhite,
    SpeedLimitFlag.BlackOrangeFlag:     CircuitPanelConfigurationFlag.BlackOrange,
    SpeedLimitFlag.VSCFlag:             CircuitPanelConfigurationFlag.VSC,
    SpeedLimitFlag.VSCEndingFlag:       CircuitPanelConfigurationFlag.VSCEnding,
    SpeedLimitFlag.FCYFlag:             CircuitPanelConfigurationFlag.FCY,
    SpeedLimitFlag.FCYEndingFlag:       CircuitPanelConfigurationFlag.FCYEnding,
    SpeedLimitFlag.Code60Flag:          CircuitPanelConfigurationFlag.Code60,
    SpeedLimitFlag.SlowZoneFlag:        CircuitPanelConfigurationFlag.SlowDownZone,
    SpeedLimitFlag.YellowSlippery:      CircuitPanelConfigurationFlag.YellowSlippery,
    SpeedLimitFlag.GoToPit:             CircuitPanelConfigurationFlag.GoToPit,
}


_FLAG_MAP: dict[EfsPanelFlag, CircuitPanelConfigurationFlag] = {
    EfsPanelFlag.YellowFlag:                  CircuitPanelConfigurationFlag.Yellow,
    EfsPanelFlag.DoubleYellowFlag:            CircuitPanelConfigurationFlag.DoubleYellow,
    EfsPanelFlag.YellowRedFlag:               CircuitPanelConfigurationFlag.YellowRed,
    EfsPanelFlag.BlueFlag:                    CircuitPanelConfigurationFlag.Blue,
    EfsPanelFlag.RedFlag:                     CircuitPanelConfigurationFlag.Red,
    EfsPanelFlag.WhiteFlag:                   CircuitPanelConfigurationFlag.White,
    EfsPanelFlag.SCFlag:                      CircuitPanelConfigurationFlag.SC,
    EfsPanelFlag.BlackFlag:                   CircuitPanelConfigurationFlag.Black,
    EfsPanelFlag.GreenFlag:                   CircuitPanelConfigurationFlag.Green,
    EfsPanelFlag.ChequeredFlag:               CircuitPanelConfigurationFlag.Chequered,
    EfsPanelFlag.BlackOrangeFlag:             CircuitPanelConfigurationFlag.BlackOrange,
    EfsPanelFlag.BlackWhiteFlag:              CircuitPanelConfigurationFlag.BlackWhite,
    EfsPanelFlag.UndefinedFlag:               CircuitPanelConfigurationFlag.Undefined,
    EfsPanelFlag.VSCFlag:                     CircuitPanelConfigurationFlag.VSC,
    EfsPanelFlag.VSCEndingFlag:               CircuitPanelConfigurationFlag.VSCEnding,
    EfsPanelFlag.Code60Flag:                  CircuitPanelConfigurationFlag.Code60,
    EfsPanelFlag.SlowDownZoneNext:            CircuitPanelConfigurationFlag.SlowDownZoneNext,
    EfsPanelFlag.SlowDownZone:                CircuitPanelConfigurationFlag.SlowDownZone,
    EfsPanelFlag.SlowDownZoneEnd:             CircuitPanelConfigurationFlag.SlowDownZoneEnd,
    EfsPanelFlag.GoToPitFlag:                 CircuitPanelConfigurationFlag.GoToPit,
    EfsPanelFlag.FullCourseYellowFlag:        CircuitPanelConfigurationFlag.FCY,
    EfsPanelFlag.FiaRainFlag:                 CircuitPanelConfigurationFlag.FiaRain,
    EfsPanelFlag.FimRainFlag:                 CircuitPanelConfigurationFlag.FimRain,
    EfsPanelFlag.FimRainSlipperyFlag:         CircuitPanelConfigurationFlag.FimRainSlippery,
    EfsPanelFlag.FimPushFlag:                 CircuitPanelConfigurationFlag.FimPush,
    EfsPanelFlag.FimChequeredFlag:            CircuitPanelConfigurationFlag.FimChequered,
    EfsPanelFlag.FullCourseYellowEndingFlag:  CircuitPanelConfigurationFlag.FCYEnding,
    EfsPanelFlag.StandingStartFlag:           CircuitPanelConfigurationFlag.StandingStart,
    EfsPanelFlag.RollingStartFlag:            CircuitPanelConfigurationFlag.RollingStart,
    EfsPanelFlag.RoadClosedSign:              CircuitPanelConfigurationFlag.RoadClosed,
    EfsPanelFlag.TurnLeftSign:                CircuitPanelConfigurationFlag.TurnLeft,
    EfsPanelFlag.TurnRightSign:               CircuitPanelConfigurationFlag.TurnRight,
    EfsPanelFlag.GoLeftSign:                  CircuitPanelConfigurationFlag.GoLeft,
    EfsPanelFlag.GoRightSign:                 CircuitPanelConfigurationFlag.GoRight,
    EfsPanelFlag.GoAheadSign:                 CircuitPanelConfigurationFlag.GoAhead,
    EfsPanelFlag.BlueYellowBandFlag:          CircuitPanelConfigurationFlag.BlueYellowBand,
    EfsPanelFlag.BlackWhiteDiagonalCrossFlag: CircuitPanelConfigurationFlag.BlackWhiteDiagonalCross,
    EfsPanelFlag.PitlaneClosedFlag:           CircuitPanelConfigurationFlag.PitlaneClosed,
    EfsPanelFlag.BlackWhiteCrossFlag:         CircuitPanelConfigurationFlag.BlackWhiteCross,
    EfsPanelFlag.SafetyVehicleSign:           CircuitPanelConfigurationFlag.SafetyVehicle,
    EfsPanelFlag.PitRedFlag:                  CircuitPanelConfigurationFlag.PitRed,
    EfsPanelFlag.StopSign:                    CircuitPanelConfigurationFlag.Stop,
    EfsPanelFlag.HoldSign:                    CircuitPanelConfigurationFlag.Hold,
    EfsPanelFlag.GoSign:                      CircuitPanelConfigurationFlag.Go,
    EfsPanelFlag.PanelIdentifier:             CircuitPanelConfigurationFlag.PanelIdentifier,
    EfsPanelFlag.YellowSlipperyFlag:          CircuitPanelConfigurationFlag.YellowSlippery,
    EfsPanelFlag.CustomSign:                  CircuitPanelConfigurationFlag.CustomSign,
    EfsPanelFlag.SCPreparePassAround:         CircuitPanelConfigurationFlag.SCPreparePassAround,
    EfsPanelFlag.SCPassAround:                CircuitPanelConfigurationFlag.SCPassAround,
}

_PENALTY_FLAG_MAP: dict[int, FlagPageParams] = {
    EfsPanelFlag.FimLongLap:      FlagPageParams.LongLap,
    EfsPanelFlag.FimLongLapx2:    FlagPageParams.LongLapx2,
    EfsPanelFlag.DriveThrough:    FlagPageParams.DriveThrough,
    EfsPanelFlag.RideThrough:     FlagPageParams.RideThrough,
    EfsPanelFlag.ChangePosition:  FlagPageParams.ChangePosition,
    EfsPanelFlag.TimePenalty:     FlagPageParams.TimePenalty,
    EfsPanelFlag.Warning:         FlagPageParams.Warning,
    EfsPanelFlag.Equipment:       FlagPageParams.Equipment,
    EfsPanelFlag.InPit:           FlagPageParams.InPit,
    EfsPanelFlag.Loudness:        FlagPageParams.Loudness,
    EfsPanelFlag.StopAndGo:       FlagPageParams.StopAndGo,
    EfsPanelFlag.Behaviour:       FlagPageParams.Behaviour,
}

def convert_penalty_flag(old_flag: int) -> FlagPageParams | None:
    """
    Converte un valore EfsPanelFlag (campo Penalty) nel corrispondente FlagPageParams.
    Ritorna None se non ha corrispondente.
    """
    try:
        return _PENALTY_FLAG_MAP.get(EfsPanelFlag(old_flag))
    except ValueError:
        return None

def convert_flag(old_flag: int) -> CircuitPanelConfigurationFlag | None:
    """
    Converte un valore EfsPanelFlag nel corrispondente CircuitPanelConfigurationFlag.
    Ritorna None se la bandiera non ha corrispondente nel nuovo schema.
    """
    return _FLAG_MAP.get(EfsPanelFlag(old_flag))

def convert_speed_limit_flag(old_flag: int) -> CircuitPanelConfigurationFlag | None:
    """
    Converte un valore SpeedLimitFlag nel corrispondente CircuitPanelConfigurationFlag.
    Ritorna None se la bandiera non ha corrispondente nel nuovo schema.
    """
    try:
        return _SPEED_LIMIT_FLAG_MAP.get(SpeedLimitFlag(old_flag))
    except ValueError:
        return None

def int_to_rrggbb(color: int) -> str:
    return f"{color:06x}"