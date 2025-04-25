# Zone

_Defines a system base voltage which is referenced._

**URI**: [nc-no:Zone](http://cim4.eu/ns/nc-no#Zone)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Zone
    click Zone href "/Models/Profiles/AviationObstacle/ConcreteClasses/Zone/"
    style Zone fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        LocationResource <|-- Zone : inherits
            click LocationResource href "/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/"
            style LocationResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ElementResource <|-- LocationResource : inherits
            click ElementResource href "/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/"
            style ElementResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ElementResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature <|-- LocationResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303


        Zone --> ZoneStateKind : Zone.state

        ZoneStateKind
            click ZoneStateKind href "/Models/Profiles/AviationObstacle/Enumerations/ZoneStateKind/"
            style ZoneStateKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Zone --> ZoneKind : Zone.zoneKind

        ZoneKind
            click ZoneKind href "/Models/Profiles/AviationObstacle/Enumerations/ZoneKind/"
            style ZoneKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        LocationResource --> LocationMethodKind : LocationResource.locationMethod

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Zone : Zone.state
        Zone : Zone.zoneKind
        LocationResource : PowerSystemResource.locationMethod
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/)
    * [ElementResource](/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/)
        * [LocationResource](/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/)
            * **Zone**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| state | [cim:Zone.state](https://cim.ucaiug.io/ns#Zone.state) | 0..1 ZoneStateKind | Current state of zone. | direct |
| zoneKind | [cim:Zone.zoneKind](https://cim.ucaiug.io/ns#Zone.zoneKind) | 0..1 ZoneKind | Kind of zone. | direct |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 LocationMethodKind | Method used to derive geographical location for this entity. | LocationResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
