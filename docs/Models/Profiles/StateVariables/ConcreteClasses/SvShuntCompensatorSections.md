# SvShuntCompensatorSections

_State variable for the number of sections in service for a shunt compensator._

**URI**: [cim:SvShuntCompensatorSections](http://iec.ch/TC57/CIM100#SvShuntCompensatorSections)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SvShuntCompensatorSections
    click SvShuntCompensatorSections href "/Models/Profiles/StateVariables/ConcreteClasses/SvShuntCompensatorSections/"
    style SvShuntCompensatorSections fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvShuntCompensatorSections --> ShuntCompensator : SvShuntCompensatorSections.ShuntCompensator

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/StateVariables/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ShuntCompensator --> SvShuntCompensatorSections : ShuntCompensator.SvShuntCompensatorSections

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/StateVariables/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SvShuntCompensatorSections : SvShuntCompensatorSections.ShuntCompensator
        SvShuntCompensatorSections : SvShuntCompensatorSections.sections
```

## Inheritance
* **SvShuntCompensatorSections**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ShuntCompensator | [cim:SvShuntCompensatorSections.ShuntCompensator](http://iec.ch/TC57/CIM100#SvShuntCompensatorSections.ShuntCompensator) | No cardinality available ShuntCompensator | The shunt compensator for which the state applies. | direct |
| sections | [cim:SvShuntCompensatorSections.sections](http://iec.ch/TC57/CIM100#SvShuntCompensatorSections.sections) | No cardinality available float | The number of sections in service as a continuous variable. The attribute shall be a positive value or zero. To get integer value scale with ShuntCompensator.bPerSection. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
