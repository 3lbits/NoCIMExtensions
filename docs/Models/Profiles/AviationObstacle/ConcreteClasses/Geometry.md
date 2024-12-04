# Geometry

_Geometric representation details._

**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class

```mermaid
classDiagram
    class Geometry
    click Geometry href "/Models/Profiles/AviationObstacle/ConcreteClasses/Geometry/"
    style Geometry fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/Models/Profiles/AviationObstacle/ConcreteClasses/SpatialObject/"
            style SpatialObject rx:10,ry:10

        Geometry
            click Geometry href "/Models/Profiles/AviationObstacle/ConcreteClasses/Geometry/"
            style Geometry rx:10,ry:10


        Feature --> Geometry : Feature.hasGeometry

        Feature
            click Feature href "/Models/Profiles/AviationObstacle/ConcreteClasses/Feature/"
            style Feature fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        Geometry : asWKT
        Geometry : asGeoJSON
        Geometry : asGML
```

## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Geometry**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| asWKT | [geo:asWKT](http://www.opengis.net/ont/geosparql#asWKT) | 0..1 string | Geometric representation of the spatial object in WKT format. | direct |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 string | Geometric representation of the spatial object in GeoJSON format. | direct |
| asGML | [geo:asGML](http://www.opengis.net/ont/geosparql#asGML) | 0..1 string | Geometric representation of the spatial object in GML format. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
