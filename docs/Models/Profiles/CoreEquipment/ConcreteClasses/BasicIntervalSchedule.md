# BasicIntervalSchedule

_Schedule of values at points in time._

**URI**: [cim:BasicIntervalSchedule](http://iec.ch/TC57/CIM100#BasicIntervalSchedule)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class BasicIntervalSchedule
    click BasicIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/BasicIntervalSchedule/"
    style BasicIntervalSchedule fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BasicIntervalSchedule <|-- RegularIntervalSchedule : inherits

        RegularIntervalSchedule
            click RegularIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegularIntervalSchedule/"
            style RegularIntervalSchedule fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- BasicIntervalSchedule : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        BasicIntervalSchedule --> UnitSymbol : BasicIntervalSchedule.value1Unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        BasicIntervalSchedule --> UnitSymbol : BasicIntervalSchedule.value2Unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BasicIntervalSchedule : BasicIntervalSchedule.startTime
        BasicIntervalSchedule : BasicIntervalSchedule.value1Unit
        BasicIntervalSchedule : BasicIntervalSchedule.value2Unit
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * **BasicIntervalSchedule**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| startTime | [cim:BasicIntervalSchedule.startTime](http://iec.ch/TC57/CIM100#BasicIntervalSchedule.startTime) | No cardinality available date | The time for the first time point.  The value can be a time of day, not a specific date. | direct |
| value1Unit | [cim:BasicIntervalSchedule.value1Unit](http://iec.ch/TC57/CIM100#BasicIntervalSchedule.value1Unit) | No cardinality available UnitSymbol | Value1 units of measure. | direct |
| value2Unit | [cim:BasicIntervalSchedule.value2Unit](http://iec.ch/TC57/CIM100#BasicIntervalSchedule.value2Unit) | No cardinality available UnitSymbol | Value2 units of measure. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
