# HydroPowerPlant

_A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir._

**URI**: [cim:HydroPowerPlant](http://iec.ch/TC57/CIM100#HydroPowerPlant)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class HydroPowerPlant
    click HydroPowerPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPowerPlant/"
    style HydroPowerPlant fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- HydroPowerPlant : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroPowerPlant --> HydroGeneratingUnit : HydroPowerPlant.HydroGeneratingUnits

        HydroGeneratingUnit
            click HydroGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroGeneratingUnit/"
            style HydroGeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        HydroPowerPlant --> HydroPump : HydroPowerPlant.HydroPumps

        HydroPump
            click HydroPump href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPump/"
            style HydroPump fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroGeneratingUnit --> HydroPowerPlant : HydroGeneratingUnit.HydroPowerPlant

        HydroGeneratingUnit
            click HydroGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroGeneratingUnit/"
            style HydroGeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroPump --> HydroPowerPlant : HydroPump.HydroPowerPlant

        HydroPump
            click HydroPump href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPump/"
            style HydroPump fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroPowerPlant --> HydroPlantStorageKind : HydroPowerPlant.hydroPlantStorageType

        HydroPlantStorageKind
            click HydroPlantStorageKind href "/Models/Profiles/CoreEquipment/Enumerations/HydroPlantStorageKind/"
            style HydroPlantStorageKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroPowerPlant : HydroPowerPlant.HydroGeneratingUnits
        HydroPowerPlant : HydroPowerPlant.hydroPlantStorageType
        HydroPowerPlant : HydroPowerPlant.HydroPumps
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * **HydroPowerPlant**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| HydroGeneratingUnits | [cim:HydroPowerPlant.HydroGeneratingUnits](http://iec.ch/TC57/CIM100#HydroPowerPlant.HydroGeneratingUnits) | No cardinality available HydroGeneratingUnit | The hydro generating unit belongs to a hydro power plant. | direct |
| hydroPlantStorageType | [cim:HydroPowerPlant.hydroPlantStorageType](http://iec.ch/TC57/CIM100#HydroPowerPlant.hydroPlantStorageType) | No cardinality available HydroPlantStorageKind | The type of hydro power plant water storage. | direct |
| HydroPumps | [cim:HydroPowerPlant.HydroPumps](http://iec.ch/TC57/CIM100#HydroPowerPlant.HydroPumps) | No cardinality available HydroPump | The hydro pump may be a member of a pumped storage plant or a pump for distributing water. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
