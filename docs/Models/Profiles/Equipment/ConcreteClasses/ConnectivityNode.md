# ConnectivityNode

_Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance._

**URI**: [cim:ConnectivityNode](https://cim.ucaiug.io/ns#ConnectivityNode)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ConnectivityNode
    click ConnectivityNode href "/Models/Profiles/Equipment/ConcreteClasses/ConnectivityNode/"
    style ConnectivityNode fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ConnectivityNode : inherits
            click IdentifiedObject href "/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> ConnectivityNodeContainer : ConnectivityNode.ConnectivityNodeContainer

        ConnectivityNodeContainer
            click ConnectivityNodeContainer href "/Models/Profiles/Equipment/AbstractClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> ConnectivityNode : Terminal.ConnectivityNode

        Terminal
            click Terminal href "/Models/Profiles/Equipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ConnectivityNode : ConnectivityNode.ConnectivityNodeContainer
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/)
    * **ConnectivityNode**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ConnectivityNodeContainer | [cim:ConnectivityNode.ConnectivityNodeContainer](https://cim.ucaiug.io/ns#ConnectivityNode.ConnectivityNodeContainer) | 0..1 ConnectivityNodeContainer | Container of this connectivity node. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
