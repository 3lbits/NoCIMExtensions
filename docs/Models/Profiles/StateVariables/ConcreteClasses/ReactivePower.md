# ReactivePower

_Product of RMS value of the voltage and the RMS value of the quadrature component of the current._

**URI**: [cim:ReactivePower](http://iec.ch/TC57/CIM100#ReactivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ReactivePower
    click ReactivePower href "/Models/Profiles/StateVariables/ConcreteClasses/ReactivePower/"
    style ReactivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SvInjection --> ReactivePower : SvInjection.qInjection

        SvInjection
            click SvInjection href "/Models/Profiles/StateVariables/ConcreteClasses/SvInjection/"
            style SvInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvPowerFlow --> ReactivePower : SvPowerFlow.q

        SvPowerFlow
            click SvPowerFlow href "/Models/Profiles/StateVariables/ConcreteClasses/SvPowerFlow/"
            style SvPowerFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ReactivePower --> UnitSymbol : ReactivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/StateVariables/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ReactivePower --> UnitMultiplier : ReactivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/StateVariables/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ReactivePower : ReactivePower.value
        ReactivePower : ReactivePower.unit
        ReactivePower : ReactivePower.multiplier
```

## Inheritance
* **ReactivePower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:ReactivePower.value](http://iec.ch/TC57/CIM100#ReactivePower.value) | No cardinality available float | No description available | direct |
| unit | [cim:ReactivePower.unit](http://iec.ch/TC57/CIM100#ReactivePower.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:ReactivePower.multiplier](http://iec.ch/TC57/CIM100#ReactivePower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
