# Geometry

_Geometric representation details._

**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Geometry
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/Geometry.md
    click Geometry href "/Models/Profiles/WattApp/ConcreteClasses/Geometry/"
    style Geometry fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/Models/Profiles/WattApp/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
    click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
    style Geometry fill:#006400,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Geometry
            click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
            style SpatialObject fill:#00008B,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/Geometry.md

        Geometry --> GeometryObject : Geometry.asGeoJSON

        GeometryObject
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/Geometry.md
            click GeometryObject href "/Models/Profiles/WattApp/ConcreteClasses/GeometryObject/"
            style GeometryObject fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
            click GeometryObject href "/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject/"
            style GeometryObject fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/Geometry.md

        Feature --> Geometry : Feature.hasGeometry

        Feature
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/Geometry.md
            click Feature href "/Models/Profiles/WattApp/ConcreteClasses/Feature/"
            style Feature fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
            click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
            style Feature fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/Geometry.md


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
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
