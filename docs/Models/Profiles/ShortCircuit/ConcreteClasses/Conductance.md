# Conductance

_Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance._

**URI**: [cim:Conductance](http://iec.ch/TC57/CIM100#Conductance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Conductance
    click Conductance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Conductance/"
    style Conductance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Conductance : ACLineSegment.g0ch

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LinearShuntCompensator --> Conductance : LinearShuntCompensator.g0PerSection

        LinearShuntCompensator
            click LinearShuntCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/LinearShuntCompensator/"
            style LinearShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MutualCoupling --> Conductance : MutualCoupling.g0ch

        MutualCoupling
            click MutualCoupling href "/Models/Profiles/ShortCircuit/ConcreteClasses/MutualCoupling/"
            style MutualCoupling fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensatorPoint --> Conductance : NonlinearShuntCompensatorPoint.g0

        NonlinearShuntCompensatorPoint
            click NonlinearShuntCompensatorPoint href "/Models/Profiles/ShortCircuit/ConcreteClasses/NonlinearShuntCompensatorPoint/"
            style NonlinearShuntCompensatorPoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Conductance : PowerTransformerEnd.g0

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Conductance --> UnitSymbol : Conductance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Conductance --> UnitMultiplier : Conductance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
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
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
