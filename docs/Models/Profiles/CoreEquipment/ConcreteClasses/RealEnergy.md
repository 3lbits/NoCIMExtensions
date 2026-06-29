# RealEnergy

_Real electrical energy._

**URI**: [cim:RealEnergy](http://iec.ch/TC57/CIM100#RealEnergy)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RealEnergy
    click RealEnergy href "/Models/Profiles/CoreEquipment/ConcreteClasses/RealEnergy/"
    style RealEnergy fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        BatteryUnit --> RealEnergy : BatteryUnit.ratedE

        BatteryUnit
            click BatteryUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/BatteryUnit/"
            style BatteryUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RealEnergy --> UnitMultiplier : RealEnergy.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RealEnergy --> UnitSymbol : RealEnergy.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RealEnergy : RealEnergy.multiplier
        RealEnergy : RealEnergy.unit
        RealEnergy : RealEnergy.value
```

## Inheritance
* **RealEnergy**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| multiplier | [cim:RealEnergy.multiplier](http://iec.ch/TC57/CIM100#RealEnergy.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:RealEnergy.unit](http://iec.ch/TC57/CIM100#RealEnergy.unit) | No cardinality available UnitSymbol | No description available | direct |
| value | [cim:RealEnergy.value](http://iec.ch/TC57/CIM100#RealEnergy.value) | No cardinality available float | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
