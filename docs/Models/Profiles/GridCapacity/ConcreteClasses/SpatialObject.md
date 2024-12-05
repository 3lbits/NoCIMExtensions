# SpatialObject

_A spatial object is a physical object that has a location in space. It may have a geometric representation to describe its shape and position._

**URI**: [geo:SpatialObject](http://www.opengis.net/ont/geosparql#SpatialObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SpatialObject
    click SpatialObject href "/Models/Profiles/GridCapacity/ConcreteClasses/SpatialObject/"
    style SpatialObject fill:#006400,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SpatialObject <|-- Feature : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature
            click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



```

## Inheritance
* **SpatialObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
