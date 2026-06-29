# VoltagePerReactivePower

_Voltage variation with reactive power._

**URI**: [cim:VoltagePerReactivePower](http://iec.ch/TC57/CIM100#VoltagePerReactivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class VoltagePerReactivePower
    click VoltagePerReactivePower href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltagePerReactivePower/"
    style VoltagePerReactivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ShuntCompensator --> VoltagePerReactivePower : ShuntCompensator.voltageSensitivity

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        StaticVarCompensator --> VoltagePerReactivePower : StaticVarCompensator.slope

        StaticVarCompensator
            click StaticVarCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/StaticVarCompensator/"
            style StaticVarCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltagePerReactivePower --> UnitSymbol : VoltagePerReactivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        VoltagePerReactivePower --> UnitMultiplier : VoltagePerReactivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltagePerReactivePower : VoltagePerReactivePower.value
        VoltagePerReactivePower : VoltagePerReactivePower.unit
        VoltagePerReactivePower : VoltagePerReactivePower.multiplier
```

## Inheritance
* **VoltagePerReactivePower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:VoltagePerReactivePower.value](http://iec.ch/TC57/CIM100#VoltagePerReactivePower.value) | No cardinality available float | No description available | direct |
| unit | [cim:VoltagePerReactivePower.unit](http://iec.ch/TC57/CIM100#VoltagePerReactivePower.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:VoltagePerReactivePower.multiplier](http://iec.ch/TC57/CIM100#VoltagePerReactivePower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
