# ACLineSegmentSpan

_The part of a segment line between two consecutive points of support._

**URI**: [nc-no:ACLineSegmentSpan](http://cim4.eu/ns/nc-no#ACLineSegmentSpan)<br />
**Type**: Class

```mermaid
classDiagram
    class ACLineSegmentSpan
    click ACLineSegmentSpan href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegmentSpan/"
    style ACLineSegmentSpan fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        PowerSystemResource <|-- ACLineSegmentSpan : inherits
            click PowerSystemResource href "/Models/Profiles/AviationObstacle/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource rx:10,ry:10

        ACLineSegmentSpan
            click ACLineSegmentSpan href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegmentSpan/"
            style ACLineSegmentSpan rx:10,ry:10

        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACLineSegmentSpan --> ACLineSegment : ACLineSegmentSpan.ACLineSegment

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACLineSegment --> ACLineSegmentSpan : ACLineSegment.ACLineSegmentSpan

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACLineSegmentSpanDeployment --> ACLineSegmentSpan : ACLineSegmentSpanDeployment.ACLineSegmentSpan

        ACLineSegmentSpanDeployment
            click ACLineSegmentSpanDeployment href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegmentSpanDeployment/"
            style ACLineSegmentSpanDeployment fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACLineSegmentSpan --> AviationObstacleLightingKind : ACLineSegmentSpan.aviationObstacleLightingKind

        AviationObstacleLightingKind
            click AviationObstacleLightingKind href "/Models/Profiles/AviationObstacle/Enumerations/AviationObstacleLightingKind/"
            style AviationObstacleLightingKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        ACLineSegmentSpan --> AviationObstacleMarkingKind : ACLineSegmentSpan.aviationObstacleMarkingKind

        AviationObstacleMarkingKind
            click AviationObstacleMarkingKind href "/Models/Profiles/AviationObstacle/Enumerations/AviationObstacleMarkingKind/"
            style AviationObstacleMarkingKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        PowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACLineSegmentSpan : ACLineSegmentSpan.aviationObstacleLightingKind
        ACLineSegmentSpan : ACLineSegmentSpan.aviationObstacleMarkingKind
        ACLineSegmentSpan : ACLineSegmentSpan.maxWidth
        ACLineSegmentSpan : ACLineSegmentSpan.maxHeight
        ACLineSegmentSpan : ACLineSegmentSpan.spanWireLength
        ACLineSegmentSpan : ACLineSegmentSpan.ACLineSegment
        PowerSystemResource : PowerSystemResource.locationMethodKind
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * **ACLineSegmentSpan**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| aviationObstacleLightingKind | [nc-no:ACLineSegmentSpan.aviationObstacleLightingKind](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.aviationObstacleLightingKind) | 0..1 AviationObstacleLightingKind | The kind of aviation obstacle lighting associated with the ACLineSegmentSpan. | direct |
| aviationObstacleMarkingKind | [nc-no:ACLineSegmentSpan.aviationObstacleMarkingKind](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.aviationObstacleMarkingKind) | 0..1 AviationObstacleMarkingKind | The kind of aviation obstacle marking associated with the ACLineSegmentSpan. | direct |
| maxWidth | [nc-no:ACLineSegmentSpan.maxWidth](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.maxWidth) | 0..1 Length | Max width of the AC Line Segment Span | direct |
| maxHeight | [nc-no:ACLineSegmentSpan.maxHeight](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.maxHeight) | 0..1 Length | Max height of the AC Line Segment Span | direct |
| spanWireLength | [nc-no:ACLineSegmentSpan.spanWireLength](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.spanWireLength) | 0..1 Length | Length of the AC Line Segment Span | direct |
| ACLineSegment | [nc-no:ACLineSegmentSpan.ACLineSegment](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.ACLineSegment) | 0..* ACLineSegment | The associated AC Line Segment | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
