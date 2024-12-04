# Conductor

_Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:Conductor](https://cim.ucaiug.io/ns#Conductor)<br />
**Type**: Class

```mermaid
classDiagram
    class Conductor
    click Conductor href "/Models/Profiles/AviationObstacle/AbstractClasses/Conductor/"
    style Conductor fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        Conductor <|-- ACLineSegment : inherits
            click Conductor href "/Models/Profiles/AviationObstacle/AbstractClasses/Conductor/"
            style Conductor rx:10,ry:10

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegment/"
            style ACLineSegment rx:10,ry:10

        ConductingEquipment <|-- Conductor : inherits
            click ConductingEquipment href "/Models/Profiles/AviationObstacle/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment rx:10,ry:10

        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/AviationObstacle/AbstractClasses/Equipment/"
            style Equipment rx:10,ry:10

        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/AviationObstacle/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource rx:10,ry:10

        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10


        PowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        PowerSystemResource : PowerSystemResource.locationMethodKind
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * **Conductor**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
