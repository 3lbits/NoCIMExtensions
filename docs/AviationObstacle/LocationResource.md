# LocationResource


_A spatial entity. LocationResource serves a similar purpose as PowerSystemResource but for non-electrical entites of interest to electrical utilities._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [nc-no:LocationResource](http://cim4.eu/ns/nc-no#LocationResource)<br />
**Type**: Class




```mermaid
 classDiagram
    class LocationResource
    click LocationResource href "../LocationResource"
      Feature <|-- LocationResource
        click Feature href "../Feature"
      ElementResource <|-- LocationResource
        click ElementResource href "../ElementResource"
      

      LocationResource <|-- Structure
        click Structure href "../Structure"
      LocationResource <|-- Zone
        click Zone href "../Zone"
      
      
      LocationResource : IdentifiedObject.description
        
      LocationResource : hasGeometry
        
          LocationResource --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      LocationResource : PowerSystemResource.locationMethod
        
          LocationResource --> LocationMethodKind : PowerSystemResource.locationMethod
          click LocationMethodKind href "../LocationMethodKind"
        
      LocationResource : IdentifiedObject.mRID
        
      LocationResource : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ElementResource](ElementResource.md)
        * **LocationResource** [ [Feature](Feature.md)]
            * [Structure](Structure.md)
            * [Zone](Zone.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Method used to derive geographical location for this entity | direct |
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
| self | nc-no:LocationResource |
| native | this:LocationResource |




