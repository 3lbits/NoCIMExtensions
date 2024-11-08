# Geometry

_Geometric representation details._

**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class

```mermaid
classDiagram
    class Geometry
    click Geometry href "/WattApp/Geometry/"
    style Geometry fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/WattApp/SpatialObject/"
            style SpatialObject rx:10,ry:10

        Geometry
            click Geometry href "/WattApp/Geometry/"
            style Geometry rx:10,ry:10

        Geometry --> GeometryObject : Geometry.asGeoJSON

        GeometryObject
            click GeometryObject href "/WattApp/GeometryObject/"
            style GeometryObject fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        Feature --> Geometry : Feature.hasGeometry

        Feature
            click Feature href "/WattApp/Feature/"
            style Feature fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        Geometry : asGeoJSON
```

## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Geometry**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| asGeoJSON | [geo:asGeoJSON](http://www.opengis.net/ont/geosparql#asGeoJSON) | 0..1 GeometryObject | Geometric representation of the spatial object in GeoJSON format. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
