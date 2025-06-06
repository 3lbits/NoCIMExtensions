# Substation

_A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics._

**URI**: [cim:Substation](https://cim.ucaiug.io/ns#Substation)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Substation
    click Substation href "/Models/Profiles/BoundaryModel/ConcreteClasses/Substation/"
    style Substation fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EquipmentContainer <|-- Substation : inherits
            click EquipmentContainer href "/Models/Profiles/BoundaryModel/AbstractClasses/EquipmentContainer/"
            style EquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConnectivityNodeContainer <|-- EquipmentContainer : inherits
            click ConnectivityNodeContainer href "/Models/Profiles/BoundaryModel/AbstractClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/Models/Profiles/BoundaryModel/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/BoundaryModel/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Substation --> SubGeographicalRegion : Substation.Region

        SubGeographicalRegion : Not defined in profile

        SubGeographicalRegion
            style SubGeographicalRegion fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> ConnectivityNodeContainer : ConnectivityNode.ConnectivityNodeContainer

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/BoundaryModel/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltageLevel --> Substation : VoltageLevel.Substation

        VoltageLevel
            click VoltageLevel href "/Models/Profiles/BoundaryModel/ConcreteClasses/VoltageLevel/"
            style VoltageLevel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Substation : Substation.Region
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/BoundaryModel/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/BoundaryModel/AbstractClasses/PowerSystemResource/)
        * [ConnectivityNodeContainer](/Models/Profiles/BoundaryModel/AbstractClasses/ConnectivityNodeContainer/)
            * [EquipmentContainer](/Models/Profiles/BoundaryModel/AbstractClasses/EquipmentContainer/)
                * **Substation**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Region | [cim:Substation.Region](https://cim.ucaiug.io/ns#Substation.Region) | 0..1 SubGeographicalRegion | The SubGeographicalRegion containing the substation. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/BoundaryModel/1.0](https://ap-no.cim4.eu/BoundaryModel/1.0)
