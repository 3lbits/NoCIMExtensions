# ConductingEquipment


_The parts of the AC power system that are designed to carry current or that are conductively connected through terminals._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:ConductingEquipment](https://cim.ucaiug.io/ns#ConductingEquipment)<br />
**Type**: Class




```mermaid
 classDiagram
    class ConductingEquipment
    click ConductingEquipment href "../ConductingEquipment"
      Equipment <|-- ConductingEquipment
        click Equipment href "../Equipment"
      

      ConductingEquipment <|-- Conductor
        click Conductor href "../Conductor"
      
      
      ConductingEquipment : IdentifiedObject.description
        
      ConductingEquipment : hasGeometry
        
          ConductingEquipment --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      ConductingEquipment : PowerSystemResource.locationMethodKind
        
          ConductingEquipment --> LocationMethodKind : PowerSystemResource.locationMethodKind
          click LocationMethodKind href "../LocationMethodKind"
        
      ConductingEquipment : IdentifiedObject.mRID
        
      ConductingEquipment : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * [Equipment](Equipment.md)
            * **ConductingEquipment**
                * [Conductor](Conductor.md)



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
| self | cim:ConductingEquipment |
| native | this:ConductingEquipment |




