# AngleRadians

_Phase angle in radians._

**URI**: [cim:AngleRadians](http://iec.ch/TC57/CIM100#AngleRadians)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AngleRadians
    click AngleRadians href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/AngleRadians/"
    style AngleRadians fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EnergySource --> AngleRadians : EnergySource.voltageAngle

        EnergySource
            click EnergySource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AngleRadians --> UnitSymbol : AngleRadians.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        AngleRadians --> UnitMultiplier : AngleRadians.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AngleRadians : AngleRadians.value
        AngleRadians : AngleRadians.unit
        AngleRadians : AngleRadians.multiplier
```

## Inheritance
* **AngleRadians**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:AngleRadians.value](http://iec.ch/TC57/CIM100#AngleRadians.value) | No cardinality available float | No description available | direct |
| unit | [cim:AngleRadians.unit](http://iec.ch/TC57/CIM100#AngleRadians.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:AngleRadians.multiplier](http://iec.ch/TC57/CIM100#AngleRadians.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
