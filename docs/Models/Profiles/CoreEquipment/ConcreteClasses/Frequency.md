# Frequency

_Cycles per second._

**URI**: [cim:Frequency](http://iec.ch/TC57/CIM100#Frequency)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Frequency
    click Frequency href "/Models/Profiles/CoreEquipment/ConcreteClasses/Frequency/"
    style Frequency fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AsynchronousMachine --> Frequency : AsynchronousMachine.nominalFrequency

        AsynchronousMachine
            click AsynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/AsynchronousMachine/"
            style AsynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Frequency --> UnitSymbol : Frequency.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Frequency --> UnitMultiplier : Frequency.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Frequency : Frequency.value
        Frequency : Frequency.unit
        Frequency : Frequency.multiplier
```

## Inheritance
* **Frequency**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Frequency.value](http://iec.ch/TC57/CIM100#Frequency.value) | No cardinality available float | No description available | direct |
| unit | [cim:Frequency.unit](http://iec.ch/TC57/CIM100#Frequency.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Frequency.multiplier](http://iec.ch/TC57/CIM100#Frequency.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
