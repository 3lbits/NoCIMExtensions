# ACDCTerminal

_None_

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ACDCTerminal](https://cim.ucaiug.io/ns#ACDCTerminal)<br />
**Type**: Class

```mermaid
classDiagram
    class ACDCTerminal
    click ACDCTerminal href "/WattApp/ACDCTerminal/"
    style ACDCTerminal fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACDCTerminal <|-- Terminal : inherits
            click ACDCTerminal href "/WattApp/ACDCTerminal/"
            style ACDCTerminal rx:10,ry:10

        Terminal
            click Terminal href "/WattApp/Terminal/"
            style Terminal rx:10,ry:10

        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10


        Measurement --> ACDCTerminal : Measurement.ACDCTerminal

        Measurement
            click Measurement href "/WattApp/Measurement/"
            style Measurement fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **ACDCTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
