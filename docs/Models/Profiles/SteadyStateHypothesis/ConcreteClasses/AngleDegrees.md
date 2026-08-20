# AngleDegrees

_Measurement of angle in degrees._

**URI**: [cim:AngleDegrees](http://iec.ch/TC57/CIM100#AngleDegrees)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AngleDegrees
    click AngleDegrees href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/AngleDegrees/"
    style AngleDegrees fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        CsConverter --> AngleDegrees : CsConverter.targetAlpha

        CsConverter
            click CsConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/CsConverter/"
            style CsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CsConverter --> AngleDegrees : CsConverter.targetGamma

        CsConverter
            click CsConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/CsConverter/"
            style CsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VsConverter --> AngleDegrees : VsConverter.targetPhasePcc

        VsConverter
            click VsConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/VsConverter/"
            style VsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AngleDegrees --> UnitSymbol : AngleDegrees.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        AngleDegrees --> UnitMultiplier : AngleDegrees.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AngleDegrees : AngleDegrees.value
        AngleDegrees : AngleDegrees.unit
        AngleDegrees : AngleDegrees.multiplier
```

## Inheritance
* **AngleDegrees**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:AngleDegrees.value](http://iec.ch/TC57/CIM100#AngleDegrees.value) | No cardinality available float | No description available | direct |
| unit | [cim:AngleDegrees.unit](http://iec.ch/TC57/CIM100#AngleDegrees.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:AngleDegrees.multiplier](http://iec.ch/TC57/CIM100#AngleDegrees.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
