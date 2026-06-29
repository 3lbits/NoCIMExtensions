# ActivePower

_Product of RMS value of the voltage and the RMS value of the in-phase component of the current._

**URI**: [cim:ActivePower](http://iec.ch/TC57/CIM100#ActivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePower
    click ActivePower href "/Models/Profiles/StateVariables/ConcreteClasses/ActivePower/"
    style ActivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> ActivePower : ACDCConverter.poleLossP

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvInjection --> ActivePower : SvInjection.pInjection

        SvInjection
            click SvInjection href "/Models/Profiles/StateVariables/ConcreteClasses/SvInjection/"
            style SvInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvPowerFlow --> ActivePower : SvPowerFlow.p

        SvPowerFlow
            click SvPowerFlow href "/Models/Profiles/StateVariables/ConcreteClasses/SvPowerFlow/"
            style SvPowerFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower --> UnitMultiplier : ActivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/StateVariables/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePower --> UnitSymbol : ActivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/StateVariables/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower : ActivePower.value
        ActivePower : ActivePower.multiplier
        ActivePower : ActivePower.unit
```

## Inheritance
* **ActivePower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:ActivePower.value](http://iec.ch/TC57/CIM100#ActivePower.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:ActivePower.multiplier](http://iec.ch/TC57/CIM100#ActivePower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:ActivePower.unit](http://iec.ch/TC57/CIM100#ActivePower.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
