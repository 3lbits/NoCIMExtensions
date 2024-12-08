# Geometry

_Geometric representation details._

**URI**: [geo:Geometry](http://www.opengis.net/ont/geosparql#Geometry)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Geometry
    click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
    style Geometry fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        SpatialObject <|-- Geometry : inherits
            click SpatialObject href "/Models/Profiles/GridCapacity/ConcreteClasses/SpatialObject/"
            style SpatialObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Geometry --> GeometryObject : Geometry.asGeoJSON

        GeometryObject
            click GeometryObject href "/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject/"
            style GeometryObject fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Feature --> Geometry : Feature.hasGeometry

        Feature
            click Feature href "/Models/Profiles/GridCapacity/ConcreteClasses/Feature/"
            style Feature fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


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
