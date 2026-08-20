# SvSwitch

_State variable for switch._

**URI**: [cim:SvSwitch](http://iec.ch/TC57/CIM100#SvSwitch)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SvSwitch
    click SvSwitch href "/Models/Profiles/StateVariables/ConcreteClasses/SvSwitch/"
    style SvSwitch fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvSwitch --> Switch : SvSwitch.Switch

        Switch
            click Switch href "/Models/Profiles/StateVariables/ConcreteClasses/Switch/"
            style Switch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch --> SvSwitch : Switch.SvSwitch

        Switch
            click Switch href "/Models/Profiles/StateVariables/ConcreteClasses/Switch/"
            style Switch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SvSwitch : SvSwitch.open
        SvSwitch : SvSwitch.Switch
```

## Inheritance
* **SvSwitch**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| open | [cim:SvSwitch.open](http://iec.ch/TC57/CIM100#SvSwitch.open) | No cardinality available boolean | The attribute tells if the computed state of the switch is considered open. | direct |
| Switch | [cim:SvSwitch.Switch](http://iec.ch/TC57/CIM100#SvSwitch.Switch) | No cardinality available Switch | The switch associated with the switch state. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
