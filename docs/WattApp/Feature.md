# Feature


_Defines a system base voltage which is referenced._





**URI**: [geo:Feature](http://www.opengis.net/ont/geosparql#Feature)<br />
**Type**: Class




```mermaid
 classDiagram
    class Feature
    click Feature href "../Feature"
      SpatialObject <|-- Feature
        click SpatialObject href "../SpatialObject"
      

      Feature <|-- PowerSystemResource
        click PowerSystemResource href "../PowerSystemResource"
      
      
      Feature : hasGeometry
        
          Feature --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      
```





## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Feature**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geo:Feature |
| native | this:Feature |




