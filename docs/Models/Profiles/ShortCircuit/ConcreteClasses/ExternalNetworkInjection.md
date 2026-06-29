# ExternalNetworkInjection

_This class represents the external network and it is used for IEC 60909 calculations._

**URI**: [cim:ExternalNetworkInjection](http://iec.ch/TC57/CIM100#ExternalNetworkInjection)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ExternalNetworkInjection
    click ExternalNetworkInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/ExternalNetworkInjection/"
    style ExternalNetworkInjection fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- ExternalNetworkInjection : inherits
            click RegulatingCondEq href "/Models/Profiles/ShortCircuit/ConcreteClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
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

        ExternalNetworkInjection --> CurrentFlow : ExternalNetworkInjection.maxInitialSymShCCurrent

        CurrentFlow
            click CurrentFlow href "/Models/Profiles/ShortCircuit/ConcreteClasses/CurrentFlow/"
            style CurrentFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ExternalNetworkInjection --> CurrentFlow : ExternalNetworkInjection.minInitialSymShCCurrent

        CurrentFlow
            click CurrentFlow href "/Models/Profiles/ShortCircuit/ConcreteClasses/CurrentFlow/"
            style CurrentFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ExternalNetworkInjection --> PU : ExternalNetworkInjection.voltageFactor

        PU
            click PU href "/Models/Profiles/ShortCircuit/ConcreteClasses/PU/"
            style PU fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ExternalNetworkInjection : ExternalNetworkInjection.ikSecond
        ExternalNetworkInjection : ExternalNetworkInjection.maxInitialSymShCCurrent
        ExternalNetworkInjection : ExternalNetworkInjection.maxR0ToX0Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.maxR1ToX1Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.maxZ0ToZ1Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.minInitialSymShCCurrent
        ExternalNetworkInjection : ExternalNetworkInjection.minR0ToX0Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.minR1ToX1Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.minZ0ToZ1Ratio
        ExternalNetworkInjection : ExternalNetworkInjection.voltageFactor
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/ShortCircuit/ConcreteClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/ShortCircuit/ConcreteClasses/RegulatingCondEq/)
                        * **ExternalNetworkInjection**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ikSecond | [cim:ExternalNetworkInjection.ikSecond](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.ikSecond) | No cardinality available boolean | Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik").  Used only if short circuit calculations are done according to superposition method. | direct |
| maxInitialSymShCCurrent | [cim:ExternalNetworkInjection.maxInitialSymShCCurrent](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxInitialSymShCCurrent) | No cardinality available CurrentFlow | Maximum initial symmetrical short-circuit currents (Ik" max) in A (Ik" = Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909. | direct |
| maxR0ToX0Ratio | [cim:ExternalNetworkInjection.maxR0ToX0Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxR0ToX0Ratio) | No cardinality available float | Maximum ratio of zero sequence resistance of Network Feeder to its zero sequence reactance (R(0)/X(0) max). Used for short circuit data exchange according to IEC 60909. | direct |
| maxR1ToX1Ratio | [cim:ExternalNetworkInjection.maxR1ToX1Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxR1ToX1Ratio) | No cardinality available float | Maximum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) max). Used for short circuit data exchange according to IEC 60909. | direct |
| maxZ0ToZ1Ratio | [cim:ExternalNetworkInjection.maxZ0ToZ1Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxZ0ToZ1Ratio) | No cardinality available float | Maximum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909. | direct |
| minInitialSymShCCurrent | [cim:ExternalNetworkInjection.minInitialSymShCCurrent](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minInitialSymShCCurrent) | No cardinality available CurrentFlow | Minimum initial symmetrical short-circuit currents (Ik" min) in A (Ik" = Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909. | direct |
| minR0ToX0Ratio | [cim:ExternalNetworkInjection.minR0ToX0Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minR0ToX0Ratio) | No cardinality available float | Indicates whether initial symmetrical short-circuit current and power have been calculated according to IEC (Ik"). Used for short circuit data exchange according to IEC 6090. | direct |
| minR1ToX1Ratio | [cim:ExternalNetworkInjection.minR1ToX1Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minR1ToX1Ratio) | No cardinality available float | Minimum ratio of positive sequence resistance of Network Feeder to its positive sequence reactance (R(1)/X(1) min). Used for short circuit data exchange according to IEC 60909. | direct |
| minZ0ToZ1Ratio | [cim:ExternalNetworkInjection.minZ0ToZ1Ratio](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minZ0ToZ1Ratio) | No cardinality available float | Minimum ratio of zero sequence impedance to its positive sequence impedance (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909. | direct |
| voltageFactor | [cim:ExternalNetworkInjection.voltageFactor](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.voltageFactor) | No cardinality available PU | Voltage factor in pu, which was used to calculate short-circuit current Ik" and power Sk".  Used only if short circuit calculations are done according to superposition method. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
