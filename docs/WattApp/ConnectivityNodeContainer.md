# ConnectivityNodeContainer


_A base class for all objects that may contain connectivity nodes or topological nodes._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:ConnectivityNodeContainer](https://cim.ucaiug.io/ns#ConnectivityNodeContainer)<br />
**Type**: Class




```mermaid
 classDiagram
    class ConnectivityNodeContainer
    click ConnectivityNodeContainer href "../ConnectivityNodeContainer"
      PowerSystemResource <|-- ConnectivityNodeContainer
        click PowerSystemResource href "../PowerSystemResource"
      

      ConnectivityNodeContainer <|-- EquipmentContainer
        click EquipmentContainer href "../EquipmentContainer"
      
      
      ConnectivityNodeContainer : IdentifiedObject.description
        
      ConnectivityNodeContainer : hasGeometry
        
          ConnectivityNodeContainer --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      ConnectivityNodeContainer : IdentifiedObject.mRID
        
      ConnectivityNodeContainer : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
        * **ConnectivityNodeContainer**
            * [EquipmentContainer](EquipmentContainer.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:ConnectivityNodeContainer |
| native | this:ConnectivityNodeContainer |




