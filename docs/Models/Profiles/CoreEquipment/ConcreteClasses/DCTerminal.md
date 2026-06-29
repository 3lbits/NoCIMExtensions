# DCTerminal

_An electrical connection point to generic DC conducting equipment._

**URI**: [cim:DCTerminal](http://iec.ch/TC57/CIM100#DCTerminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DCTerminal
    click DCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCTerminal/"
    style DCTerminal fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        DCBaseTerminal <|-- DCTerminal : inherits
            click DCBaseTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCBaseTerminal/"
            style DCBaseTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCTerminal <|-- DCBaseTerminal : inherits
            click ACDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCTerminal --> DCConductingEquipment : DCTerminal.DCConductingEquipment

        DCConductingEquipment
            click DCConductingEquipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCConductingEquipment/"
            style DCConductingEquipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        DCBaseTerminal --> DCNode : DCBaseTerminal.DCNode

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCTerminal --> OperationalLimitSet : ACDCTerminal.OperationalLimitSet

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCTerminal --> BusNameMarker : ACDCTerminal.BusNameMarker

        BusNameMarker
            click BusNameMarker href "/Models/Profiles/CoreEquipment/ConcreteClasses/BusNameMarker/"
            style BusNameMarker fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BusNameMarker --> ACDCTerminal : BusNameMarker.Terminal

        BusNameMarker
            click BusNameMarker href "/Models/Profiles/CoreEquipment/ConcreteClasses/BusNameMarker/"
            style BusNameMarker fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCConductingEquipment --> DCTerminal : DCConductingEquipment.DCTerminals

        DCConductingEquipment
            click DCConductingEquipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCConductingEquipment/"
            style DCConductingEquipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCNode --> DCBaseTerminal : DCNode.DCTerminals

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> ACDCTerminal : OperationalLimitSet.Terminal

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCTerminal : DCTerminal.DCConductingEquipment
        DCBaseTerminal : DCBaseTerminal.DCNode
        ACDCTerminal : ACDCTerminal.sequenceNumber
        ACDCTerminal : ACDCTerminal.OperationalLimitSet
        ACDCTerminal : ACDCTerminal.BusNameMarker
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * [ACDCTerminal](/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/)
        * [DCBaseTerminal](/Models/Profiles/CoreEquipment/ConcreteClasses/DCBaseTerminal/)
            * **DCTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCConductingEquipment | [cim:DCTerminal.DCConductingEquipment](http://iec.ch/TC57/CIM100#DCTerminal.DCConductingEquipment) | No cardinality available DCConductingEquipment | An DC  terminal belong to a DC conducting equipment. | direct |
| DCNode | [cim:DCBaseTerminal.DCNode](http://iec.ch/TC57/CIM100#DCBaseTerminal.DCNode) | No cardinality available DCNode | The DC connectivity node to which this DC base terminal connects with zero impedance. | DCBaseTerminal |
| sequenceNumber | [cim:ACDCTerminal.sequenceNumber](http://iec.ch/TC57/CIM100#ACDCTerminal.sequenceNumber) | No cardinality available integer | The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the "starting point" for a two terminal branch. | ACDCTerminal |
| OperationalLimitSet | [cim:ACDCTerminal.OperationalLimitSet](http://iec.ch/TC57/CIM100#ACDCTerminal.OperationalLimitSet) | No cardinality available OperationalLimitSet | The operational limit sets at the terminal. | ACDCTerminal |
| BusNameMarker | [cim:ACDCTerminal.BusNameMarker](http://iec.ch/TC57/CIM100#ACDCTerminal.BusNameMarker) | No cardinality available BusNameMarker | The bus name marker used to name the bus (topological node). | ACDCTerminal |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
