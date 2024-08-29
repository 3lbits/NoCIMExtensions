# Conductor


_Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:Conductor](http://iec.ch/TC57/CIM100#Conductor)<br />
**Type**: Class




```mermaid
 classDiagram
    class Conductor
    click Conductor href "../Conductor"
      ConductingEquipment <|-- Conductor
        click ConductingEquipment href "../ConductingEquipment"
      

      Conductor <|-- ExtACLineSegment
        click ExtACLineSegment href "../ExtACLineSegment"
      
      
      Conductor : IdentifiedObject.description
        
      Conductor : PowerSystemResource.locationMethodKind
        
          Conductor --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      Conductor : IdentifiedObject.mRID
        
      Conductor : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ExtPowerSystemResource](ExtPowerSystemResource.md)
        * [PowerSystemResource](PowerSystemResource.md)
            * [Equipment](Equipment.md)
                * [ConductingEquipment](ConductingEquipment.md)
                    * **Conductor**
                        * [ExtACLineSegment](ExtACLineSegment.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethodKind) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Possible methods to derive geographical location | [ExtPowerSystemResource](ExtPowerSystemResource.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:Conductor |
| native | this:Conductor |




