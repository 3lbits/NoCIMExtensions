# PhaseTapChangerTabular

_Describes a tap changer with a table defining the relation between the tap step and the phase angle difference across the transformer._

**URI**: [cim:PhaseTapChangerTabular](http://iec.ch/TC57/CIM100#PhaseTapChangerTabular)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class PhaseTapChangerTabular
    click PhaseTapChangerTabular href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTabular/"
    style PhaseTapChangerTabular fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PhaseTapChanger <|-- PhaseTapChangerTabular : inherits
            click PhaseTapChanger href "/Models/Profiles/CoreEquipment/AbstractClasses/PhaseTapChanger/"
            style PhaseTapChanger fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        TapChanger <|-- PhaseTapChanger : inherits
            click TapChanger href "/Models/Profiles/CoreEquipment/AbstractClasses/TapChanger/"
            style TapChanger fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- TapChanger : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerTabular --> PhaseTapChangerTable : PhaseTapChangerTabular.PhaseTapChangerTable

        PhaseTapChangerTable
            click PhaseTapChangerTable href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTable/"
            style PhaseTapChangerTable fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        PhaseTapChanger --> TransformerEnd : PhaseTapChanger.TransformerEnd

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/CoreEquipment/AbstractClasses/TransformerEnd/"
            style TransformerEnd fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        TapChanger --> TapSchedule : TapChanger.TapSchedules

        TapSchedule
            click TapSchedule href "/Models/Profiles/CoreEquipment/AbstractClasses/TapSchedule/"
            style TapSchedule fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        TapChanger --> TapChangerControl : TapChanger.TapChangerControl

        TapChangerControl
            click TapChangerControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerControl/"
            style TapChangerControl fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TapSchedule --> TapChanger : TapSchedule.TapChanger

        TapSchedule
            click TapSchedule href "/Models/Profiles/CoreEquipment/AbstractClasses/TapSchedule/"
            style TapSchedule fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerTable --> PhaseTapChangerTabular : PhaseTapChangerTable.PhaseTapChangerTabular

        PhaseTapChangerTable
            click PhaseTapChangerTable href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTable/"
            style PhaseTapChangerTable fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TapChangerControl --> TapChanger : TapChangerControl.TapChanger

        TapChangerControl
            click TapChangerControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerControl/"
            style TapChangerControl fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TransformerEnd --> PhaseTapChanger : TransformerEnd.PhaseTapChanger

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/CoreEquipment/AbstractClasses/TransformerEnd/"
            style TransformerEnd fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        PhaseTapChangerTabular : PhaseTapChangerTabular.PhaseTapChangerTable
        PhaseTapChanger : PhaseTapChanger.TransformerEnd
        TapChanger : TapChanger.TapSchedules
        TapChanger : TapChanger.highStep
        TapChanger : TapChanger.lowStep
        TapChanger : TapChanger.ltcFlag
        TapChanger : TapChanger.neutralStep
        TapChanger : TapChanger.neutralU
        TapChanger : TapChanger.normalStep
        TapChanger : TapChanger.TapChangerControl
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * [TapChanger](/Models/Profiles/CoreEquipment/AbstractClasses/TapChanger/)
            * [PhaseTapChanger](/Models/Profiles/CoreEquipment/AbstractClasses/PhaseTapChanger/)
                * **PhaseTapChangerTabular**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| PhaseTapChangerTable | [cim:PhaseTapChangerTabular.PhaseTapChangerTable](http://iec.ch/TC57/CIM100#PhaseTapChangerTabular.PhaseTapChangerTable) | No cardinality available PhaseTapChangerTable | The phase tap changer table for this phase tap changer. | direct |
| TransformerEnd | [cim:PhaseTapChanger.TransformerEnd](http://iec.ch/TC57/CIM100#PhaseTapChanger.TransformerEnd) | No cardinality available TransformerEnd | Transformer end to which this phase tap changer belongs. | PhaseTapChanger |
| TapSchedules | [cim:TapChanger.TapSchedules](http://iec.ch/TC57/CIM100#TapChanger.TapSchedules) | No cardinality available TapSchedule | A TapChanger can have TapSchedules. | TapChanger |
| highStep | [cim:TapChanger.highStep](http://iec.ch/TC57/CIM100#TapChanger.highStep) | No cardinality available integer | Highest possible tap step position, advance from neutral.
The attribute shall be greater than lowStep. | TapChanger |
| lowStep | [cim:TapChanger.lowStep](http://iec.ch/TC57/CIM100#TapChanger.lowStep) | No cardinality available integer | Lowest possible tap step position, retard from neutral. | TapChanger |
| ltcFlag | [cim:TapChanger.ltcFlag](http://iec.ch/TC57/CIM100#TapChanger.ltcFlag) | No cardinality available boolean | Specifies whether or not a TapChanger has load tap changing capabilities. | TapChanger |
| neutralStep | [cim:TapChanger.neutralStep](http://iec.ch/TC57/CIM100#TapChanger.neutralStep) | No cardinality available integer | The neutral tap step position for this winding.
The attribute shall be equal to or greater than lowStep and equal or less than highStep.
It is the step position where the voltage is neutralU when the other terminals of the transformer are at the ratedU.  If there are other tap changers on the transformer those taps are kept constant at their neutralStep. | TapChanger |
| neutralU | [cim:TapChanger.neutralU](http://iec.ch/TC57/CIM100#TapChanger.neutralU) | No cardinality available Voltage | Voltage at which the winding operates at the neutral tap setting. It is the voltage at the terminal of the PowerTransformerEnd associated with the tap changer when all tap changers on the transformer are at their neutralStep position.  Normally neutralU of the tap changer is the same as ratedU of the PowerTransformerEnd, but it can differ in special cases such as when the tapping mechanism is separate from the winding more common on lower voltage transformers.
This attribute is not relevant for PhaseTapChangerAsymmetrical, PhaseTapChangerSymmetrical and PhaseTapChangerLinear. | TapChanger |
| normalStep | [cim:TapChanger.normalStep](http://iec.ch/TC57/CIM100#TapChanger.normalStep) | No cardinality available integer | The tap step position used in "normal" network operation for this winding. For a "Fixed" tap changer indicates the current physical tap setting.
The attribute shall be equal to or greater than lowStep and equal to or less than highStep. | TapChanger |
| TapChangerControl | [cim:TapChanger.TapChangerControl](http://iec.ch/TC57/CIM100#TapChanger.TapChangerControl) | No cardinality available TapChangerControl | The regulating control scheme in which this tap changer participates. | TapChanger |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
