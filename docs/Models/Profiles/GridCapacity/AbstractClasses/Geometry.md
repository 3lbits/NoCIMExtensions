# Geometry

_Geometric representation details._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Geometry
    click Geometry href "/Models/Profiles/GridCapacity/AbstractClasses/Geometry/"
    style Geometry fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/AbstractClasses/SpatialObject/"
            style SpatialObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Feature --> Geometry : Feature.hasGeometry

        Feature
            click Feature href "/Models/Profiles/GridCapacity/AbstractClasses/Feature/"
            style Feature fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Geometry : asWKT
        Geometry : asGeoJSON
        Geometry : asGML
```

## Inheritance
* [SpatialObject](/Models/Profiles/GridCapacity/AbstractClasses/SpatialObject/)
    * **Geometry**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| asWKT | [geo:asWKT](http://www.opengis.net/ont/geosparql#asWKT) | 0..1 string | Geometric representation of the spatial object in WKT format. | direct |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 string | Geometric representation of the spatial object in GeoJSON format. | direct |
| asGML | [geo:asGML](http://www.opengis.net/ont/geosparql#asGML) | 0..1 string | Geometric representation of the spatial object in GML format. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
