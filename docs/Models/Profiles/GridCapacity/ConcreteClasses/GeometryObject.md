# GeometryObject

_An object that represents a jsonld compound to support value, type and language._

**URI**: [No URI available](No URI available)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class GeometryObject
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/GeometryObject.md
    click GeometryObject href "/Models/Profiles/WattApp/ConcreteClasses/GeometryObject/"
    style GeometryObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
    click GeometryObject href "/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject/"
    style GeometryObject fill:#006400,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject.md


        Geometry --> GeometryObject : Geometry.asGeoJSON

        Geometry
<<<<<<< HEAD:docs/Models/Profiles/WattApp/ConcreteClasses/GeometryObject.md
            click Geometry href "/Models/Profiles/WattApp/ConcreteClasses/Geometry/"
            style Geometry fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
=======
            click Geometry href "/Models/Profiles/GridCapacity/ConcreteClasses/Geometry/"
            style Geometry fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
>>>>>>> f7d5d7dc4d970b98fa060adac484ce9c06135a79:docs/Models/Profiles/GridCapacity/ConcreteClasses/GeometryObject.md


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
