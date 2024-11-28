# Terminal

_An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes._

**URI**: [cim:Terminal](https://cim.ucaiug.io/ns#Terminal)<br />
**Type**: Class

```mermaid
classDiagram
    class Terminal
    click Terminal href "/WattApp/Terminal/"
    style Terminal fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ACDCTerminal <|-- Terminal : inherits
            click ACDCTerminal href "/WattApp/ACDCTerminal/"
            style ACDCTerminal rx:10,ry:10

        Terminal
            click Terminal href "/WattApp/Terminal/"
            style Terminal rx:10,ry:10

        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Terminal --> ConnectivityNode : Terminal.ConnectivityNode

        ConnectivityNode
            click ConnectivityNode href "/WattApp/ConnectivityNode/"
            style ConnectivityNode fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        TransformerEnd --> Terminal : TransformerEnd.Terminal

        TransformerEnd
            click TransformerEnd href "/WattApp/TransformerEnd/"
            style TransformerEnd fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        Measurement --> ACDCTerminal : Measurement.ACDCTerminal

        Measurement
            click Measurement href "/WattApp/Measurement/"
            style Measurement fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        Terminal : Terminal.ConnectivityNode
        ACDCTerminal : ACDCTerminal.sequenceNumber
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ACDCTerminal](ACDCTerminal.md)
        * **Terminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ConnectivityNode | [cim:Terminal.ConnectivityNode](https://cim.ucaiug.io/ns#Terminal.ConnectivityNode) | 0..1 ConnectivityNode | The connectivity node to which this terminal connects with zero impedance. | direct |
| sequenceNumber | [cim:ACDCTerminal.sequenceNumber](https://cim.ucaiug.io/ns#ACDCTerminal.sequenceNumber) | 0..1 Integer | The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order. The first terminal is the "starting point" for a two terminal branch. | ACDCTerminal |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
