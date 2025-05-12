# OverheadStructure

_An overhead structure is an element of an electric transmission or distribution system that supports the overhead conductors and associated equipment used for the transmission of electricity._

**URI**: [nc-no:OverheadStructure](http://cim4.eu/ns/nc-no#OverheadStructure)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class OverheadStructure
    click OverheadStructure href "/Models/Profiles/AviationObstacle/ConcreteClasses/OverheadStructure/"
    style OverheadStructure fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Structure <|-- OverheadStructure : inherits
            click Structure href "/Models/Profiles/AviationObstacle/AbstractClasses/Structure/"
            style Structure fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        LocationResource <|-- Structure : inherits
            click LocationResource href "/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/"
            style LocationResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ElementResource <|-- LocationResource : inherits
            click ElementResource href "/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/"
            style ElementResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ElementResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature <|-- LocationResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/AbstractClasses/Feature/"
            style Feature fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303


        StructureDeployment --> Structure : StructureDeployment.ACLineSegmentSpan

        StructureDeployment
            click StructureDeployment href "/Models/Profiles/AviationObstacle/ConcreteClasses/StructureDeployment/"
            style StructureDeployment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OverheadStructure --> AviationObstacleLightingKind : OverheadStructure.aviationObstacleLightingKind

        AviationObstacleLightingKind
            click AviationObstacleLightingKind href "/Models/Profiles/AviationObstacle/Enumerations/AviationObstacleLightingKind/"
            style AviationObstacleLightingKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        OverheadStructure --> AviationObstacleMarkingKind : OverheadStructure.aviationObstacleMarkingKind

        AviationObstacleMarkingKind
            click AviationObstacleMarkingKind href "/Models/Profiles/AviationObstacle/Enumerations/AviationObstacleMarkingKind/"
            style AviationObstacleMarkingKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        LocationResource --> LocationMethodKind : LocationResource.locationMethod

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OverheadStructure : OverheadStructure.aviationObstacleLightingKind
        OverheadStructure : OverheadStructure.aviationObstacleMarkingKind
        OverheadStructure : OverheadStructure.maxHeight
        Structure : Structure.height
        LocationResource : PowerSystemResource.locationMethod
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/)
    * [ElementResource](/Models/Profiles/AviationObstacle/AbstractClasses/ElementResource/)
        * [LocationResource](/Models/Profiles/AviationObstacle/AbstractClasses/LocationResource/)
            * [Structure](/Models/Profiles/AviationObstacle/AbstractClasses/Structure/)
                * **OverheadStructure**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| aviationObstacleLightingKind | [nc-no:OverheadStructure.aviationObstacleLightingKind](http://cim4.eu/ns/nc-no#OverheadStructure.aviationObstacleLightingKind) | 0..1 AviationObstacleLightingKind | Kind of lighting on the structure. | direct |
| aviationObstacleMarkingKind | [nc-no:OverheadStructure.aviationObstacleMarkingKind](http://cim4.eu/ns/nc-no#OverheadStructure.aviationObstacleMarkingKind) | 0..1 AviationObstacleMarkingKind | Kind of marking on the structure. | direct |
| maxHeight | [nc-no:OverheadStructure.maxHeight](http://cim4.eu/ns/nc-no#OverheadStructure.maxHeight) | 0..1 Length | The length of the longest distance from the ground to the highest point on the structure. If f.ex. the structure is located in a steep slope, the distance from the top of the structure to the ground may vary. | direct |
| height | [nc-no:Structure.height](http://cim4.eu/ns/nc-no#Structure.height) | 0..1 Length | Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. | Structure |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 LocationMethodKind | Method used to derive geographical location for this entity. | LocationResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
