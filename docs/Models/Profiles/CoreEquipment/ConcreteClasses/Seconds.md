# Seconds

_Time, in seconds._

**URI**: [cim:Seconds](http://iec.ch/TC57/CIM100#Seconds)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Seconds
    click Seconds href "/Models/Profiles/CoreEquipment/ConcreteClasses/Seconds/"
    style Seconds fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        GeneratingUnit --> Seconds : GeneratingUnit.startupTime

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitType --> Seconds : OperationalLimitType.acceptableDuration

        OperationalLimitType
            click OperationalLimitType href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitType/"
            style OperationalLimitType fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegularIntervalSchedule --> Seconds : RegularIntervalSchedule.timeStep

        RegularIntervalSchedule
            click RegularIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegularIntervalSchedule/"
            style RegularIntervalSchedule fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ShuntCompensator --> Seconds : ShuntCompensator.aVRDelay

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Seconds --> UnitSymbol : Seconds.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Seconds --> UnitMultiplier : Seconds.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Seconds : Seconds.value
        Seconds : Seconds.unit
        Seconds : Seconds.multiplier
```

## Inheritance
* **Seconds**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Seconds.value](http://iec.ch/TC57/CIM100#Seconds.value) | No cardinality available float | Time, in seconds | direct |
| unit | [cim:Seconds.unit](http://iec.ch/TC57/CIM100#Seconds.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Seconds.multiplier](http://iec.ch/TC57/CIM100#Seconds.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
