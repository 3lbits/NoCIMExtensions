# MeasurementValue

_The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:MeasurementValue](https://cim.ucaiug.io/ns#MeasurementValue)<br />
**Type**: Class

```mermaid
classDiagram
    class MeasurementValue
    click MeasurementValue href "/WattApp/MeasurementValue/"
    style MeasurementValue fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        MeasurementValue <|-- AnalogValue : inherits
            click MeasurementValue href "/WattApp/MeasurementValue/"
            style MeasurementValue rx:10,ry:10

        AnalogValue
            click AnalogValue href "/WattApp/AnalogValue/"
            style AnalogValue rx:10,ry:10

        IOPoint <|-- MeasurementValue : inherits
            click IOPoint href "/WattApp/IOPoint/"
            style IOPoint rx:10,ry:10

        IdentifiedObject <|-- IOPoint : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10



        MeasurementValue : MeasurementValue.timeStamp
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [IOPoint](IOPoint.md)
        * **MeasurementValue**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| timeStamp | [cim:MeasurementValue.timeStamp](https://cim.ucaiug.io/ns#MeasurementValue.timeStamp) | 0..1 DateTime |  | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
