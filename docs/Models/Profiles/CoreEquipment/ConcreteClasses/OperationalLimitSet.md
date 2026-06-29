# OperationalLimitSet

_A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set._

**URI**: [cim:OperationalLimitSet](http://iec.ch/TC57/CIM100#OperationalLimitSet)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class OperationalLimitSet
    click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
    style OperationalLimitSet fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- OperationalLimitSet : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> ACDCTerminal : OperationalLimitSet.Terminal

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        OperationalLimitSet --> Equipment : OperationalLimitSet.Equipment

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        OperationalLimitSet --> OperationalLimit : OperationalLimitSet.OperationalLimitValue

        OperationalLimit
            click OperationalLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimit/"
            style OperationalLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCTerminal --> OperationalLimitSet : ACDCTerminal.OperationalLimitSet

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Equipment --> OperationalLimitSet : Equipment.OperationalLimitSet

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit --> OperationalLimitSet : OperationalLimit.OperationalLimitSet

        OperationalLimit
            click OperationalLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimit/"
            style OperationalLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        OperationalLimitSet : OperationalLimitSet.Terminal
        OperationalLimitSet : OperationalLimitSet.Equipment
        OperationalLimitSet : OperationalLimitSet.OperationalLimitValue
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * **OperationalLimitSet**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Terminal | [cim:OperationalLimitSet.Terminal](http://iec.ch/TC57/CIM100#OperationalLimitSet.Terminal) | No cardinality available ACDCTerminal | The terminal where the operational limit set apply. | direct |
| Equipment | [cim:OperationalLimitSet.Equipment](http://iec.ch/TC57/CIM100#OperationalLimitSet.Equipment) | No cardinality available Equipment | The equipment to which the limit set applies. | direct |
| OperationalLimitValue | [cim:OperationalLimitSet.OperationalLimitValue](http://iec.ch/TC57/CIM100#OperationalLimitSet.OperationalLimitValue) | No cardinality available OperationalLimit | Values of equipment limits. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
