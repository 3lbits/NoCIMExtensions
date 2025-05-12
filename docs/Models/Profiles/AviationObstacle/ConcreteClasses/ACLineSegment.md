# ACLineSegment

_A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.For symmetrical, transposed three phase lines, it is sufficient to use attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances.The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines may have slightly different BaseVoltage.nominalVoltages and variation is allowed. Larger voltage difference in general requires use of an equivalent branch._

**URI**: [cim:ACLineSegment](https://cim.ucaiug.io/ns#ACLineSegment)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ACLineSegment
    click ACLineSegment href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegment/"
    style ACLineSegment fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Conductor <|-- ACLineSegment : inherits
            click Conductor href "/Models/Profiles/AviationObstacle/AbstractClasses/Conductor/"
            style Conductor fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- Conductor : inherits
            click ConductingEquipment href "/Models/Profiles/AviationObstacle/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/AviationObstacle/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/AviationObstacle/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/Models/Profiles/AviationObstacle/AbstractClasses/Feature/"
            style Feature fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303

        ACLineSegment --> ACLineSegmentSpan : ACLineSegment.ACLineSegmentSpan

        ACLineSegmentSpan
            click ACLineSegmentSpan href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegmentSpan/"
            style ACLineSegmentSpan fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACLineSegmentSpan --> ACLineSegment : ACLineSegmentSpan.ACLineSegment

        ACLineSegmentSpan
            click ACLineSegmentSpan href "/Models/Profiles/AviationObstacle/ConcreteClasses/ACLineSegmentSpan/"
            style ACLineSegmentSpan fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/AviationObstacle/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACLineSegment : ACLineSegment.ACLineSegmentSpan
        PowerSystemResource : PowerSystemResource.locationMethodKind
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/AviationObstacle/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/AviationObstacle/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/AviationObstacle/AbstractClasses/ConductingEquipment/)
                * [Conductor](/Models/Profiles/AviationObstacle/AbstractClasses/Conductor/)
                    * **ACLineSegment**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ACLineSegmentSpan | [nc-no:ACLineSegment.ACLineSegmentSpan](http://cim4.eu/ns/nc-no#ACLineSegment.ACLineSegmentSpan) | 0..* ACLineSegmentSpan | The associated AC Line Segment | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
