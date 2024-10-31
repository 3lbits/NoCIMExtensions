# Structure

_Construction holding assets such as conductors, transformers, switchgear, etc._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [nc-no:Structure](http://cim4.eu/ns/nc-no#Structure)<br />
**Type**: Class

```mermaid
classDiagram
    class Structure
    click Structure href "/AviationObstacle/Structure/"
    style Structure fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        Structure <|-- OverheadStructure : inherits
            click Structure href "/AviationObstacle/Structure/"
            style Structure rx:10,ry:10

        OverheadStructure
            click OverheadStructure href "/AviationObstacle/OverheadStructure/"
            style OverheadStructure rx:10,ry:10

        LocationResource <|-- Structure : inherits
            click LocationResource href "/AviationObstacle/LocationResource/"
            style LocationResource rx:10,ry:10

        ElementResource <|-- LocationResource : inherits
            click ElementResource href "/AviationObstacle/ElementResource/"
            style ElementResource rx:10,ry:10

        IdentifiedObject <|-- ElementResource : inherits
            click IdentifiedObject href "/AviationObstacle/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- LocationResource : inherits
            click Feature href "/AviationObstacle/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10


        StructureDeployment --> Structure : StructureDeployment.ACLineSegmentSpan

        StructureDeployment
            click StructureDeployment href "/AviationObstacle/StructureDeployment/"
            style StructureDeployment fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        LocationResource --> LocationMethodKind : LocationResource.locationMethod

        LocationMethodKind
            click LocationMethodKind href "/AviationObstacle/LocationMethodKind/"
            style LocationMethodKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        Structure : Structure.height
        LocationResource : PowerSystemResource.locationMethod
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ElementResource](ElementResource.md)
        * [LocationResource](LocationResource.md)
            * **Structure**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| height | [nc-no:Structure.height](http://cim4.eu/ns/nc-no#Structure.height) | 0..1 Length | Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. | direct |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 LocationMethodKind | Method used to derive geographical location for this entity. | LocationResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
