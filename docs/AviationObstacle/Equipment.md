# Equipment


_The parts of a power system that are physical devices, electronic or mechanical._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:Equipment](http://iec.ch/TC57/CIM100#Equipment)<br />
**Type**: Class




```mermaid
 classDiagram
    class Equipment
    click Equipment href "../Equipment"
      PowerSystemResource <|-- Equipment
        click PowerSystemResource href "../PowerSystemResource"
      

      Equipment <|-- ConductingEquipment
        click ConductingEquipment href "../ConductingEquipment"
      
      
      Equipment : asGeoJSON
        
      Equipment : asGML
        
      Equipment : asWKT
        
      Equipment : IdentifiedObject.description
        
      Equipment : PowerSystemResource.locationMethodKind
        
          Equipment --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      Equipment : IdentifiedObject.mRID
        
      Equipment : IdentifiedObject.name
        
      
```





## Inheritance
* [PowerSystemResource](PowerSystemResource.md) [ [IdentifiedObject](IdentifiedObject.md) [SpatialObject](SpatialObject.md)]
    * **Equipment**
        * [ConductingEquipment](ConductingEquipment.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | [PowerSystemResource](PowerSystemResource.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |
| asWKT | [geo:asWKT](http://www.opengis.net/ont/geosparql#asWKT) | 0..1 <br />  string  | Geometric representation of the spatial object in WKT format | [SpatialObject](SpatialObject.md) |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 <br />  string  | Geometric representation of the spatial object in GeoJSON format | [SpatialObject](SpatialObject.md) |
| asGML | [geo:asGML](http://www.opengis.net/ont/geosparql#asGML) | 0..1 <br />  string  | Geometric representation of the spatial object in GML format | [SpatialObject](SpatialObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:Equipment |
| native | this:Equipment |




