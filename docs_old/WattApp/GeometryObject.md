# GeometryObject

_An object that represents a jsonld compound to support value, type and language._

**URI**: [No URI available](No URI available)<br />
**Type**: Class

```mermaid
classDiagram
    class GeometryObject
    click GeometryObject href "/WattApp/GeometryObject/"
    style GeometryObject fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10


        Geometry --> GeometryObject : Geometry.asGeoJSON

        Geometry
            click Geometry href "/WattApp/Geometry/"
            style Geometry fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


```

## Inheritance
* **GeometryObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | No URI available | 0..1 string | A string representing the GeoJSON object, typically serialized as a string. | direct |
| type | No URI available | 0..1 string | The type of the GeoJSON object, e.g., geo:geoJSONLiteral. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
