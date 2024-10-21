# Feeder


_A collection of equipment for organizational purposes, used for grouping distribution resources. The organization a feeder does not necessarily reflect connectivity or current operation state._





**URI**: [cim:Feeder](https://cim.ucaiug.io/ns#Feeder)<br />
**Type**: Class




```mermaid
 classDiagram
    class Feeder
    click Feeder href "../Feeder"
      EquipmentContainer <|-- Feeder
        click EquipmentContainer href "../EquipmentContainer"
      
      Feeder : IdentifiedObject.description
        
      Feeder : hasGeometry
        
          Feeder --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      Feeder : IdentifiedObject.mRID
        
      Feeder : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * [ConnectivityNodeContainer](ConnectivityNodeContainer.md)
            * [EquipmentContainer](EquipmentContainer.md)
                * **Feeder**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapacitySchedule](CapacitySchedule.md) | Feeder | range | [Feeder](Feeder.md) |
| [Container](Container.md) | Feeder | range | [Feeder](Feeder.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:Feeder |
| native | this:Feeder |




