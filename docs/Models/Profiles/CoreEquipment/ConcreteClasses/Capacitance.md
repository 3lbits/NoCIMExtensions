# Capacitance

_Capacitive part of reactance (imaginary part of impedance), at rated frequency._

**URI**: [cim:Capacitance](http://iec.ch/TC57/CIM100#Capacitance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Capacitance
    click Capacitance href "/Models/Profiles/CoreEquipment/ConcreteClasses/Capacitance/"
    style Capacitance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCLineSegment --> Capacitance : DCLineSegment.capacitance

        DCLineSegment
            click DCLineSegment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLineSegment/"
            style DCLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCShunt --> Capacitance : DCShunt.capacitance

        DCShunt
            click DCShunt href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCShunt/"
            style DCShunt fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Capacitance --> UnitSymbol : Capacitance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Capacitance --> UnitMultiplier : Capacitance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Capacitance : Capacitance.value
        Capacitance : Capacitance.unit
        Capacitance : Capacitance.multiplier
```

## Inheritance
* **Capacitance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Capacitance.value](http://iec.ch/TC57/CIM100#Capacitance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Capacitance.unit](http://iec.ch/TC57/CIM100#Capacitance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Capacitance.multiplier](http://iec.ch/TC57/CIM100#Capacitance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
