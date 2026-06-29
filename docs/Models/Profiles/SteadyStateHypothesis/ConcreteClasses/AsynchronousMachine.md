# AsynchronousMachine

_A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g. squirrel-cage induction machine._

**URI**: [cim:AsynchronousMachine](http://iec.ch/TC57/CIM100#AsynchronousMachine)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AsynchronousMachine
    click AsynchronousMachine href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/AsynchronousMachine/"
    style AsynchronousMachine fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RotatingMachine <|-- AsynchronousMachine : inherits
            click RotatingMachine href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RotatingMachine/"
            style RotatingMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- RotatingMachine : inherits
            click RegulatingCondEq href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> ActivePower : RotatingMachine.p

        ActivePower
            click ActivePower href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ActivePower/"
            style ActivePower fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RotatingMachine --> ReactivePower : RotatingMachine.q

        ReactivePower
            click ReactivePower href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ReactivePower/"
            style ReactivePower fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AsynchronousMachine --> AsynchronousMachineKind : AsynchronousMachine.asynchronousMachineType

        AsynchronousMachineKind
            click AsynchronousMachineKind href "/Models/Profiles/SteadyStateHypothesis/Enumerations/AsynchronousMachineKind/"
            style AsynchronousMachineKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AsynchronousMachine : AsynchronousMachine.asynchronousMachineType
        RotatingMachine : RotatingMachine.p
        RotatingMachine : RotatingMachine.q
        RegulatingCondEq : RegulatingCondEq.controlEnabled
        Equipment : Equipment.inService
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RegulatingCondEq/)
                        * [RotatingMachine](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RotatingMachine/)
                            * **AsynchronousMachine**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| asynchronousMachineType | [cim:AsynchronousMachine.asynchronousMachineType](http://iec.ch/TC57/CIM100#AsynchronousMachine.asynchronousMachineType) | No cardinality available AsynchronousMachineKind | Indicates the type of Asynchronous Machine (motor or generator). | direct |
| p | [cim:RotatingMachine.p](http://iec.ch/TC57/CIM100#RotatingMachine.p) | No cardinality available ActivePower | Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
Starting value for a steady state solution. | RotatingMachine |
| q | [cim:RotatingMachine.q](http://iec.ch/TC57/CIM100#RotatingMachine.q) | No cardinality available ReactivePower | Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
Starting value for a steady state solution. | RotatingMachine |
| controlEnabled | [cim:RegulatingCondEq.controlEnabled](http://iec.ch/TC57/CIM100#RegulatingCondEq.controlEnabled) | No cardinality available boolean | Specifies the regulation status of the equipment.  True is regulating, false is not regulating. | RegulatingCondEq |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | No cardinality available boolean | Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. | Equipment |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
