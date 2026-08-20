# ConductingEquipment

_The parts of the AC power system that are designed to carry current or that are conductively connected through terminals._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConductingEquipment](http://iec.ch/TC57/CIM100#ConductingEquipment)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ConductingEquipment
    click ConductingEquipment href "/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/"
    style ConductingEquipment fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- Conductor : inherits

        Conductor
            click Conductor href "/Models/Profiles/ShortCircuit/AbstractClasses/Conductor/"
            style Conductor fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- Connector : inherits

        Connector
            click Connector href "/Models/Profiles/ShortCircuit/AbstractClasses/Connector/"
            style Connector fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- EarthFaultCompensator : inherits

        EarthFaultCompensator
            click EarthFaultCompensator href "/Models/Profiles/ShortCircuit/AbstractClasses/EarthFaultCompensator/"
            style EarthFaultCompensator fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- EnergyConnection : inherits

        EnergyConnection
            click EnergyConnection href "/Models/Profiles/ShortCircuit/AbstractClasses/EnergyConnection/"
            style EnergyConnection fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- EquivalentEquipment : inherits

        EquivalentEquipment
            click EquivalentEquipment href "/Models/Profiles/ShortCircuit/AbstractClasses/EquivalentEquipment/"
            style EquivalentEquipment fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- PowerTransformer : inherits

        PowerTransformer
            click PowerTransformer href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformer/"
            style PowerTransformer fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- SeriesCompensator : inherits

        SeriesCompensator
            click SeriesCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/SeriesCompensator/"
            style SeriesCompensator fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/"
            style Equipment fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/)
            * **ConductingEquipment**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
