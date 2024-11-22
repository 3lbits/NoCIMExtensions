# PowerTransformer

_An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
A power transformer may be composed of separate transformer tanks that need not be identical.
A power transformer can be modelled with or without tanks and is intended for use in both balanced and unbalanced representations. A power transformer typically has two terminals, but may have one (grounding), three or more terminals.
The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead._

**URI**: [cim:PowerTransformer](https://cim.ucaiug.io/ns#PowerTransformer)<br />
**Type**: Class

```mermaid
classDiagram
    class PowerTransformer
    click PowerTransformer href "/WattApp/PowerTransformer/"
    style PowerTransformer fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ConductingEquipment <|-- PowerTransformer : inherits
            click ConductingEquipment href "/WattApp/ConductingEquipment/"
            style ConductingEquipment rx:10,ry:10

        PowerTransformer
            click PowerTransformer href "/WattApp/PowerTransformer/"
            style PowerTransformer rx:10,ry:10

        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/WattApp/Equipment/"
            style Equipment rx:10,ry:10

        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/WattApp/PowerSystemResource/"
            style PowerSystemResource rx:10,ry:10

        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/WattApp/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10

        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        EquipmentContainer
            click EquipmentContainer href "/WattApp/EquipmentContainer/"
            style EquipmentContainer fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        PowerTransformerEnd --> PowerTransformer : PowerTransformerEnd.PowerTransformer

        PowerTransformerEnd
            click PowerTransformerEnd href "/WattApp/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        Equipment : Equipment.EquipmentContainer
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * **PowerTransformer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| EquipmentContainer | [cim:Equipment.EquipmentContainer](https://cim.ucaiug.io/ns#Equipment.EquipmentContainer) | 0..1 EquipmentContainer | Container of this equipment. | Equipment |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
