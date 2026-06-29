# Conductance

_Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance._

**URI**: [cim:Conductance](http://iec.ch/TC57/CIM100#Conductance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Conductance
    click Conductance href "/Models/Profiles/CoreEquipment/ConcreteClasses/Conductance/"
    style Conductance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Conductance : ACLineSegment.gch

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentShunt --> Conductance : EquivalentShunt.g

        EquivalentShunt
            click EquivalentShunt href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquivalentShunt/"
            style EquivalentShunt fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LinearShuntCompensator --> Conductance : LinearShuntCompensator.gPerSection

        LinearShuntCompensator
            click LinearShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/LinearShuntCompensator/"
            style LinearShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensatorPoint --> Conductance : NonlinearShuntCompensatorPoint.g

        NonlinearShuntCompensatorPoint
            click NonlinearShuntCompensatorPoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensatorPoint/"
            style NonlinearShuntCompensatorPoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Conductance : PowerTransformerEnd.g

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Conductance --> UnitSymbol : Conductance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Conductance --> UnitMultiplier : Conductance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Conductance : Conductance.value
        Conductance : Conductance.unit
        Conductance : Conductance.multiplier
```

## Inheritance
* **Conductance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Conductance.value](http://iec.ch/TC57/CIM100#Conductance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Conductance.unit](http://iec.ch/TC57/CIM100#Conductance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Conductance.multiplier](http://iec.ch/TC57/CIM100#Conductance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
