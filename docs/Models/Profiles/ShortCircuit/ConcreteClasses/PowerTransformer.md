# PowerTransformer

_An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
A power transformer may be composed of separate transformer tanks that need not be identical.
A power transformer can be modelled with or without tanks and is intended for use in both balanced and unbalanced representations.   A power transformer typically has two terminals, but may have one (grounding), three or more terminals.
The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead._

**URI**: [cim:PowerTransformer](http://iec.ch/TC57/CIM100#PowerTransformer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PowerTransformer
    click PowerTransformer href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformer/"
    style PowerTransformer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- PowerTransformer : inherits
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

        PowerTransformer --> CurrentFlow : PowerTransformer.beforeShCircuitHighestOperatingCurrent

        CurrentFlow
            click CurrentFlow href "/Models/Profiles/ShortCircuit/ConcreteClasses/CurrentFlow/"
            style CurrentFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerTransformer --> Voltage : PowerTransformer.beforeShCircuitHighestOperatingVoltage

        Voltage
            click Voltage href "/Models/Profiles/ShortCircuit/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerTransformer --> AngleDegrees : PowerTransformer.beforeShortCircuitAnglePf

        AngleDegrees
            click AngleDegrees href "/Models/Profiles/ShortCircuit/ConcreteClasses/AngleDegrees/"
            style AngleDegrees fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerTransformer --> Voltage : PowerTransformer.highSideMinOperatingU

        Voltage
            click Voltage href "/Models/Profiles/ShortCircuit/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PowerTransformer : PowerTransformer.beforeShCircuitHighestOperatingCurrent
        PowerTransformer : PowerTransformer.beforeShCircuitHighestOperatingVoltage
        PowerTransformer : PowerTransformer.beforeShortCircuitAnglePf
        PowerTransformer : PowerTransformer.highSideMinOperatingU
        PowerTransformer : PowerTransformer.isPartOfGeneratorUnit
        PowerTransformer : PowerTransformer.operationalValuesConsidered
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/ShortCircuit/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/ShortCircuit/ConcreteClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/ShortCircuit/ConcreteClasses/ConductingEquipment/)
                * **PowerTransformer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| beforeShCircuitHighestOperatingCurrent | [cim:PowerTransformer.beforeShCircuitHighestOperatingCurrent](http://iec.ch/TC57/CIM100#PowerTransformer.beforeShCircuitHighestOperatingCurrent) | No cardinality available CurrentFlow | The highest operating current (Ib in IEC 60909-0) before short circuit (depends on network configuration and relevant reliability philosophy). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. | direct |
| beforeShCircuitHighestOperatingVoltage | [cim:PowerTransformer.beforeShCircuitHighestOperatingVoltage](http://iec.ch/TC57/CIM100#PowerTransformer.beforeShCircuitHighestOperatingVoltage) | No cardinality available Voltage | The highest operating voltage (Ub in IEC 60909-0) before short circuit. It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is worst case voltage on the low side winding (3.7.1 of IEC 60909:2001). Used to define operating conditions. | direct |
| beforeShortCircuitAnglePf | [cim:PowerTransformer.beforeShortCircuitAnglePf](http://iec.ch/TC57/CIM100#PowerTransformer.beforeShortCircuitAnglePf) | No cardinality available AngleDegrees | The angle of power factor before short circuit (phib in IEC 60909-0). It is used for calculation of the impedance correction factor KT defined in IEC 60909-0. This is the worst case power factor. Used to define operating conditions. | direct |
| highSideMinOperatingU | [cim:PowerTransformer.highSideMinOperatingU](http://iec.ch/TC57/CIM100#PowerTransformer.highSideMinOperatingU) | No cardinality available Voltage | The minimum operating voltage (uQmin in IEC 60909-0) at the high voltage side (Q side) of the unit transformer of the power station unit. A value well established from long-term operating experience of the system. It is used for calculation of the impedance correction factor KG defined in IEC 60909-0. | direct |
| isPartOfGeneratorUnit | [cim:PowerTransformer.isPartOfGeneratorUnit](http://iec.ch/TC57/CIM100#PowerTransformer.isPartOfGeneratorUnit) | No cardinality available boolean | Indicates whether the machine is part of a power station unit. Used for short circuit data exchange according to IEC 60909.  It has an impact on how the correction factors are calculated for transformers, since the transformer is not necessarily part of a synchronous machine and generating unit. It is not always possible to derive this information from the model. This is why the attribute is necessary. | direct |
| operationalValuesConsidered | [cim:PowerTransformer.operationalValuesConsidered](http://iec.ch/TC57/CIM100#PowerTransformer.operationalValuesConsidered) | No cardinality available boolean | It is used to define if the data (other attributes related to short circuit data exchange) defines long term operational conditions or not. Used for short circuit data exchange according to IEC 60909. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
