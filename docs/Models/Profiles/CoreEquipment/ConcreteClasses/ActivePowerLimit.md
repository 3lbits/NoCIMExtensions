# ActivePowerLimit

_Limit on active power flow._

**URI**: [cim:ActivePowerLimit](http://iec.ch/TC57/CIM100#ActivePowerLimit)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ActivePowerLimit
    click ActivePowerLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ActivePowerLimit/"
    style ActivePowerLimit fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        OperationalLimit <|-- ActivePowerLimit : inherits
            click OperationalLimit href "/Models/Profiles/CoreEquipment/AbstractClasses/OperationalLimit/"
            style OperationalLimit fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- OperationalLimit : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit --> OperationalLimitSet : OperationalLimit.OperationalLimitSet

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        OperationalLimit --> OperationalLimitType : OperationalLimit.OperationalLimitType

        OperationalLimitType
            click OperationalLimitType href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitType/"
            style OperationalLimitType fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> OperationalLimit : OperationalLimitSet.OperationalLimitValue

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitType --> OperationalLimit : OperationalLimitType.OperationalLimit

        OperationalLimitType
            click OperationalLimitType href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitType/"
            style OperationalLimitType fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        ActivePowerLimit : ActivePowerLimit.normalValue
        OperationalLimit : OperationalLimit.OperationalLimitSet
        OperationalLimit : OperationalLimit.OperationalLimitType
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [OperationalLimit](/Models/Profiles/CoreEquipment/AbstractClasses/OperationalLimit/)
        * **ActivePowerLimit**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| normalValue | [cim:ActivePowerLimit.normalValue](http://iec.ch/TC57/CIM100#ActivePowerLimit.normalValue) | No cardinality available ActivePower | The normal value of active power limit. The attribute shall be a positive value or zero. | direct |
| OperationalLimitSet | [cim:OperationalLimit.OperationalLimitSet](http://iec.ch/TC57/CIM100#OperationalLimit.OperationalLimitSet) | No cardinality available OperationalLimitSet | The limit set to which the limit values belong. | OperationalLimit |
| OperationalLimitType | [cim:OperationalLimit.OperationalLimitType](http://iec.ch/TC57/CIM100#OperationalLimit.OperationalLimitType) | No cardinality available OperationalLimitType | The limit type associated with this limit. | OperationalLimit |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
