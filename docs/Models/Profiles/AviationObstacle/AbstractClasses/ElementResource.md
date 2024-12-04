# ElementResource

_An element of an asset that has no electrical characteristic._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ElementResource](https://cim.ucaiug.io/ns#ElementResource)<br />
**Type**: Class

```mermaid
classDiagram
    class ElementResource
    click ElementResource href "/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/"
    style ElementResource fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ElementResource <|-- LocationResource : inherits
            click ElementResource href "/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/"
            style ElementResource rx:10,ry:10

        LocationResource
            click LocationResource href "/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/"
            style LocationResource rx:10,ry:10

        IdentifiedObject <|-- ElementResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- LocationResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10



        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **ElementResource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
