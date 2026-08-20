# ActivePowerPerCurrentFlow

_Active power variation with current flow._

**URI**: [cim:ActivePowerPerCurrentFlow](http://iec.ch/TC57/CIM100#ActivePowerPerCurrentFlow)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePowerPerCurrentFlow
    click ActivePowerPerCurrentFlow href "/Models/Profiles/CoreEquipment/ConcreteClasses/ActivePowerPerCurrentFlow/"
    style ActivePowerPerCurrentFlow fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> ActivePowerPerCurrentFlow : ACDCConverter.switchingLoss

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerPerCurrentFlow --> UnitMultiplier : ActivePowerPerCurrentFlow.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePowerPerCurrentFlow --> UnitSymbol : ActivePowerPerCurrentFlow.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerPerCurrentFlow : ActivePowerPerCurrentFlow.multiplier
        ActivePowerPerCurrentFlow : ActivePowerPerCurrentFlow.unit
        ActivePowerPerCurrentFlow : ActivePowerPerCurrentFlow.value
```

## Inheritance
* **ActivePowerPerCurrentFlow**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| multiplier | [cim:ActivePowerPerCurrentFlow.multiplier](http://iec.ch/TC57/CIM100#ActivePowerPerCurrentFlow.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:ActivePowerPerCurrentFlow.unit](http://iec.ch/TC57/CIM100#ActivePowerPerCurrentFlow.unit) | No cardinality available UnitSymbol | No description available | direct |
| value | [cim:ActivePowerPerCurrentFlow.value](http://iec.ch/TC57/CIM100#ActivePowerPerCurrentFlow.value) | No cardinality available float | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
