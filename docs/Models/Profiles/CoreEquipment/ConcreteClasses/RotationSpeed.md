# RotationSpeed

_Number of revolutions per second._

**URI**: [cim:RotationSpeed](http://iec.ch/TC57/CIM100#RotationSpeed)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RotationSpeed
    click RotationSpeed href "/Models/Profiles/CoreEquipment/ConcreteClasses/RotationSpeed/"
    style RotationSpeed fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AsynchronousMachine --> RotationSpeed : AsynchronousMachine.nominalSpeed

        AsynchronousMachine
            click AsynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/AsynchronousMachine/"
            style AsynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotationSpeed --> UnitMultiplier : RotationSpeed.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RotationSpeed --> UnitSymbol : RotationSpeed.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotationSpeed : RotationSpeed.multiplier
        RotationSpeed : RotationSpeed.unit
        RotationSpeed : RotationSpeed.value
```

## Inheritance
* **RotationSpeed**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| multiplier | [cim:RotationSpeed.multiplier](http://iec.ch/TC57/CIM100#RotationSpeed.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:RotationSpeed.unit](http://iec.ch/TC57/CIM100#RotationSpeed.unit) | No cardinality available UnitSymbol | No description available | direct |
| value | [cim:RotationSpeed.value](http://iec.ch/TC57/CIM100#RotationSpeed.value) | No cardinality available float | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
