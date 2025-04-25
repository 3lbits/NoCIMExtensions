# PowerSystemResource

_A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:PowerSystemResource](https://cim.ucaiug.io/ns#PowerSystemResource)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PowerSystemResource
    click PowerSystemResource href "/Models/Profiles/AviationObstacle/AbstractClasses/PowerSystemResource/"
    style PowerSystemResource fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- Equipment : inherits

        Equipment
            click Equipment href "/Models/Profiles/AviationObstacle/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303


        PowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource : PowerSystemResource.locationMethodKind
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/)
    * **PowerSystemResource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
