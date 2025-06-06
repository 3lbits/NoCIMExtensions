# Feature

_Defines a system base voltage which is referenced._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [geo:Feature](http://www.opengis.net/ont/geosparql#Feature)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Feature
    click Feature href "/Models/Profiles/GridCapacity/AbstractClasses/Feature/"
    style Feature fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        SpatialObject <|-- Feature : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/AbstractClasses/SpatialObject/"
            style SpatialObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --|> Feature : inherits
            click PowerSystemResource href "/Models/Profiles/GridCapacity/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303

        Feature --> Geometry : Feature.hasGeometry

        Geometry
            click Geometry href "/Models/Profiles/GridCapacity/AbstractClasses/Geometry/"
            style Geometry fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Feature : hasGeometry
```

## Inheritance
* [SpatialObject](/Models/Profiles/GridCapacity/AbstractClasses/SpatialObject/)
    * **Feature**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 Geometry | Geometric representation of the spatial object. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
