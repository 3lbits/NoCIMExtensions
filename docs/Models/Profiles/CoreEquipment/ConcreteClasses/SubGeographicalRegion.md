# SubGeographicalRegion

_A subset of a geographical region of a power system network model._

**URI**: [cim:SubGeographicalRegion](http://iec.ch/TC57/CIM100#SubGeographicalRegion)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SubGeographicalRegion
    click SubGeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubGeographicalRegion/"
    style SubGeographicalRegion fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- SubGeographicalRegion : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SubGeographicalRegion --> DCLine : SubGeographicalRegion.DCLines

        DCLine
            click DCLine href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLine/"
            style DCLine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        SubGeographicalRegion --> GeographicalRegion : SubGeographicalRegion.Region

        GeographicalRegion
            click GeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeographicalRegion/"
            style GeographicalRegion fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        SubGeographicalRegion --> Line : SubGeographicalRegion.Lines

        Line
            click Line href "/Models/Profiles/CoreEquipment/ConcreteClasses/Line/"
            style Line fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        SubGeographicalRegion --> Substation : SubGeographicalRegion.Substations

        Substation
            click Substation href "/Models/Profiles/CoreEquipment/ConcreteClasses/Substation/"
            style Substation fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCLine --> SubGeographicalRegion : DCLine.Region

        DCLine
            click DCLine href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLine/"
            style DCLine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeographicalRegion --> SubGeographicalRegion : GeographicalRegion.Regions

        GeographicalRegion
            click GeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeographicalRegion/"
            style GeographicalRegion fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Line --> SubGeographicalRegion : Line.Region

        Line
            click Line href "/Models/Profiles/CoreEquipment/ConcreteClasses/Line/"
            style Line fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Substation --> SubGeographicalRegion : Substation.Region

        Substation
            click Substation href "/Models/Profiles/CoreEquipment/ConcreteClasses/Substation/"
            style Substation fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SubGeographicalRegion : SubGeographicalRegion.DCLines
        SubGeographicalRegion : SubGeographicalRegion.Region
        SubGeographicalRegion : SubGeographicalRegion.Lines
        SubGeographicalRegion : SubGeographicalRegion.Substations
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * **SubGeographicalRegion**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCLines | [cim:SubGeographicalRegion.DCLines](http://iec.ch/TC57/CIM100#SubGeographicalRegion.DCLines) | No cardinality available DCLine | The DC lines in this sub-geographical region. | direct |
| Region | [cim:SubGeographicalRegion.Region](http://iec.ch/TC57/CIM100#SubGeographicalRegion.Region) | No cardinality available GeographicalRegion | The geographical region which this sub-geographical region is within. | direct |
| Lines | [cim:SubGeographicalRegion.Lines](http://iec.ch/TC57/CIM100#SubGeographicalRegion.Lines) | No cardinality available Line | The lines within the sub-geographical region. | direct |
| Substations | [cim:SubGeographicalRegion.Substations](http://iec.ch/TC57/CIM100#SubGeographicalRegion.Substations) | No cardinality available Substation | The substations in this sub-geographical region. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
