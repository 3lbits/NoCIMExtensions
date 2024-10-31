# ACLineSegment


_A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.For symmetrical, transposed three phase lines, it is sufficient to use attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances.The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines may have slightly different BaseVoltage.nominalVoltages and variation is allowed. Larger voltage difference in general requires use of an equivalent branch._





**URI**: [cim:ACLineSegment](https://cim.ucaiug.io/ns#ACLineSegment)<br />
**Type**: Class




```mermaid
 classDiagram
    class ACLineSegment
    click ACLineSegment href "../ACLineSegment"
      Conductor <|-- ACLineSegment
        click Conductor href "../Conductor"
      
      ACLineSegment : ACLineSegment.ACLineSegmentSpan
        
          ACLineSegment --> ACLineSegmentSpan : ACLineSegment.ACLineSegmentSpan
          click ACLineSegmentSpan href "../ACLineSegmentSpan"
        
      ACLineSegment : IdentifiedObject.description
        
      ACLineSegment : hasGeometry
        
          ACLineSegment --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      ACLineSegment : PowerSystemResource.locationMethodKind
        
          ACLineSegment --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      ACLineSegment : IdentifiedObject.mRID
        
      ACLineSegment : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * [Conductor](Conductor.md)
                    * **ACLineSegment**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ACLineSegmentSpan | [nc-no:ACLineSegment.ACLineSegmentSpan](http://cim4.eu/ns/nc-no#ACLineSegment.ACLineSegmentSpan) | 0..* <br />  [ACLineSegmentSpan](ACLineSegmentSpan.md)  | The associated AC Line Segment | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | [PowerSystemResource](PowerSystemResource.md) |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ACLineSegmentSpan](ACLineSegmentSpan.md) | ACLineSegment | range | [ACLineSegment](ACLineSegment.md) |






## Comments

* - Each ACLineSegment is required to have an association to a BaseVoltage. The association to Line is not required.- Using the EquipmentContainer association, an ACLineSegment can only be contained by a Line, but the association to Line is not required.

## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:ACLineSegment |
| native | this:ACLineSegment |




