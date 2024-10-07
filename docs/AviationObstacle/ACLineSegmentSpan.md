# ACLineSegmentSpan


_The part of a segment line between two consecutive points of support._





**URI**: [nc-no:ACLineSegmentSpan](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan)<br />
**Type**: Class




```mermaid
 classDiagram
    class ACLineSegmentSpan
    click ACLineSegmentSpan href "../ACLineSegmentSpan"
      PowerSystemResource <|-- ACLineSegmentSpan
        click PowerSystemResource href "../PowerSystemResource"
      
      ACLineSegmentSpan : ACLineSegmentSpan.ACLineSegment
        
          ACLineSegmentSpan --> ACLineSegment : ACLineSegmentSpan.ACLineSegment
          click ACLineSegment href "../ACLineSegment"
        
      ACLineSegmentSpan : ACLineSegmentSpan.aviationObstacleLightingKind
        
          ACLineSegmentSpan --> AviationObstacleLightingKind : ACLineSegmentSpan.aviationObstacleLightingKind
          click AviationObstacleLightingKind href "../AviationObstacleLightingKind"
        
      ACLineSegmentSpan : ACLineSegmentSpan.aviationObstacleMarkingKind
        
          ACLineSegmentSpan --> AviationObstacleMarkingKind : ACLineSegmentSpan.aviationObstacleMarkingKind
          click AviationObstacleMarkingKind href "../AviationObstacleMarkingKind"
        
      ACLineSegmentSpan : IdentifiedObject.description
        
      ACLineSegmentSpan : hasGeometry
        
          ACLineSegmentSpan --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      ACLineSegmentSpan : PowerSystemResource.locationMethodKind
        
          ACLineSegmentSpan --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      ACLineSegmentSpan : ACLineSegmentSpan.maxHeight
        
      ACLineSegmentSpan : ACLineSegmentSpan.maxWidth
        
      ACLineSegmentSpan : IdentifiedObject.mRID
        
      ACLineSegmentSpan : IdentifiedObject.name
        
      ACLineSegmentSpan : ACLineSegmentSpan.spanWireLength
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * **ACLineSegmentSpan**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| aviationObstacleLightingKind | [nc-no:ACLineSegmentSpan.aviationObstacleLightingKind](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.aviationObstacleLightingKind) | 0..1 <br />  [AviationObstacleLightingKind](AviationObstacleLightingKind.md)  | The kind of aviation obstacle lighting associated with the ACLineSegmentSpan | direct |
| aviationObstacleMarkingKind | [nc-no:ACLineSegmentSpan.aviationObstacleMarkingKind](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.aviationObstacleMarkingKind) | 0..1 <br />  [AviationObstacleMarkingKind](AviationObstacleMarkingKind.md)  | The kind of aviation obstacle marking associated with the ACLineSegmentSpan | direct |
| maxWidth | [nc-no:ACLineSegmentSpan.maxWidth](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.maxWidth) | 0..1 <br />  [Length](Length.md)  | Max width of the AC Line Segment Span | direct |
| maxHeight | [nc-no:ACLineSegmentSpan.maxHeight](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.maxHeight) | 0..1 <br />  [Length](Length.md)  | Max height of the AC Line Segment Span | direct |
| spanWireLength | [nc-no:ACLineSegmentSpan.spanWireLength](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.spanWireLength) | 0..1 <br />  [Length](Length.md)  | Length of the AC Line Segment Span | direct |
| ACLineSegment | [nc-no:ACLineSegmentSpan.ACLineSegment](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan.ACLineSegment) | 0..* <br />  [ACLineSegment](ACLineSegment.md)  | The associated AC Line Segment | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | [PowerSystemResource](PowerSystemResource.md) |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ACLineSegment](ACLineSegment.md) | ACLineSegmentSpan | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |
| [ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | ACLineSegmentSpan | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |
| [Container](Container.md) | ACLineSegmentSpan | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:ACLineSegmentSpan |
| native | this:ACLineSegmentSpan |




