import struct
from dataclasses import dataclass


@dataclass
class DashPacket:
    IsRaceOn: int

    TimestampMS: int

    EngineMaxRpm: float
    EngineIdleRpm: float
    CurrentEngineRpm: float

    AccelerationX: float
    AccelerationY: float
    AccelerationZ: float

    VelocityX: float
    VelocityY: float
    VelocityZ: float

    AngularVelocityX: float
    AngularVelocityY: float
    AngularVelocityZ: float

    Yaw: float
    Pitch: float
    Roll: float

    NormalizedSuspensionTravelFrontLeft: float
    NormalizedSuspensionTravelFrontRight: float
    NormalizedSuspensionTravelRearLeft: float
    NormalizedSuspensionTravelRearRight: float

    TireSlipRatioFrontLeft: float
    TireSlipRatioFrontRight: float
    TireSlipRatioRearLeft: float
    TireSlipRatioRearRight: float

    WheelRotationSpeedFrontLeft: float
    WheelRotationSpeedFrontRight: float
    WheelRotationSpeedRearLeft: float
    WheelRotationSpeedRearRight: float

    WheelOnRumbleStripFrontLeft: float
    WheelOnRumbleStripFrontRight: float
    WheelOnRumbleStripRearLeft: float
    WheelOnRumbleStripRearRight: float

    WheelInPuddleDepthFrontLeft: float
    WheelInPuddleDepthFrontRight: float
    WheelInPuddleDepthRearLeft: float
    WheelInPuddleDepthRearRight: float

    SurfaceRumbleFrontLeft: float
    SurfaceRumbleFrontRight: float
    SurfaceRumbleRearLeft: float
    SurfaceRumbleRearRight: float

    TireSlipAngleFrontLeft: float
    TireSlipAngleFrontRight: float
    TireSlipAngleRearLeft: float
    TireSlipAngleRearRight: float

    TireCombinedSlipFrontLeft: float
    TireCombinedSlipFrontRight: float
    TireCombinedSlipRearLeft: float
    TireCombinedSlipRearRight: float

    SuspensionTravelMetersFrontLeft: float
    SuspensionTravelMetersFrontRight: float
    SuspensionTravelMetersRearLeft: float
    SuspensionTravelMetersRearRight: float

    CarOrdinal: int
    CarClass: int
    CarPerformanceIndex: int
    DrivetrainType: int
    NumCylinders: int

    PositionX: float
    PositionY: float
    PositionZ: float

    Speed: float
    Power: float
    Torque: float

    TireTempFrontLeft: float
    TireTempFrontRight: float
    TireTempRearLeft: float
    TireTempRearRight: float

    Boost: float
    Fuel: float
    DistanceTraveled: float
    BestLap: float
    LastLap: float
    CurrentLap: float
    CurrentRaceTime: float

    LapNumber: int
    RacePosition: int

    Accel: int
    Brake: int
    Clutch: int
    HandBrake: int
    Gear: int
    Steer: int

    NormalizedDrivingLine: int
    NormalizedAIBrakeDifference: int


