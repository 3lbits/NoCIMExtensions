# ACDCConverterDCTerminal

_A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC side._

**URI**: [cim:ACDCConverterDCTerminal](http://iec.ch/TC57/CIM100#ACDCConverterDCTerminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ACDCConverterDCTerminal
    click ACDCConverterDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverterDCTerminal/"
    style ACDCConverterDCTerminal fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        DCBaseTerminal <|-- ACDCConverterDCTerminal : inherits
            click DCBaseTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCBaseTerminal/"
            style DCBaseTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCTerminal <|-- DCBaseTerminal : inherits
            click ACDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverterDCTerminal --> ACDCConverter : ACDCConverterDCTerminal.DCConductingEquipment

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
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

        ACDCConverter --> ACDCConverterDCTerminal : ACDCConverter.DCTerminals

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BusNameMarker --> ACDCTerminal : BusNameMarker.Terminal

        BusNameMarker
            click BusNameMarker href "/Models/Profiles/CoreEquipment/ConcreteClasses/BusNameMarker/"
            style BusNameMarker fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCNode --> DCBaseTerminal : DCNode.DCTerminals

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> ACDCTerminal : OperationalLimitSet.Terminal

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverterDCTerminal --> DCPolarityKind : ACDCConverterDCTerminal.polarity

        DCPolarityKind
            click DCPolarityKind href "/Models/Profiles/CoreEquipment/Enumerations/DCPolarityKind/"
            style DCPolarityKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverterDCTerminal : ACDCConverterDCTerminal.DCConductingEquipment
        ACDCConverterDCTerminal : ACDCConverterDCTerminal.polarity
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
            * **ACDCConverterDCTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCConductingEquipment | [cim:ACDCConverterDCTerminal.DCConductingEquipment](http://iec.ch/TC57/CIM100#ACDCConverterDCTerminal.DCConductingEquipment) | No cardinality available ACDCConverter | A DC converter terminal belong to an DC converter. | direct |
| polarity | [cim:ACDCConverterDCTerminal.polarity](http://iec.ch/TC57/CIM100#ACDCConverterDCTerminal.polarity) | No cardinality available DCPolarityKind | Represents the normal network polarity condition. Depending on the converter configuration the value shall be set as follows:
- For a monopole with two converter terminals use DCPolarityKind “positive” and “negative”.
- For a bi-pole or symmetric monopole with three converter terminals use DCPolarityKind “positive”, “middle” and “negative”. | direct |
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
