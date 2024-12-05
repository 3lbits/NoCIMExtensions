# Feature

_Defines a system base voltage which is referenced._

**URI**: [geo:Feature](http://www.opengis.net/ont/geosparql#Feature)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Feature
    click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
    style Feature fill:#006400,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SpatialObject <|-- Feature : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature
            click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --|> Feature : inherits
            click PowerSystemResource href "/Models/Profiles/GridCapacity/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#FF8C00,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature --> Geometry : Feature.hasGeometry

        Geometry
            click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
            style Geometry fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Feature : hasGeometry
```

## Inheritance
* [SpatialObject](SpatialObject.md)
    * **Feature**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 Geometry | Geometric representation of the spatial object. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
