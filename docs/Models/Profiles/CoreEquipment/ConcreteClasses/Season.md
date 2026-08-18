# Season

_A specified time period of the year._

**URI**: [cim:Season](http://iec.ch/TC57/CIM100#Season)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Season
    click Season href "/Models/Profiles/CoreEquipment/ConcreteClasses/Season/"
    style Season fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Season : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Season --> SeasonDayTypeSchedule : Season.SeasonDayTypeSchedules

        SeasonDayTypeSchedule
            click SeasonDayTypeSchedule href "/Models/Profiles/CoreEquipment/AbstractClasses/SeasonDayTypeSchedule/"
            style SeasonDayTypeSchedule fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SeasonDayTypeSchedule --> Season : SeasonDayTypeSchedule.Season

        SeasonDayTypeSchedule
            click SeasonDayTypeSchedule href "/Models/Profiles/CoreEquipment/AbstractClasses/SeasonDayTypeSchedule/"
            style SeasonDayTypeSchedule fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Season : Season.endDate
        Season : Season.startDate
        Season : Season.SeasonDayTypeSchedules
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * **Season**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| endDate | [cim:Season.endDate](http://iec.ch/TC57/CIM100#Season.endDate) | No cardinality available date | Date season ends. | direct |
| startDate | [cim:Season.startDate](http://iec.ch/TC57/CIM100#Season.startDate) | No cardinality available date | Date season starts. | direct |
| SeasonDayTypeSchedules | [cim:Season.SeasonDayTypeSchedules](http://iec.ch/TC57/CIM100#Season.SeasonDayTypeSchedules) | No cardinality available SeasonDayTypeSchedule | Schedules that use this Season. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
