# GroundingImpedance

_A fixed impedance device used for grounding._

**URI**: [cim:GroundingImpedance](http://iec.ch/TC57/CIM100#GroundingImpedance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class GroundingImpedance
    click GroundingImpedance href "/Models/Profiles/ShortCircuit/ConcreteClasses/GroundingImpedance/"
    style GroundingImpedance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EarthFaultCompensator <|-- GroundingImpedance : inherits
            click EarthFaultCompensator href "/Models/Profiles/ShortCircuit/AbstractClasses/EarthFaultCompensator/"
            style EarthFaultCompensator fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EarthFaultCompensator : inherits
            click ConductingEquipment href "/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        GroundingImpedance : GroundingImpedance.x
        EarthFaultCompensator : EarthFaultCompensator.r
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/)
                * [EarthFaultCompensator](/Models/Profiles/ShortCircuit/AbstractClasses/EarthFaultCompensator/)
                    * **GroundingImpedance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| x | [cim:GroundingImpedance.x](http://iec.ch/TC57/CIM100#GroundingImpedance.x) | No cardinality available Reactance | Reactance of device. | direct |
| r | [cim:EarthFaultCompensator.r](http://iec.ch/TC57/CIM100#EarthFaultCompensator.r) | No cardinality available Resistance | Nominal resistance of device. | EarthFaultCompensator |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
