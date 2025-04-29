# ConformLoadGroup

_A group of loads conforming to an allocation pattern._

**URI**: [cim:ConformLoadGroup](https://cim.ucaiug.io/ns#ConformLoadGroup)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ConformLoadGroup
    click ConformLoadGroup href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/ConformLoadGroup/"
    style ConformLoadGroup fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        LoadGroup <|-- ConformLoadGroup : inherits
            click LoadGroup href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/LoadGroup/"
            style LoadGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- LoadGroup : inherits
            click IdentifiedObject href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConformLoadGroup --> SubLoadArea : LoadGroup.SubLoadArea

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        LoadGroup --> SubLoadArea : LoadGroup.SubLoadArea

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConformLoad --> ConformLoadGroup : ConformLoad.LoadGroup

        ConformLoad
            click ConformLoad href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/ConformLoad/"
            style ConformLoad fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ConformLoadGroup : LoadGroup.SubLoadArea
        LoadGroup : LoadGroup.SubLoadArea
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/)
    * [LoadGroup](/Models/Profiles/Telemark-120Equipment/AbstractClasses/LoadGroup/)
        * **ConformLoadGroup**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SubLoadArea | [cim:LoadGroup.SubLoadArea](https://cim.ucaiug.io/ns#LoadGroup.SubLoadArea) | 0..1 SubLoadArea | The SubLoadArea where the Loadgroup belongs. | direct |
| SubLoadArea | [cim:LoadGroup.SubLoadArea](https://cim.ucaiug.io/ns#LoadGroup.SubLoadArea) | 0..1 SubLoadArea | The SubLoadArea where the Loadgroup belongs. | LoadGroup |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
