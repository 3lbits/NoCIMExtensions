# ConnectivityNodeContainer

_A base class for all objects that may contain connectivity nodes or topological nodes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConnectivityNodeContainer](https://cim.ucaiug.io/ns#ConnectivityNodeContainer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ConnectivityNodeContainer
    click ConnectivityNodeContainer href "/Models/Profiles/GridCapacity/AbstractClasses/ConnectivityNodeContainer/"
    style ConnectivityNodeContainer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNodeContainer <|-- EquipmentContainer : inherits

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/GridCapacity/AbstractClasses/EquipmentContainer/"
            style EquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/Models/Profiles/GridCapacity/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/GridCapacity/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
            style Feature fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303



        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/GridCapacity/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/GridCapacity/AbstractClasses/PowerSystemResource/)
        * **ConnectivityNodeContainer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](/Models/Profiles/GridCapacity/ConcreteClasses/LanguageObject/) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
