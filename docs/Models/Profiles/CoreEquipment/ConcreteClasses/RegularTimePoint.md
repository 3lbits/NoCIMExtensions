# RegularTimePoint

_Time point for a schedule where the time between the consecutive points is constant._

**URI**: [cim:RegularTimePoint](http://iec.ch/TC57/CIM100#RegularTimePoint)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RegularTimePoint
    click RegularTimePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegularTimePoint/"
    style RegularTimePoint fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegularTimePoint --> RegularIntervalSchedule : RegularTimePoint.IntervalSchedule

        RegularIntervalSchedule
            click RegularIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegularIntervalSchedule/"
            style RegularIntervalSchedule fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegularIntervalSchedule --> RegularTimePoint : RegularIntervalSchedule.TimePoints

        RegularIntervalSchedule
            click RegularIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegularIntervalSchedule/"
            style RegularIntervalSchedule fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        RegularTimePoint : RegularTimePoint.sequenceNumber
        RegularTimePoint : RegularTimePoint.value1
        RegularTimePoint : RegularTimePoint.value2
        RegularTimePoint : RegularTimePoint.IntervalSchedule
```

## Inheritance
* **RegularTimePoint**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| sequenceNumber | [cim:RegularTimePoint.sequenceNumber](http://iec.ch/TC57/CIM100#RegularTimePoint.sequenceNumber) | No cardinality available integer | The position of the regular time point in the sequence. Note that time points don't have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the associated regular interval schedule's time step with the regular time point sequence number and adding the associated schedules start time. To specify values for the start time, use sequence number 0.  The sequence number cannot be negative. | direct |
| value1 | [cim:RegularTimePoint.value1](http://iec.ch/TC57/CIM100#RegularTimePoint.value1) | No cardinality available float | The first value at the time. The meaning of the value is defined by the derived type of the associated schedule. | direct |
| value2 | [cim:RegularTimePoint.value2](http://iec.ch/TC57/CIM100#RegularTimePoint.value2) | No cardinality available float | The second value at the time. The meaning of the value is defined by the derived type of the associated schedule. | direct |
| IntervalSchedule | [cim:RegularTimePoint.IntervalSchedule](http://iec.ch/TC57/CIM100#RegularTimePoint.IntervalSchedule) | No cardinality available RegularIntervalSchedule | Regular interval schedule containing this time point. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
