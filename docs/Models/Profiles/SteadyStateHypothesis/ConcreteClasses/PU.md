# PU

_Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10._

**URI**: [cim:PU](http://iec.ch/TC57/CIM100#PU)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PU
    click PU href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PU/"
    style PU fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        VsConverter --> PU : VsConverter.droop

        VsConverter
            click VsConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/VsConverter/"
            style VsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PU --> UnitSymbol : PU.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PU --> UnitMultiplier : PU.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PU : PU.value
        PU : PU.unit
        PU : PU.multiplier
```

## Inheritance
* **PU**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:PU.value](http://iec.ch/TC57/CIM100#PU.value) | No cardinality available float | No description available | direct |
| unit | [cim:PU.unit](http://iec.ch/TC57/CIM100#PU.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:PU.multiplier](http://iec.ch/TC57/CIM100#PU.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
