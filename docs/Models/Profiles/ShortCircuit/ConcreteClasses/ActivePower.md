# ActivePower

_Product of RMS value of the voltage and the RMS value of the in-phase component of the current._

**URI**: [cim:ActivePower](http://iec.ch/TC57/CIM100#ActivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePower
    click ActivePower href "/Models/Profiles/ShortCircuit/ConcreteClasses/ActivePower/"
    style ActivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AsynchronousMachine --> ActivePower : AsynchronousMachine.ratedMechanicalPower

        AsynchronousMachine
            click AsynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/AsynchronousMachine/"
            style AsynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower --> UnitMultiplier : ActivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePower --> UnitSymbol : ActivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
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
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
