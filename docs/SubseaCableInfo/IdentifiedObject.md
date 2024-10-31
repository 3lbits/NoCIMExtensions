# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM-generic#IdentifiedObject)<br />
**Type**: Class

```mermaid
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "../IdentifiedObject"
    style IdentifiedObject fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        IdentifiedObject <|-- AssetInfo : inherits
            click IdentifiedObject href "../IdentifiedObject"
            style IdentifiedObject rx:10,ry:10

        AssetInfo
            click AssetInfo href "../AssetInfo"
            style AssetInfo rx:10,ry:10



        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | direct |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)