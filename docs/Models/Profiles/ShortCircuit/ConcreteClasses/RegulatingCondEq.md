# RegulatingCondEq

_A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network._

**URI**: [cim:RegulatingCondEq](http://iec.ch/TC57/CIM100#RegulatingCondEq)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RegulatingCondEq
    click RegulatingCondEq href "/Models/Profiles/ShortCircuit/ConcreteClasses/RegulatingCondEq/"
    style RegulatingCondEq fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingCondEq <|-- ExternalNetworkInjection : inherits

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingCondEq <|-- RotatingMachine : inherits

        RotatingMachine
            click RotatingMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/RotatingMachine/"
            style RotatingMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingCondEq <|-- ShuntCompensator : inherits

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
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



        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/ShortCircuit/ConcreteClasses/EnergyConnection/)
                    * **RegulatingCondEq**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
