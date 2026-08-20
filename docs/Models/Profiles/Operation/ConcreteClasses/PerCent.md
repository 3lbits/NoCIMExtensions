# PerCent

_Percentage on a defined base.   For example, specify as 100 to indicate at the defined base._

**URI**: [cim:PerCent](http://iec.ch/TC57/CIM100#PerCent)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PerCent
    click PerCent href "/Models/Profiles/Operation/ConcreteClasses/PerCent/"
    style PerCent fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        MeasurementValue --> PerCent : MeasurementValue.sensorAccuracy

        MeasurementValue
            click MeasurementValue href "/Models/Profiles/Operation/ConcreteClasses/MeasurementValue/"
            style MeasurementValue fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PerCent --> UnitSymbol : PerCent.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/Operation/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PerCent --> UnitMultiplier : PerCent.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/Operation/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PerCent : PerCent.value
        PerCent : PerCent.unit
        PerCent : PerCent.multiplier
```

## Inheritance
* **PerCent**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:PerCent.value](http://iec.ch/TC57/CIM100#PerCent.value) | No cardinality available float | Normally 0 to 100 on a defined base. | direct |
| unit | [cim:PerCent.unit](http://iec.ch/TC57/CIM100#PerCent.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:PerCent.multiplier](http://iec.ch/TC57/CIM100#PerCent.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
