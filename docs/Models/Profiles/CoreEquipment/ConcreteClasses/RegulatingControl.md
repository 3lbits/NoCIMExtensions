# RegulatingControl

_Specifies a set of equipment that works together to control a power system quantity such as voltage or flow. 
Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment.
The specified terminal shall be associated with the connectivity node of the controlled point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers.
For flow control, load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.
The attribute minAllowedTargetValue and maxAllowedTargetValue are required in the following cases:
- For a power generating module operated in power factor control mode to specify maximum and minimum power factor values;
- Whenever it is necessary to have an off center target voltage for the tap changer regulator. For instance, due to long cables to off shore wind farms and the need to have a simpler setup at the off shore transformer platform, the voltage is controlled from the land at the connection point for the off shore wind farm. Since there usually is a voltage rise along the cable, there is typical and overvoltage of up 3-4 kV compared to the on shore station. Thus in normal operation the tap changer on the on shore station is operated with a target set point, which is in the lower parts of the dead band.
The attributes minAllowedTargetValue and maxAllowedTargetValue are not related to the attribute targetDeadband and thus they are not treated as an alternative of the targetDeadband. They are needed due to limitations in the local substation controller. The attribute targetDeadband is used to prevent the power flow from move the tap position in circles (hunting) that is to be used regardless of the attributes minAllowedTargetValue and maxAllowedTargetValue._

**URI**: [cim:RegulatingControl](http://iec.ch/TC57/CIM100#RegulatingControl)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class RegulatingControl
    click RegulatingControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingControl/"
    style RegulatingControl fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl <|-- TapChangerControl : inherits

        TapChangerControl
            click TapChangerControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerControl/"
            style TapChangerControl fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- RegulatingControl : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl --> RegulationSchedule : RegulatingControl.RegulationSchedule

        RegulationSchedule
            click RegulationSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulationSchedule/"
            style RegulationSchedule fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        RegulatingControl --> RegulatingCondEq : RegulatingControl.RegulatingCondEq

        RegulatingCondEq
            click RegulatingCondEq href "/Models/Profiles/CoreEquipment/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        RegulatingControl --> Terminal : RegulatingControl.Terminal

        Terminal
            click Terminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/Terminal/"
            style Terminal fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulationSchedule --> RegulatingControl : RegulationSchedule.RegulatingControl

        RegulationSchedule
            click RegulationSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulationSchedule/"
            style RegulationSchedule fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingCondEq --> RegulatingControl : RegulatingCondEq.RegulatingControl

        RegulatingCondEq
            click RegulatingCondEq href "/Models/Profiles/CoreEquipment/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> RegulatingControl : Terminal.RegulatingControl

        Terminal
            click Terminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/Terminal/"
            style Terminal fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl --> RegulatingControlModeKind : RegulatingControl.mode

        RegulatingControlModeKind
            click RegulatingControlModeKind href "/Models/Profiles/CoreEquipment/Enumerations/RegulatingControlModeKind/"
            style RegulatingControlModeKind fill:#5729FF,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl : RegulatingControl.RegulationSchedule
        RegulatingControl : RegulatingControl.RegulatingCondEq
        RegulatingControl : RegulatingControl.mode
        RegulatingControl : RegulatingControl.Terminal
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * **RegulatingControl**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| RegulationSchedule | [cim:RegulatingControl.RegulationSchedule](http://iec.ch/TC57/CIM100#RegulatingControl.RegulationSchedule) | No cardinality available RegulationSchedule | Schedule for this regulating control. | direct |
| RegulatingCondEq | [cim:RegulatingControl.RegulatingCondEq](http://iec.ch/TC57/CIM100#RegulatingControl.RegulatingCondEq) | No cardinality available RegulatingCondEq | The equipment that participates in this regulating control scheme. | direct |
| mode | [cim:RegulatingControl.mode](http://iec.ch/TC57/CIM100#RegulatingControl.mode) | No cardinality available RegulatingControlModeKind | The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. | direct |
| Terminal | [cim:RegulatingControl.Terminal](http://iec.ch/TC57/CIM100#RegulatingControl.Terminal) | No cardinality available Terminal | The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node or a connectivity node.  Sometimes it is useful to model regulation at a terminal of a bus bar object. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
