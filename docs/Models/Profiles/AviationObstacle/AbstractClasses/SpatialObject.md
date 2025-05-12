# SpatialObject

_A spatial object is a physical object that has a location in space. It may have a geometric representation to describe its shape and position._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SpatialObject
    click SpatialObject href "/Models/Profiles/AviationObstacle/AbstractClasses/SpatialObject/"
    style SpatialObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SpatialObject <|-- Feature : inherits

        Feature
            click Feature href "/Models/Profiles/AviationObstacle/AbstractClasses/Feature/"
            style Feature fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SpatialObject <|-- Geometry : inherits

        Geometry
            click Geometry href "/Models/Profiles/AviationObstacle/AbstractClasses/Geometry/"
            style Geometry fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



```

## Inheritance
* **SpatialObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
