# ElementResource


_An element of an asset that has no electrical characteristic._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:ElementResource](http://iec.ch/TC57/CIM100#ElementResource)<br />
**Type**: Class




```mermaid
 classDiagram
    class ElementResource
    click ElementResource href "../ElementResource"
      IdentifiedObject <|-- ElementResource
        click IdentifiedObject href "../IdentifiedObject"
      

      ElementResource <|-- LocationResource
        click LocationResource href "../LocationResource"
      
      
      ElementResource : IdentifiedObject.description
        
      ElementResource : IdentifiedObject.mRID
        
      ElementResource : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **ElementResource**
        * [LocationResource](LocationResource.md) [ [SpatialObject](SpatialObject.md)]



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:ElementResource |
| native | this:ElementResource |




