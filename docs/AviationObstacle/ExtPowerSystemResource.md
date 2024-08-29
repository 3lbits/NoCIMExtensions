# ExtPowerSystemResource


_Extends PowerSystemResource_




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [nc-no:PowerSystemResource](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource)<br />
**Type**: Class




```mermaid
 classDiagram
    class ExtPowerSystemResource
    click ExtPowerSystemResource href "../ExtPowerSystemResource"
      IdentifiedObject <|-- ExtPowerSystemResource
        click IdentifiedObject href "../IdentifiedObject"
      

      ExtPowerSystemResource <|-- PowerSystemResource
        click PowerSystemResource href "../PowerSystemResource"
      
      
      ExtPowerSystemResource : IdentifiedObject.description
        
      ExtPowerSystemResource : PowerSystemResource.locationMethodKind
        
          ExtPowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      ExtPowerSystemResource : IdentifiedObject.mRID
        
      ExtPowerSystemResource : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **ExtPowerSystemResource**
        * [PowerSystemResource](PowerSystemResource.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:PowerSystemResource |
| native | this:ExtPowerSystemResource |




