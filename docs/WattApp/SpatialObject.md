# SpatialObject

_A spatial object is a physical object that has a location in space. It may have a geometric representation to describe its shape and position._

**URI**: [geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject)<br />
**Type**: Class

```mermaid
classDiagram
    class SpatialObject
    click SpatialObject href "../SpatialObject"
    style SpatialObject fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        SpatialObject <|-- Feature : inherits
            click SpatialObject href "../SpatialObject"
            style SpatialObject rx:10,ry:10

        Feature
            click Feature href "../Feature"
            style Feature rx:10,ry:10



```

## Inheritance
* **SpatialObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
