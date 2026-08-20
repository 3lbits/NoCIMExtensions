# ControlArea

_A control area is a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be used for a variety of purposes including automatic generation control, power flow solution area interchange control specification, and input to load forecasting. All generation and load within the area defined by the terminals on the border are considered in the area interchange control. Note that any number of overlapping control area specifications can be superimposed on the physical model. The following general principles apply to ControlArea:
1.  The control area orientation for net interchange is positive for an import, negative for an export.
2.  The control area net interchange is determined by summing flows in Terminals. The Terminals are identified by creating a set of TieFlow objects associated with a ControlArea object. Each TieFlow object identifies one Terminal.
3.  In a single network model, a tie between two control areas must be modelled in both control area specifications, such that the two representations of the tie flow sum to zero.
4.  The normal orientation of Terminal flow is positive for flow into the conducting equipment that owns the Terminal. (i.e. flow from a bus into a device is positive.) However, the orientation of each flow in the control area specification must align with the control area convention, i.e. import is positive. If the orientation of the Terminal flow referenced by a TieFlow is positive into the control area, then this is confirmed by setting TieFlow.positiveFlowIn flag TRUE. If not, the orientation must be reversed by setting the TieFlow.positiveFlowIn flag FALSE._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ControlArea](http://iec.ch/TC57/CIM100#ControlArea)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ControlArea
    click ControlArea href "/Models/Profiles/CoreEquipment/AbstractClasses/ControlArea/"
    style ControlArea fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ControlArea : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea --> TieFlow : ControlArea.TieFlow

        TieFlow
            click TieFlow href "/Models/Profiles/CoreEquipment/ConcreteClasses/TieFlow/"
            style TieFlow fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        ControlArea --> ControlAreaGeneratingUnit : ControlArea.ControlAreaGeneratingUnit

        ControlAreaGeneratingUnit
            click ControlAreaGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ControlAreaGeneratingUnit/"
            style ControlAreaGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        ControlArea --> EnergyArea : ControlArea.EnergyArea

        EnergyArea
            click EnergyArea href "/Models/Profiles/CoreEquipment/AbstractClasses/EnergyArea/"
            style EnergyArea fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ControlAreaGeneratingUnit --> ControlArea : ControlAreaGeneratingUnit.ControlArea

        ControlAreaGeneratingUnit
            click ControlAreaGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ControlAreaGeneratingUnit/"
            style ControlAreaGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        EnergyArea --> ControlArea : EnergyArea.ControlArea

        EnergyArea
            click EnergyArea href "/Models/Profiles/CoreEquipment/AbstractClasses/EnergyArea/"
            style EnergyArea fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TieFlow --> ControlArea : TieFlow.ControlArea

        TieFlow
            click TieFlow href "/Models/Profiles/CoreEquipment/ConcreteClasses/TieFlow/"
            style TieFlow fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea --> ControlAreaTypeKind : ControlArea.type

        ControlAreaTypeKind
            click ControlAreaTypeKind href "/Models/Profiles/CoreEquipment/Enumerations/ControlAreaTypeKind/"
            style ControlAreaTypeKind fill:#5729FF,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea : ControlArea.type
        ControlArea : ControlArea.TieFlow
        ControlArea : ControlArea.ControlAreaGeneratingUnit
        ControlArea : ControlArea.EnergyArea
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * **ControlArea**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| type | [cim:ControlArea.type](http://iec.ch/TC57/CIM100#ControlArea.type) | No cardinality available ControlAreaTypeKind | The primary type of control area definition used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.   A control area specified with primary type of automatic generation control could still be forecast and used as an interchange area in power flow analysis. | direct |
| TieFlow | [cim:ControlArea.TieFlow](http://iec.ch/TC57/CIM100#ControlArea.TieFlow) | No cardinality available TieFlow | The tie flows associated with the control area. | direct |
| ControlAreaGeneratingUnit | [cim:ControlArea.ControlAreaGeneratingUnit](http://iec.ch/TC57/CIM100#ControlArea.ControlAreaGeneratingUnit) | No cardinality available ControlAreaGeneratingUnit | The generating unit specifications for the control area. | direct |
| EnergyArea | [cim:ControlArea.EnergyArea](http://iec.ch/TC57/CIM100#ControlArea.EnergyArea) | No cardinality available EnergyArea | The energy area that is forecast from this control area specification. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
