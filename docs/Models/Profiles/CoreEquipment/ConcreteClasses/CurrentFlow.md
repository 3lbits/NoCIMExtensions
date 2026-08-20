# CurrentFlow

_Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity node. Can be both AC and DC._

**URI**: [cim:CurrentFlow](http://iec.ch/TC57/CIM100#CurrentFlow)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class CurrentFlow
    click CurrentFlow href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurrentFlow/"
    style CurrentFlow fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        CsConverter --> CurrentFlow : CsConverter.maxIdc

        CsConverter
            click CsConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/CsConverter/"
            style CsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CsConverter --> CurrentFlow : CsConverter.minIdc

        CsConverter
            click CsConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/CsConverter/"
            style CsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CsConverter --> CurrentFlow : CsConverter.ratedIdc

        CsConverter
            click CsConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/CsConverter/"
            style CsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurrentLimit --> CurrentFlow : CurrentLimit.normalValue

        CurrentLimit
            click CurrentLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurrentLimit/"
            style CurrentLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch --> CurrentFlow : Switch.ratedCurrent

        Switch
            click Switch href "/Models/Profiles/CoreEquipment/ConcreteClasses/Switch/"
            style Switch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurrentFlow --> UnitMultiplier : CurrentFlow.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        CurrentFlow --> UnitSymbol : CurrentFlow.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurrentFlow : CurrentFlow.value
        CurrentFlow : CurrentFlow.multiplier
        CurrentFlow : CurrentFlow.unit
```

## Inheritance
* **CurrentFlow**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:CurrentFlow.value](http://iec.ch/TC57/CIM100#CurrentFlow.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:CurrentFlow.multiplier](http://iec.ch/TC57/CIM100#CurrentFlow.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:CurrentFlow.unit](http://iec.ch/TC57/CIM100#CurrentFlow.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
