# Money

_Amount of money._

**URI**: [cim:Money](http://iec.ch/TC57/CIM100#Money)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Money
    click Money href "/Models/Profiles/CoreEquipment/ConcreteClasses/Money/"
    style Money fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        GeneratingUnit --> Money : GeneratingUnit.startupCost

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> Money : GeneratingUnit.variableCost

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Money --> Currency : Money.unit

        Currency
            click Currency href "/Models/Profiles/CoreEquipment/Enumerations/Currency/"
            style Currency fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Money --> UnitMultiplier : Money.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Money : Money.unit
        Money : Money.multiplier
        Money : Money.value
```

## Inheritance
* **Money**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| unit | [cim:Money.unit](http://iec.ch/TC57/CIM100#Money.unit) | No cardinality available Currency | No description available | direct |
| multiplier | [cim:Money.multiplier](http://iec.ch/TC57/CIM100#Money.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| value | [cim:Money.value](http://iec.ch/TC57/CIM100#Money.value) | No cardinality available double | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
