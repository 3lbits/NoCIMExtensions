# NonlinearShuntCompensatorPoint

_A non linear shunt compensator bank or section admittance value. The number of NonlinearShuntCompenstorPoint instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections. ShuntCompensator.sections shall only be set to one of the NonlinearShuntCompenstorPoint.sectionNumber. There is no interpolation between NonlinearShuntCompenstorPoint-s._

**URI**: [cim:NonlinearShuntCompensatorPoint](http://iec.ch/TC57/CIM100#NonlinearShuntCompensatorPoint)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class NonlinearShuntCompensatorPoint
    click NonlinearShuntCompensatorPoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensatorPoint/"
    style NonlinearShuntCompensatorPoint fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensatorPoint --> NonlinearShuntCompensator : NonlinearShuntCompensatorPoint.NonlinearShuntCompensator

        NonlinearShuntCompensator
            click NonlinearShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensator/"
            style NonlinearShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        NonlinearShuntCompensatorPoint --> Susceptance : NonlinearShuntCompensatorPoint.b

        Susceptance
            click Susceptance href "/Models/Profiles/CoreEquipment/ConcreteClasses/Susceptance/"
            style Susceptance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        NonlinearShuntCompensatorPoint --> Conductance : NonlinearShuntCompensatorPoint.g

        Conductance
            click Conductance href "/Models/Profiles/CoreEquipment/ConcreteClasses/Conductance/"
            style Conductance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensator --> NonlinearShuntCompensatorPoint : NonlinearShuntCompensator.NonlinearShuntCompensatorPoints

        NonlinearShuntCompensator
            click NonlinearShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensator/"
            style NonlinearShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        NonlinearShuntCompensatorPoint : NonlinearShuntCompensatorPoint.NonlinearShuntCompensator
        NonlinearShuntCompensatorPoint : NonlinearShuntCompensatorPoint.b
        NonlinearShuntCompensatorPoint : NonlinearShuntCompensatorPoint.g
        NonlinearShuntCompensatorPoint : NonlinearShuntCompensatorPoint.sectionNumber
```

## Inheritance
* **NonlinearShuntCompensatorPoint**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| NonlinearShuntCompensator | [cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator](http://iec.ch/TC57/CIM100#NonlinearShuntCompensatorPoint.NonlinearShuntCompensator) | No cardinality available NonlinearShuntCompensator | Non-linear shunt compensator owning this point. | direct |
| b | [cim:NonlinearShuntCompensatorPoint.b](http://iec.ch/TC57/CIM100#NonlinearShuntCompensatorPoint.b) | No cardinality available Susceptance | Positive sequence shunt (charging) susceptance per section. | direct |
| g | [cim:NonlinearShuntCompensatorPoint.g](http://iec.ch/TC57/CIM100#NonlinearShuntCompensatorPoint.g) | No cardinality available Conductance | Positive sequence shunt (charging) conductance per section. | direct |
| sectionNumber | [cim:NonlinearShuntCompensatorPoint.sectionNumber](http://iec.ch/TC57/CIM100#NonlinearShuntCompensatorPoint.sectionNumber) | No cardinality available integer | The number of the section. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
