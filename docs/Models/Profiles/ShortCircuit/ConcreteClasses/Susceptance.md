# Susceptance

_Imaginary part of admittance._

**URI**: [cim:Susceptance](http://iec.ch/TC57/CIM100#Susceptance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Susceptance
    click Susceptance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Susceptance/"
    style Susceptance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Susceptance : ACLineSegment.b0ch

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LinearShuntCompensator --> Susceptance : LinearShuntCompensator.b0PerSection

        LinearShuntCompensator
            click LinearShuntCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/LinearShuntCompensator/"
            style LinearShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MutualCoupling --> Susceptance : MutualCoupling.b0ch

        MutualCoupling
            click MutualCoupling href "/Models/Profiles/ShortCircuit/ConcreteClasses/MutualCoupling/"
            style MutualCoupling fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensatorPoint --> Susceptance : NonlinearShuntCompensatorPoint.b0

        NonlinearShuntCompensatorPoint
            click NonlinearShuntCompensatorPoint href "/Models/Profiles/ShortCircuit/ConcreteClasses/NonlinearShuntCompensatorPoint/"
            style NonlinearShuntCompensatorPoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Susceptance : PowerTransformerEnd.b0

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Susceptance --> UnitSymbol : Susceptance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Susceptance --> UnitMultiplier : Susceptance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Susceptance : Susceptance.value
        Susceptance : Susceptance.unit
        Susceptance : Susceptance.multiplier
```

## Inheritance
* **Susceptance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Susceptance.value](http://iec.ch/TC57/CIM100#Susceptance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Susceptance.unit](http://iec.ch/TC57/CIM100#Susceptance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Susceptance.multiplier](http://iec.ch/TC57/CIM100#Susceptance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
