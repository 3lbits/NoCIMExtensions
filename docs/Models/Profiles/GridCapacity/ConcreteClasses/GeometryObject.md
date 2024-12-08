# GeometryObject

_An object that represents a jsonld compound to support value, type and language._

**URI**: [No URI available](No URI available)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class GeometryObject
    click GeometryObject href "/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject/"
    style GeometryObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Geometry --> GeometryObject : Geometry.asGeoJSON

        Geometry
            click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
            style Geometry fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


```

## Inheritance
* **GeometryObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | No URI available | 0..1 string | A string representing the GeoJSON object, typically serialized as a string. | direct |
| type | No URI available | 0..1 string | The type of the GeoJSON object, e.g., geo:geoJSONLiteral. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
