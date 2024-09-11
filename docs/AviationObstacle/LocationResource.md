# LocationResource


_A spatial entity. LocationResource serves a similar purpose as PowerSystemResource but for non-electrical entites of interest to electrical utilities._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [nc-no:LocationResource](https://ap-no.cim4.eu/AviationObstacle/1.0#LocationResource)<br />
**Type**: Class




```mermaid
 classDiagram
    class LocationResource
    click LocationResource href "../LocationResource"
      ElementResource <|-- LocationResource
        click ElementResource href "../ElementResource"
      SpatialObject <|-- LocationResource
        click SpatialObject href "../SpatialObject"
      

      LocationResource <|-- Structure
        click Structure href "../Structure"
      LocationResource <|-- Zone
        click Zone href "../Zone"
      
      
      LocationResource : asGeoJSON
        
      LocationResource : asGML
        
      LocationResource : asWKT
        
      LocationResource : IdentifiedObject.description
        
      LocationResource : PowerSystemResource.locationMethod
        
          LocationResource --> LocationMethodKind : PowerSystemResource.locationMethod
          click LocationMethodKind href "../LocationMethodKind"
        
      LocationResource : IdentifiedObject.mRID
        
      LocationResource : IdentifiedObject.name
        
      
```





## Inheritance
* **LocationResource** [ [ElementResource](ElementResource.md) [SpatialObject](SpatialObject.md)]
    * [Structure](Structure.md)
    * [Zone](Zone.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethod) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Method used to derive geographical location for this entity | direct |
| asWKT | [geo:asWKT](http://www.opengis.net/ont/geosparql#asWKT) | 0..1 <br />  string  | Geometric representation of the spatial object in WKT format | [SpatialObject](SpatialObject.md) |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 <br />  string  | Geometric representation of the spatial object in GeoJSON format | [SpatialObject](SpatialObject.md) |
| asGML | [geo:asGML](http://www.opengis.net/ont/geosparql#asGML) | 0..1 <br />  string  | Geometric representation of the spatial object in GML format | [SpatialObject](SpatialObject.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:LocationResource |
| native | this:LocationResource |



