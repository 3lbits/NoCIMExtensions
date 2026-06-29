# EnergySource

_A generic equivalent for an energy supplier on a transmission or distribution voltage level._

**URI**: [cim:EnergySource](http://iec.ch/TC57/CIM100#EnergySource)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class EnergySource
    click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
    style EnergySource fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- EnergySource : inherits
            click EnergyConnection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/ShortCircuit/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Resistance : EnergySource.r

        Resistance
            click Resistance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Resistance/"
            style Resistance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergySource --> Resistance : EnergySource.r0

        Resistance
            click Resistance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Resistance/"
            style Resistance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergySource --> Resistance : EnergySource.rn

        Resistance
            click Resistance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Resistance/"
            style Resistance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergySource --> Reactance : EnergySource.x

        Reactance
            click Reactance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Reactance/"
            style Reactance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergySource --> Reactance : EnergySource.x0

        Reactance
            click Reactance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Reactance/"
            style Reactance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergySource --> Reactance : EnergySource.xn

        Reactance
            click Reactance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Reactance/"
            style Reactance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EnergySource : EnergySource.r
        EnergySource : EnergySource.r0
        EnergySource : EnergySource.rn
        EnergySource : EnergySource.x
        EnergySource : EnergySource.x0
        EnergySource : EnergySource.xn
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/ShortCircuit/ConcreteClasses/EnergyConnection/)
                    * **EnergySource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| r | [cim:EnergySource.r](http://iec.ch/TC57/CIM100#EnergySource.r) | No cardinality available Resistance | Positive sequence Thevenin resistance. | direct |
| r0 | [cim:EnergySource.r0](http://iec.ch/TC57/CIM100#EnergySource.r0) | No cardinality available Resistance | Zero sequence Thevenin resistance. | direct |
| rn | [cim:EnergySource.rn](http://iec.ch/TC57/CIM100#EnergySource.rn) | No cardinality available Resistance | Negative sequence Thevenin resistance. | direct |
| x | [cim:EnergySource.x](http://iec.ch/TC57/CIM100#EnergySource.x) | No cardinality available Reactance | Positive sequence Thevenin reactance. | direct |
| x0 | [cim:EnergySource.x0](http://iec.ch/TC57/CIM100#EnergySource.x0) | No cardinality available Reactance | Zero sequence Thevenin reactance. | direct |
| xn | [cim:EnergySource.xn](http://iec.ch/TC57/CIM100#EnergySource.xn) | No cardinality available Reactance | Negative sequence Thevenin reactance. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
