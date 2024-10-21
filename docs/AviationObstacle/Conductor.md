# Conductor


_Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:Conductor](https://cim.ucaiug.io/ns#Conductor)<br />
**Type**: Class




```mermaid
 classDiagram
    class Conductor
    click Conductor href "../Conductor"
      ConductingEquipment <|-- Conductor
        click ConductingEquipment href "../ConductingEquipment"
      

      Conductor <|-- ACLineSegment
        click ACLineSegment href "../ACLineSegment"
      
      
      Conductor : IdentifiedObject.description
        
      Conductor : hasGeometry
        
          Conductor --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      Conductor : PowerSystemResource.locationMethodKind
        
          Conductor --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      Conductor : IdentifiedObject.mRID
        
      Conductor : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * **Conductor**
                    * [ACLineSegment](ACLineSegment.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | [PowerSystemResource](PowerSystemResource.md) |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:Conductor |
| native | this:Conductor |




