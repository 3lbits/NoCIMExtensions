# Feature

_Defines a system base voltage which is referenced._

**URI**: [geo:Feature](http://www.opengis.net/ont/geosparql#Feature)<br />
**Type**: Class

```mermaid
classDiagram
    class Feature
    click Feature href "../Feature"
    style Feature fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        SpatialObject <|-- Feature : inherits
            click SpatialObject href "../SpatialObject"
            style SpatialObject rx:10,ry:10

        Feature
            click Feature href "../Feature"
            style Feature rx:10,ry:10

        PowerSystemResource --|> Feature : inherits
            click PowerSystemResource href "../PowerSystemResource"
            style PowerSystemResource fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10

        Feature --> Geometry : Feature.hasGeometry

        Geometry
            click Geometry href "../Geometry"
            style Geometry fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        Feature : hasGeometry
```

## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Feature**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 | Geometric representation of the spatial object. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
