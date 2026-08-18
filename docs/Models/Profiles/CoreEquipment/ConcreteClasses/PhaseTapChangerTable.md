# PhaseTapChangerTable

_Describes a tabular curve for how the phase angle difference and impedance varies with the tap step._

**URI**: [cim:PhaseTapChangerTable](http://iec.ch/TC57/CIM100#PhaseTapChangerTable)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PhaseTapChangerTable
    click PhaseTapChangerTable href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTable/"
    style PhaseTapChangerTable fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PhaseTapChangerTable : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerTable --> PhaseTapChangerTablePoint : PhaseTapChangerTable.PhaseTapChangerTablePoint

        PhaseTapChangerTablePoint
            click PhaseTapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTablePoint/"
            style PhaseTapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PhaseTapChangerTable --> PhaseTapChangerTabular : PhaseTapChangerTable.PhaseTapChangerTabular

        PhaseTapChangerTabular
            click PhaseTapChangerTabular href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTabular/"
            style PhaseTapChangerTabular fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerTablePoint --> PhaseTapChangerTable : PhaseTapChangerTablePoint.PhaseTapChangerTable

        PhaseTapChangerTablePoint
            click PhaseTapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTablePoint/"
            style PhaseTapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerTabular --> PhaseTapChangerTable : PhaseTapChangerTabular.PhaseTapChangerTable

        PhaseTapChangerTabular
            click PhaseTapChangerTabular href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTabular/"
            style PhaseTapChangerTabular fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PhaseTapChangerTable : PhaseTapChangerTable.PhaseTapChangerTablePoint
        PhaseTapChangerTable : PhaseTapChangerTable.PhaseTapChangerTabular
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * **PhaseTapChangerTable**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| PhaseTapChangerTablePoint | [cim:PhaseTapChangerTable.PhaseTapChangerTablePoint](http://iec.ch/TC57/CIM100#PhaseTapChangerTable.PhaseTapChangerTablePoint) | No cardinality available PhaseTapChangerTablePoint | The points of this table. | direct |
| PhaseTapChangerTabular | [cim:PhaseTapChangerTable.PhaseTapChangerTabular](http://iec.ch/TC57/CIM100#PhaseTapChangerTable.PhaseTapChangerTabular) | No cardinality available PhaseTapChangerTabular | The phase tap changers to which this phase tap table applies. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
