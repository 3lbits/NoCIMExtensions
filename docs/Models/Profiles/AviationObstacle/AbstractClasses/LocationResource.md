# LocationResource

_A spatial entity. LocationResource serves a similar purpose as PowerSystemResource but for non-electrical entites of interest to electrical utilities._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [nc-no:LocationResource](http://cim4.eu/ns/nc-no#LocationResource)<br />
**Type**: Class

```mermaid
classDiagram
    class LocationResource
    click LocationResource href "/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/"
    style LocationResource fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        LocationResource <|-- Structure : inherits
            click LocationResource href "/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/"
            style LocationResource rx:10,ry:10

        Structure
            click Structure href "/Models/Profiles/AviationObstacle/AbstractClasses/Structure/"
            style Structure rx:10,ry:10

        ElementResource <|-- LocationResource : inherits
            click ElementResource href "/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/"
            style ElementResource rx:10,ry:10

        IdentifiedObject <|-- ElementResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- LocationResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10


        LocationResource --> LocationMethodKind : LocationResource.locationMethod

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        LocationResource : PowerSystemResource.locationMethod
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ElementResource](ElementResource.md)
        * **LocationResource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 LocationMethodKind | Method used to derive geographical location for this entity. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
