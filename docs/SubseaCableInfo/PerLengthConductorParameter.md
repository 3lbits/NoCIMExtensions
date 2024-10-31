# PerLengthConductorParameter

_Common type for per-length electrical catalogues describing line parameters._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:PerLengthConductorParameter](http://iec.ch/TC57/CIM-generic#PerLengthConductorParameter)<br />
**Type**: Class

```mermaid
classDiagram
    class PerLengthConductorParameter
    click PerLengthConductorParameter href "../PerLengthConductorParameter"
    style PerLengthConductorParameter fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        PerLengthConductorParameter <|-- PerLengthImpedance : inherits
            click PerLengthConductorParameter href "../PerLengthConductorParameter"
            style PerLengthConductorParameter rx:10,ry:10

        PerLengthImpedance
            click PerLengthImpedance href "../PerLengthImpedance"
            style PerLengthImpedance rx:10,ry:10

        IdentifiedObject <|-- PerLengthConductorParameter : inherits
            click IdentifiedObject href "../IdentifiedObject"
            style IdentifiedObject rx:10,ry:10

        PerLengthConductorParameter --> ConductorInfo : PerLengthConductorParameter.ConductorInfo

        ConductorInfo
            click ConductorInfo href "../ConductorInfo"
            style ConductorInfo fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        PerLengthConductorParameter : PerLengthConductorParameter.mRID
        PerLengthConductorParameter : PerLengthConductorParameter.ConductorInfo
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **PerLengthConductorParameter**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:PerLengthConductorParameter.mRID](http://iec.ch/TC57/CIM-generic#PerLengthConductorParameter.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| ConductorInfo | [cim:PerLengthConductorParameter.ConductorInfo](http://iec.ch/TC57/CIM-generic#PerLengthConductorParameter.ConductorInfo) | 0..1 ConductorInfo | No description available | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)