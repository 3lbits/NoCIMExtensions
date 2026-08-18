# SvPowerFlow

_State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive._

**URI**: [cim:SvPowerFlow](http://iec.ch/TC57/CIM100#SvPowerFlow)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SvPowerFlow
    click SvPowerFlow href "/Models/Profiles/StateVariables/ConcreteClasses/SvPowerFlow/"
    style SvPowerFlow fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvPowerFlow --> Terminal : SvPowerFlow.Terminal

        Terminal
            click Terminal href "/Models/Profiles/StateVariables/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> SvPowerFlow : Terminal.SvPowerFlow

        Terminal
            click Terminal href "/Models/Profiles/StateVariables/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SvPowerFlow : SvPowerFlow.p
        SvPowerFlow : SvPowerFlow.q
        SvPowerFlow : SvPowerFlow.Terminal
```

## Inheritance
* **SvPowerFlow**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| p | [cim:SvPowerFlow.p](http://iec.ch/TC57/CIM100#SvPowerFlow.p) | No cardinality available ActivePower | The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. | direct |
| q | [cim:SvPowerFlow.q](http://iec.ch/TC57/CIM100#SvPowerFlow.q) | No cardinality available ReactivePower | The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. | direct |
| Terminal | [cim:SvPowerFlow.Terminal](http://iec.ch/TC57/CIM100#SvPowerFlow.Terminal) | No cardinality available Terminal | The terminal associated with the power flow state variable. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
