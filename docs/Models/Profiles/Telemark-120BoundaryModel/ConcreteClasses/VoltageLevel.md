# VoltageLevel

_A collection of equipment at one common system voltage forming a switchgear. The equipment typically consists of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these._

**URI**: [cim:VoltageLevel](https://cim.ucaiug.io/ns#VoltageLevel)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class VoltageLevel
    click VoltageLevel href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/VoltageLevel/"
    style VoltageLevel fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EquipmentContainer <|-- VoltageLevel : inherits
            click EquipmentContainer href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConnectivityNodeContainer <|-- EquipmentContainer : inherits
            click ConnectivityNodeContainer href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/Models/Profiles/Telemark-120BoundaryModel/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/Telemark-120BoundaryModel/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltageLevel --> BaseVoltage : VoltageLevel.BaseVoltage

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        VoltageLevel --> Substation : VoltageLevel.Substation

        Substation
            click Substation href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/Substation/"
            style Substation fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> ConnectivityNodeContainer : ConnectivityNode.ConnectivityNodeContainer

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        VoltageLevel : VoltageLevel.BaseVoltage
        VoltageLevel : VoltageLevel.Substation
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120BoundaryModel/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/Telemark-120BoundaryModel/AbstractClasses/PowerSystemResource/)
        * [ConnectivityNodeContainer](/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/ConnectivityNodeContainer/)
            * [EquipmentContainer](/Models/Profiles/Telemark-120BoundaryModel/ConcreteClasses/EquipmentContainer/)
                * **VoltageLevel**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| BaseVoltage | [cim:VoltageLevel.BaseVoltage](https://cim.ucaiug.io/ns#VoltageLevel.BaseVoltage) | 0..1 BaseVoltage | Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. | direct |
| Substation | [cim:VoltageLevel.Substation](https://cim.ucaiug.io/ns#VoltageLevel.Substation) | 0..1 Substation | The substation of the voltage level. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/BoundaryModel/1.0](https://ap-no.cim4.eu/BoundaryModel/1.0)
