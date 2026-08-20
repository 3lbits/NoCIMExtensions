# FossilFuel

_The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   These are the specific fuels that the generating unit can consume._

**URI**: [cim:FossilFuel](http://iec.ch/TC57/CIM100#FossilFuel)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class FossilFuel
    click FossilFuel href "/Models/Profiles/CoreEquipment/ConcreteClasses/FossilFuel/"
    style FossilFuel fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- FossilFuel : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        FossilFuel --> ThermalGeneratingUnit : FossilFuel.ThermalGeneratingUnit

        ThermalGeneratingUnit
            click ThermalGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ThermalGeneratingUnit/"
            style ThermalGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ThermalGeneratingUnit --> FossilFuel : ThermalGeneratingUnit.FossilFuels

        ThermalGeneratingUnit
            click ThermalGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ThermalGeneratingUnit/"
            style ThermalGeneratingUnit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        FossilFuel --> FuelType : FossilFuel.fossilFuelType

        FuelType
            click FuelType href "/Models/Profiles/CoreEquipment/Enumerations/FuelType/"
            style FuelType fill:#5729FF,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        FossilFuel : FossilFuel.fossilFuelType
        FossilFuel : FossilFuel.ThermalGeneratingUnit
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * **FossilFuel**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| fossilFuelType | [cim:FossilFuel.fossilFuelType](http://iec.ch/TC57/CIM100#FossilFuel.fossilFuelType) | No cardinality available FuelType | The type of fossil fuel, such as coal, oil, or gas. | direct |
| ThermalGeneratingUnit | [cim:FossilFuel.ThermalGeneratingUnit](http://iec.ch/TC57/CIM100#FossilFuel.ThermalGeneratingUnit) | No cardinality available ThermalGeneratingUnit | A thermal generating unit may have one or more fossil fuels. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
