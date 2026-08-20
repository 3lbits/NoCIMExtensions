# LinearShuntCompensator

_A linear shunt compensator has banks or sections with equal admittance values._

**URI**: [cim:LinearShuntCompensator](http://iec.ch/TC57/CIM100#LinearShuntCompensator)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class LinearShuntCompensator
    click LinearShuntCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/LinearShuntCompensator/"
    style LinearShuntCompensator fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        ShuntCompensator <|-- LinearShuntCompensator : inherits
            click ShuntCompensator href "/Models/Profiles/ShortCircuit/AbstractClasses/ShuntCompensator/"
            style ShuntCompensator fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- ShuntCompensator : inherits
            click RegulatingCondEq href "/Models/Profiles/ShortCircuit/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/ShortCircuit/AbstractClasses/EnergyConnection/"
            style EnergyConnection fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/"
            style Equipment fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white



        LinearShuntCompensator : LinearShuntCompensator.b0PerSection
        LinearShuntCompensator : LinearShuntCompensator.g0PerSection
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/ShortCircuit/AbstractClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/ShortCircuit/AbstractClasses/RegulatingCondEq/)
                        * [ShuntCompensator](/Models/Profiles/ShortCircuit/AbstractClasses/ShuntCompensator/)
                            * **LinearShuntCompensator**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| b0PerSection | [cim:LinearShuntCompensator.b0PerSection](http://iec.ch/TC57/CIM100#LinearShuntCompensator.b0PerSection) | No cardinality available Susceptance | Zero sequence shunt (charging) susceptance per section. | direct |
| g0PerSection | [cim:LinearShuntCompensator.g0PerSection](http://iec.ch/TC57/CIM100#LinearShuntCompensator.g0PerSection) | No cardinality available Conductance | Zero sequence shunt (charging) conductance per section. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