class DashCodec:
    format: str = '<iIfffffffffffffffffffffffffffffffffffffffffffffffffffiiiiifffffffffffffffffHBBBBBBbbb'

    attrs = [
        'IsRaceOn',
        'TimestampMS',
        'EngineMaxRpm',
        'EngineIdleRpm',
        'CurrentEngineRpm',
        'AccelerationX',
        'AccelerationY',
        'AccelerationZ',
        'VelocityX',
        'VelocityY',
        'VelocityZ',
        'AngularVelocityX',
        'AngularVelocityY',
        'AngularVelocityZ',
        'Yaw',
        'Pitch',
        'Roll',
        'NormalizedSuspensionTravelFrontLeft',
        'NormalizedSuspensionTravelFrontRight',
        'NormalizedSuspensionTravelRearLeft',
        'NormalizedSuspensionTravelRearRight',
        'TireSlipRatioFrontLeft',
        'TireSlipRatioFrontRight',
        'TireSlipRatioRearLeft',
        'TireSlipRatioRearRight',
        'WheelRotationSpeedFrontLeft',
        'WheelRotationSpeedFrontRight',
        'WheelRotationSpeedRearLeft',
        'WheelRotationSpeedRearRight',
        'WheelOnRumbleStripFrontLeft',
        'WheelOnRumbleStripFrontRight',
        'WheelOnRumbleStripRearLeft',
        'WheelOnRumbleStripRearRight',
        'WheelInPuddleDepthFrontLeft',
        'WheelInPuddleDepthFrontRight',
        'WheelInPuddleDepthRearLeft',
        'WheelInPuddleDepthRearRight',
        'SurfaceRumbleFrontLeft',
        'SurfaceRumbleFrontRight',
        'SurfaceRumbleRearLeft',
        'SurfaceRumbleRearRight',
        'TireSlipAngleFrontLeft',
        'TireSlipAngleFrontRight',
        'TireSlipAngleRearLeft',
        'TireSlipAngleRearRight',
        'TireCombinedSlipFrontLeft',
        'TireCombinedSlipFrontRight',
        'TireCombinedSlipRearLeft',
        'TireCombinedSlipRearRight',
        'SuspensionTravelMetersFrontLeft',
        'SuspensionTravelMetersFrontRight',
        'SuspensionTravelMetersRearLeft',
        'SuspensionTravelMetersRearRight',
        'CarOrdinal',
        'CarClass',
        'CarPerformanceIndex',
        'DrivetrainType',
        'NumCylinders',
        'PositionX',
        'PositionY',
        'PositionZ',
        'Speed',
        'Power',
        'Torque',
        'TireTempFrontLeft',
        'TireTempFrontRight',
        'TireTempRearLeft',
        'TireTempRearRight',
        'Boost',
        'Fuel',
        'DistanceTraveled',
        'BestLap',
        'LastLap',
        'CurrentLap',
        'CurrentRaceTime',
        'LapNumber',
        'RacePosition',
        'Accel',
        'Brake',
        'Clutch',
        'HandBrake',
        'Gear',
        'Steer',
        'NormalizedDrivingLine',
        'NormalizedAIBrakeDifference',
    ]

    def unpack(self, data) -> DashPacket:
        IsRaceOn, \
        TimestampMS, \
        EngineMaxRpm, \
        EngineIdleRpm, \
        CurrentEngineRpm, \
        AccelerationX, \
        AccelerationY, \
        AccelerationZ, \
        VelocityX, \
        VelocityY, \
        VelocityZ, \
        AngularVelocityX, \
        AngularVelocityY, \
        AngularVelocityZ, \
        Yaw, \
        Pitch, \
        Roll, \
        NormalizedSuspensionTravelFrontLeft, \
        NormalizedSuspensionTravelFrontRight, \
        NormalizedSuspensionTravelRearLeft, \
        NormalizedSuspensionTravelRearRight, \
        TireSlipRatioFrontLeft, \
        TireSlipRatioFrontRight, \
        TireSlipRatioRearLeft, \
        TireSlipRatioRearRight, \
        WheelRotationSpeedFrontLeft, \
        WheelRotationSpeedFrontRight, \
        WheelRotationSpeedRearLeft, \
        WheelRotationSpeedRearRight, \
        WheelOnRumbleStripFrontLeft, \
        WheelOnRumbleStripFrontRight, \
        WheelOnRumbleStripRearLeft, \
        WheelOnRumbleStripRearRight, \
        WheelInPuddleDepthFrontLeft, \
        WheelInPuddleDepthFrontRight, \
        WheelInPuddleDepthRearLeft, \
        WheelInPuddleDepthRearRight, \
        SurfaceRumbleFrontLeft, \
        SurfaceRumbleFrontRight, \
        SurfaceRumbleRearLeft, \
        SurfaceRumbleRearRight, \
        TireSlipAngleFrontLeft, \
        TireSlipAngleFrontRight, \
        TireSlipAngleRearLeft, \
        TireSlipAngleRearRight, \
        TireCombinedSlipFrontLeft, \
        TireCombinedSlipFrontRight, \
        TireCombinedSlipRearLeft, \
        TireCombinedSlipRearRight, \
        SuspensionTravelMetersFrontLeft, \
        SuspensionTravelMetersFrontRight, \
        SuspensionTravelMetersRearLeft, \
        SuspensionTravelMetersRearRight, \
        CarOrdinal, \
        CarClass, \
        CarPerformanceIndex, \
        DrivetrainType, \
        NumCylinders, \
        PositionX, \
        PositionY, \
        PositionZ, \
        Speed, \
        Power, \
        Torque, \
        TireTempFrontLeft, \
        TireTempFrontRight, \
        TireTempRearLeft, \
        TireTempRearRight, \
        Boost, \
        Fuel, \
        DistanceTraveled, \
        BestLap, \
        LastLap, \
        CurrentLap, \
        CurrentRaceTime, \
        LapNumber, \
        RacePosition, \
        Accel, \
        Brake, \
        Clutch, \
        HandBrake, \
        Gear, \
        Steer, \
        NormalizedDrivingLine, \
        NormalizedAIBrakeDifference = struct.unpack(self.format, data)

        return DashPacket(
            IsRaceOn,
            TimestampMS,
            EngineMaxRpm,
            EngineIdleRpm,
            CurrentEngineRpm,
            AccelerationX,
            AccelerationY,
            AccelerationZ,
            VelocityX,
            VelocityY,
            VelocityZ,
            AngularVelocityX,
            AngularVelocityY,
            AngularVelocityZ,
            Yaw,
            Pitch,
            Roll,
            NormalizedSuspensionTravelFrontLeft,
            NormalizedSuspensionTravelFrontRight,
            NormalizedSuspensionTravelRearLeft,
            NormalizedSuspensionTravelRearRight,
            TireSlipRatioFrontLeft,
            TireSlipRatioFrontRight,
            TireSlipRatioRearLeft,
            TireSlipRatioRearRight,
            WheelRotationSpeedFrontLeft,
            WheelRotationSpeedFrontRight,
            WheelRotationSpeedRearLeft,
            WheelRotationSpeedRearRight,
            WheelOnRumbleStripFrontLeft,
            WheelOnRumbleStripFrontRight,
            WheelOnRumbleStripRearLeft,
            WheelOnRumbleStripRearRight,
            WheelInPuddleDepthFrontLeft,
            WheelInPuddleDepthFrontRight,
            WheelInPuddleDepthRearLeft,
            WheelInPuddleDepthRearRight,
            SurfaceRumbleFrontLeft,
            SurfaceRumbleFrontRight,
            SurfaceRumbleRearLeft,
            SurfaceRumbleRearRight,
            TireSlipAngleFrontLeft,
            TireSlipAngleFrontRight,
            TireSlipAngleRearLeft,
            TireSlipAngleRearRight,
            TireCombinedSlipFrontLeft,
            TireCombinedSlipFrontRight,
            TireCombinedSlipRearLeft,
            TireCombinedSlipRearRight,
            SuspensionTravelMetersFrontLeft,
            SuspensionTravelMetersFrontRight,
            SuspensionTravelMetersRearLeft,
            SuspensionTravelMetersRearRight,
            CarOrdinal,
            CarClass,
            CarPerformanceIndex,
            DrivetrainType,
            NumCylinders,
            PositionX,
            PositionY,
            PositionZ,
            Speed,
            Power,
            Torque,
            TireTempFrontLeft,
            TireTempFrontRight,
            TireTempRearLeft,
            TireTempRearRight,
            Boost,
            Fuel,
            DistanceTraveled,
            BestLap,
            LastLap,
            CurrentLap,
            CurrentRaceTime,
            LapNumber,
            RacePosition,
            Accel,
            Brake,
            Clutch,
            HandBrake,
            Gear,
            Steer,
            NormalizedDrivingLine,
            NormalizedAIBrakeDifference
        )
