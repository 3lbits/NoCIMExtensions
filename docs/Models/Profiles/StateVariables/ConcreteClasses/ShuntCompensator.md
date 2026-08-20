# ShuntCompensator

_A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor. A negative value for bPerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied._

**URI**: [cim:ShuntCompensator](http://iec.ch/TC57/CIM100#ShuntCompensator)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ShuntCompensator
    click ShuntCompensator href "/Models/Profiles/StateVariables/ConcreteClasses/ShuntCompensator/"
    style ShuntCompensator fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ShuntCompensator --> SvShuntCompensatorSections : ShuntCompensator.SvShuntCompensatorSections

        SvShuntCompensatorSections
            click SvShuntCompensatorSections href "/Models/Profiles/StateVariables/ConcreteClasses/SvShuntCompensatorSections/"
            style SvShuntCompensatorSections fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvShuntCompensatorSections --> ShuntCompensator : SvShuntCompensatorSections.ShuntCompensator

        SvShuntCompensatorSections
            click SvShuntCompensatorSections href "/Models/Profiles/StateVariables/ConcreteClasses/SvShuntCompensatorSections/"
            style SvShuntCompensatorSections fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ShuntCompensator : ShuntCompensator.SvShuntCompensatorSections
```

## Inheritance
* **ShuntCompensator**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SvShuntCompensatorSections | [cim:ShuntCompensator.SvShuntCompensatorSections](http://iec.ch/TC57/CIM100#ShuntCompensator.SvShuntCompensatorSections) | No cardinality available SvShuntCompensatorSections | The state for the number of shunt compensator sections in service. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
