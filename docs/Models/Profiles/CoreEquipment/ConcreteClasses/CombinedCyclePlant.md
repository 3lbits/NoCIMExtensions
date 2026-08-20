# CombinedCyclePlant

_A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency._

**URI**: [cim:CombinedCyclePlant](http://iec.ch/TC57/CIM100#CombinedCyclePlant)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class CombinedCyclePlant
    click CombinedCyclePlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/CombinedCyclePlant/"
    style CombinedCyclePlant fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- CombinedCyclePlant : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        CombinedCyclePlant --> ThermalGeneratingUnit : CombinedCyclePlant.ThermalGeneratingUnits

        ThermalGeneratingUnit
            click ThermalGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ThermalGeneratingUnit/"
            style ThermalGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ThermalGeneratingUnit --> CombinedCyclePlant : ThermalGeneratingUnit.CombinedCyclePlant

        ThermalGeneratingUnit
            click ThermalGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ThermalGeneratingUnit/"
            style ThermalGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        CombinedCyclePlant : CombinedCyclePlant.ThermalGeneratingUnits
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * **CombinedCyclePlant**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ThermalGeneratingUnits | [cim:CombinedCyclePlant.ThermalGeneratingUnits](http://iec.ch/TC57/CIM100#CombinedCyclePlant.ThermalGeneratingUnits) | No cardinality available ThermalGeneratingUnit | A thermal generating unit may be a member of a combined cycle plant. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
