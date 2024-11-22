# Watt App Vocabulary

**URI**: https://ap-no.cim4.eu/WattApp/1.0

**Name**: WattApp

## Classes

| Class | Description |
| --- | --- |
| [ACDCTerminal](ACDCTerminal.md) | None |
| [ACPointOfCommonCoupling](ACPointOfCommonCoupling.md) | Point of interconnection of the DC converter station to the adjacent AC system (IEC 60633). |
| [Analog](Analog.md) | Analog represents an analog Measurement. |
| [AnalogValue](AnalogValue.md) | AnalogValue represents an analog MeasurementValue. |
| [BaseIrregularTimeSeries](BaseIrregularTimeSeries.md) | Time series that has irregular points in time. |
| [BaseTimeSeries](BaseTimeSeries.md) | Time series of values at points in time. |
| [CapacitySchedule](CapacitySchedule.md) | The schedule for the capacity. |
| [CapacityTimePoint](CapacityTimePoint.md) |  |
| [ConductingEquipment](ConductingEquipment.md) | The parts of the AC power system that are designed to carry current or that are conductively connected through terminals. |
| [ConnectivityNode](ConnectivityNode.md) | Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance. |
| [ConnectivityNodeContainer](ConnectivityNodeContainer.md) | A base class for all objects that may contain connectivity nodes or topological nodes. |
| [Equipment](Equipment.md) | The parts of a power system that are physical devices, electronic or mechanical. |
| [EquipmentContainer](EquipmentContainer.md) | A modelling construct to provide a root class for containing equipment. |
| [Feature](Feature.md) | Defines a system base voltage which is referenced. |
| [Feeder](Feeder.md) | A collection of equipment for organizational purposes, used for grouping distribution resources. The organization a feeder does not necessarily reflect connectivity or current operation state. |
| [Geometry](Geometry.md) | Geometric representation details. |
| [GeometryObject](GeometryObject.md) | An object that represents a jsonld compound to support value, type and language. |
| [IOPoint](IOPoint.md) | The class describe a measurement or control value. The purpose is to enable having attributes and associations common for measurement and control. |
| [IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing identification and naming attributes. |
| [LanguageObject](LanguageObject.md) | An object that represents a jsonld compound to support value, type and language. |
| [Measurement](Measurement.md) | A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.
The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leaves, e.g. Substation-VoltageLevel-Bay-Switch-Measurement.
Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (VT) or potential transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.
If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance.
When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone. |
| [MeasurementValue](MeasurementValue.md) | The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement. |
| [PointOfCommonCoupling](PointOfCommonCoupling.md) | Point of Common Coupling (PCC) refers to the location where multiple electrical sources or loads are electrically connected and provide a reference point where the voltages and currents from different parts of the system are considered to be common. The PCC is used to support system analysis, control, and monitoring, as it provides a reference for understanding the interactions and power flow between various components within the system. It is also relevant to define the requirement and responsibility between different actors in operating a power system. |
| [PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated. |
| [PowerTransformer](PowerTransformer.md) | An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
A power transformer may be composed of separate transformer tanks that need not be identical.
A power transformer can be modelled with or without tanks and is intended for use in both balanced and unbalanced representations. A power transformer typically has two terminals, but may have one (grounding), three or more terminals.
The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead. |
| [PowerTransformerEnd](PowerTransformerEnd.md) | A PowerTransformerEnd is associated with each Terminal of a PowerTransformer.
The impedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalent as follows.
1) for a two Terminal PowerTransformer the high voltage (TransformerEnd.endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0.  Parameters are always provided, even if the PowerTransformerEnds have the same rated voltage.  In this case, the parameters are provided at the PowerTransformerEnd which has TransformerEnd.endNumber equal to 1.
2) for a three Terminal PowerTransformer the three PowerTransformerEnds represent a star equivalent with each leg in the star represented by r, r0, x, and x0 values.
3) For a three Terminal transformer each PowerTransformerEnd shall have g, g0, b and b0 values corresponding to the no load losses distributed on the three PowerTransformerEnds. The total no load loss shunt impedances may also be placed at one of the PowerTransformerEnds, preferably the end numbered 1, having the shunt values on end 1.  This is the preferred way.
4) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
Each PowerTransformerEnd must be contained by a PowerTransformer. Because a PowerTransformerEnd (or any other object) can not be contained by more than one parent, a PowerTransformerEnd can not have an association to an EquipmentContainer (Substation, VoltageLevel, etc). |
| [SpatialObject](SpatialObject.md) | A spatial object is a physical object that has a location in space. It may have a geometric representation to describe its shape and position. |
| [Substation](Substation.md) | A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics. |
| [Terminal](Terminal.md) | An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes. |
| [TransformerEnd](TransformerEnd.md) | A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because it associates to terminal but is not a specialization of ConductingEquipment. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [BaseTimeSeriesKind](BaseTimeSeriesKind.md) |  |
| [PhaseCode](PhaseCode.md) | Enumeration of phase identifiers. Allows designation of phases for both transmission and distribution equipment, circuits and loads.Residential and small commercial loads are often served from single-phase, or split-phase, secondary circuits. For example of s12N, phases 1 and 2 refer to hot wires that are 180 degrees out of phase, while N refers to the neutral wire. Through single-phase transformer connections, these secondary circuits may be served from one or two of the primary phases A, B, and C. For three-phase loads, use the A, B, C phase codes instead of s12N. |
| [TimeSeriesInterpolationKind](TimeSeriesInterpolationKind.md) |  |
| [UnitMultiplier](UnitMultiplier.md) | The unit multipliers defined for the CIM. |
| [UnitSymbol](UnitSymbol.md) | The units defined for usage in the CIM. |
