# Geometry


_Geometric representation details._





**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class




```mermaid
 classDiagram
    class Geometry
    click Geometry href "../Geometry"
      SpatialObject <|-- Geometry
        click SpatialObject href "../SpatialObject"
      
      Geometry : asGeoJSON
        
      
```





## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Geometry**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 <br />  string  | Geometric representation of the spatial object in GeoJSON format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Feature](Feature.md) | hasGeometry | range | [Geometry](Geometry.md) |
| [PowerSystemResource](PowerSystemResource.md) | hasGeometry | range | [Geometry](Geometry.md) |
| [ConnectivityNodeContainer](ConnectivityNodeContainer.md) | hasGeometry | range | [Geometry](Geometry.md) |
| [EquipmentContainer](EquipmentContainer.md) | hasGeometry | range | [Geometry](Geometry.md) |
| [Feeder](Feeder.md) | hasGeometry | range | [Geometry](Geometry.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geo:Geometry |
| native | this:Geometry |




