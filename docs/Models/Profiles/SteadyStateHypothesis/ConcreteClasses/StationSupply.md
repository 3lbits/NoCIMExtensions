# StationSupply

_Station supply with load derived from the station output._

**URI**: [cim:StationSupply](http://iec.ch/TC57/CIM100#StationSupply)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class StationSupply
    click StationSupply href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/StationSupply/"
    style StationSupply fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConsumer <|-- StationSupply : inherits
            click EnergyConsumer href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- EnergyConsumer : inherits
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



        EnergyConsumer : EnergyConsumer.p
        EnergyConsumer : EnergyConsumer.q
        Equipment : Equipment.inService
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConnection/)
                    * [EnergyConsumer](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConsumer/)
                        * **StationSupply**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| p | [cim:EnergyConsumer.p](http://iec.ch/TC57/CIM100#EnergyConsumer.p) | No cardinality available ActivePower | Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node.
For voltage dependent loads the value is at rated voltage.
Starting value for a steady state solution. | EnergyConsumer |
| q | [cim:EnergyConsumer.q](http://iec.ch/TC57/CIM100#EnergyConsumer.q) | No cardinality available ReactivePower | Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node.
For voltage dependent loads the value is at rated voltage.
Starting value for a steady state solution. | EnergyConsumer |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | No cardinality available boolean | Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. | Equipment |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
