# Inductance

_Inductive part of reactance (imaginary part of impedance), at rated frequency._

**URI**: [cim:Inductance](http://iec.ch/TC57/CIM100#Inductance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Inductance
    click Inductance href "/Models/Profiles/CoreEquipment/ConcreteClasses/Inductance/"
    style Inductance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCGround --> Inductance : DCGround.inductance

        DCGround
            click DCGround href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCGround/"
            style DCGround fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCLineSegment --> Inductance : DCLineSegment.inductance

        DCLineSegment
            click DCLineSegment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLineSegment/"
            style DCLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCSeriesDevice --> Inductance : DCSeriesDevice.inductance

        DCSeriesDevice
            click DCSeriesDevice href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCSeriesDevice/"
            style DCSeriesDevice fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Inductance --> UnitSymbol : Inductance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Inductance --> UnitMultiplier : Inductance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Inductance : Inductance.value
        Inductance : Inductance.unit
        Inductance : Inductance.multiplier
```

## Inheritance
* **Inductance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Inductance.value](http://iec.ch/TC57/CIM100#Inductance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Inductance.unit](http://iec.ch/TC57/CIM100#Inductance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Inductance.multiplier](http://iec.ch/TC57/CIM100#Inductance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
