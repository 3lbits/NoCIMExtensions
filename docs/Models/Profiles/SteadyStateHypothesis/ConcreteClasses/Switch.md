# Switch

_A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant._

**URI**: [cim:Switch](http://iec.ch/TC57/CIM100#Switch)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Switch
    click Switch href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Switch/"
    style Switch fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch <|-- Disconnector : inherits

        Disconnector
            click Disconnector href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Disconnector/"
            style Disconnector fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch <|-- Fuse : inherits

        Fuse
            click Fuse href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Fuse/"
            style Fuse fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch <|-- GroundDisconnector : inherits

        GroundDisconnector
            click GroundDisconnector href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/GroundDisconnector/"
            style GroundDisconnector fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch <|-- Jumper : inherits

        Jumper
            click Jumper href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Jumper/"
            style Jumper fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Switch <|-- ProtectedSwitch : inherits

        ProtectedSwitch
            click ProtectedSwitch href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ProtectedSwitch/"
            style ProtectedSwitch fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- Switch : inherits
            click ConductingEquipment href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        Switch : Switch.open
        Switch : Switch.locked
        Equipment : Equipment.inService
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ConductingEquipment/)
                * **Switch**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| open | [cim:Switch.open](http://iec.ch/TC57/CIM100#Switch.open) | No cardinality available boolean | The attribute tells if the switch is considered open when used as input to topology processing. | direct |
| locked | [cim:Switch.locked](http://iec.ch/TC57/CIM100#Switch.locked) | No cardinality available boolean | If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:
<ul>
	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>
	<li>locked=false and Switch.open=true. The resulting state is open;</li>
	<li>locked=false and Switch.open=false. The resulting state is closed.</li>
</ul> | direct |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | No cardinality available boolean | Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. | Equipment |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
