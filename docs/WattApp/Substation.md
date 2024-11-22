# Substation

_A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics._

**URI**: [cim:Substation](https://cim.ucaiug.io/ns#Substation)<br />
**Type**: Class

```mermaid
classDiagram
    class Substation
    click Substation href "/WattApp/Substation/"
    style Substation fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        EquipmentContainer <|-- Substation : inherits
            click EquipmentContainer href "/WattApp/EquipmentContainer/"
            style EquipmentContainer rx:10,ry:10

        Substation
            click Substation href "/WattApp/Substation/"
            style Substation rx:10,ry:10

        ConnectivityNodeContainer <|-- EquipmentContainer : inherits
            click ConnectivityNodeContainer href "/WattApp/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer rx:10,ry:10

        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/WattApp/PowerSystemResource/"
            style PowerSystemResource rx:10,ry:10

        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Feature <|-- PowerSystemResource : inherits
            click Feature href "/WattApp/Feature/"
            style Feature fill:#FFA500,stroke:#333,stroke-width:2px,rx:10,ry:10


        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        Equipment
            click Equipment href "/WattApp/Equipment/"
            style Equipment fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [ConnectivityNodeContainer](ConnectivityNodeContainer.md)
            * [EquipmentContainer](EquipmentContainer.md)
                * **Substation**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
