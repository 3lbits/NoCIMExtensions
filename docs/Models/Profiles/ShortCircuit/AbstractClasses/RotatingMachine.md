# RotatingMachine

_A rotating machine which may be used as a generator or motor._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:RotatingMachine](http://iec.ch/TC57/CIM100#RotatingMachine)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RotatingMachine
    click RotatingMachine href "/Models/Profiles/ShortCircuit/AbstractClasses/RotatingMachine/"
    style RotatingMachine fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine <|-- AsynchronousMachine : inherits

        AsynchronousMachine
            click AsynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/AsynchronousMachine/"
            style AsynchronousMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine <|-- SynchronousMachine : inherits

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- RotatingMachine : inherits
            click RegulatingCondEq href "/Models/Profiles/ShortCircuit/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/ShortCircuit/AbstractClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
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



        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/AbstractClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/ShortCircuit/AbstractClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/ShortCircuit/AbstractClasses/RegulatingCondEq/)
                        * **RotatingMachine**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
