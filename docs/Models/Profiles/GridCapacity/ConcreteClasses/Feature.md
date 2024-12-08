# Feature

_Defines a system base voltage which is referenced._

**URI**: [geo:Feature](http://www.opengis.net/ont/geosparql#Feature)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Feature
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/Feature.md
    click Feature href "/Models/Profiles/WattApp/ConcreteClasses/Feature/"
    style Feature fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        SpatialObject <|-- Feature : inherits
            click SpatialObject href "/Models/Profiles/WattApp/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --|> Feature : inherits
            click PowerSystemResource href "/Models/Profiles/WattApp/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#F2EBE2,stroke:#333,stroke-width:2px,rx:10,ry:10,color:#8A0303
=======
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
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/Feature.md

        Feature --> Geometry : Feature.hasGeometry

        Geometry
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/Feature.md
            click Geometry href "/Models/Profiles/WattApp/ConcreteClasses/Geometry/"
            style Geometry fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
            click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
            style Geometry fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/Feature.md


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
