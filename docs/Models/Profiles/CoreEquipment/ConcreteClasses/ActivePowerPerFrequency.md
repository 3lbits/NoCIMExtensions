# ActivePowerPerFrequency

_Active power variation with frequency._

**URI**: [cim:ActivePowerPerFrequency](http://iec.ch/TC57/CIM100#ActivePowerPerFrequency)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePowerPerFrequency
    click ActivePowerPerFrequency href "/Models/Profiles/CoreEquipment/ConcreteClasses/ActivePowerPerFrequency/"
    style ActivePowerPerFrequency fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ExternalNetworkInjection --> ActivePowerPerFrequency : ExternalNetworkInjection.governorSCD

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerPerFrequency --> UnitMultiplier : ActivePowerPerFrequency.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePowerPerFrequency --> UnitSymbol : ActivePowerPerFrequency.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerPerFrequency : ActivePowerPerFrequency.multiplier
        ActivePowerPerFrequency : ActivePowerPerFrequency.unit
        ActivePowerPerFrequency : ActivePowerPerFrequency.value
```

## Inheritance
* **ActivePowerPerFrequency**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| multiplier | [cim:ActivePowerPerFrequency.multiplier](http://iec.ch/TC57/CIM100#ActivePowerPerFrequency.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:ActivePowerPerFrequency.unit](http://iec.ch/TC57/CIM100#ActivePowerPerFrequency.unit) | No cardinality available UnitSymbol | No description available | direct |
| value | [cim:ActivePowerPerFrequency.value](http://iec.ch/TC57/CIM100#ActivePowerPerFrequency.value) | No cardinality available float | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
