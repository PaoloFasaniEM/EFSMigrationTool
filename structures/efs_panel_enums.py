from enum import IntEnum

class EfsPanelModel(IntEnum):
    ModelT1          = 0
    ModelTLite       = 1
    ModelXixunM      = 2
    ModelT2          = 3
    ModelXixunK      = 4
    ModelEMLiveBoard = 5
    ModelT3          = 6
    ModelT4          = 7
    ThirdPartyPanel  = 8


class EfsPanelType(IntEnum):
    TrackSidePanel = 0
    PitlanePanel   = 1
    InfoPanel      = 2


class EfsPanelSize(IntEnum):
    Size50x40  = 0
    Size96x64  = 1
    Size112x72 = 2
    Size30x28  = 3
    Size30x24  = 4
    Size192x96 = 5
    Size64x64  = 6
    Size192x128 = 7
    Size48x48  = 8
    Size40x40  = 9
    Size32x32  = 10
    Size360x150 = 11
    Size256x128 = 12
    Size384x128 = 13
    Size384x64  = 14
    Size624x312 = 15
    Size312x208 = 16
    Size768x512 = 17


class EMTPanelModel(IntEnum):
    NullModel = 0
    T1        = 1
    T2        = 2
    TLite     = 3
    T3        = 4
    T4        = 5


class EMTPanelSize(IntEnum):
    NullSize  = 0
    Size50x40 = 1
    Size30x28 = 2
    Size30x24 = 3
    Size48x48 = 4
    Size40x40 = 5
    Size32x32 = 6


class EMInfoPanelModel(IntEnum):
    NullModel = 0
    EM1       = 1


class EMInfoPanelSize(IntEnum):
    NullSize    = 0
    Size96x64   = 1
    Size112x72  = 2
    Size192x96  = 3
    Size64x64   = 4
    Size192x128 = 5
    Size360x150 = 6
    Size384x128 = 7
    Size256x128 = 8
    Size384x64  = 9
    Size624x312 = 10
    Size312x208 = 11
    Size768x512 = 12


class ThirdPartyPanelType(IntEnum):
    UndefinedType = 0
    TrackSide     = 1
    Info          = 2


class ThirdPartyPanelAspectRatio(IntEnum):
    UndefinedRatio = 0
    Ratio2_1       = 1
    Ratio3_2       = 2