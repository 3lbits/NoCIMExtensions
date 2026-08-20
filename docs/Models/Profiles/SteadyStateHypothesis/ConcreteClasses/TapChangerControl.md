# TapChangerControl

_Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment._

**URI**: [cim:TapChangerControl](http://iec.ch/TC57/CIM100#TapChangerControl)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class TapChangerControl
    click TapChangerControl href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/TapChangerControl/"
    style TapChangerControl fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingControl <|-- TapChangerControl : inherits
            click RegulatingControl href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RegulatingControl/"
            style RegulatingControl fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- RegulatingControl : inherits
            click PowerSystemResource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        RegulatingControl --> UnitMultiplier : RegulatingControl.targetValueUnitMultiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl : RegulatingControl.discrete
        RegulatingControl : RegulatingControl.enabled
        RegulatingControl : RegulatingControl.targetDeadband
        RegulatingControl : RegulatingControl.targetValue
        RegulatingControl : RegulatingControl.targetValueUnitMultiplier
        RegulatingControl : RegulatingControl.maxAllowedTargetValue
        RegulatingControl : RegulatingControl.minAllowedTargetValue
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/)
        * [RegulatingControl](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RegulatingControl/)
            * **TapChangerControl**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| discrete | [cim:RegulatingControl.discrete](http://iec.ch/TC57/CIM100#RegulatingControl.discrete) | No cardinality available boolean | The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap changers and shunt compensators. | RegulatingControl |
| enabled | [cim:RegulatingControl.enabled](http://iec.ch/TC57/CIM100#RegulatingControl.enabled) | No cardinality available boolean | The flag tells if regulation is enabled. | RegulatingControl |
| targetDeadband | [cim:RegulatingControl.targetDeadband](http://iec.ch/TC57/CIM100#RegulatingControl.targetDeadband) | No cardinality available float | This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating.  The units of those appropriate for the mode. The attribute shall be a positive value or zero. If RegulatingControl.discrete is set to "false", the RegulatingControl.targetDeadband is to be ignored.
Note that for instance, if the targetValue is 100 kV and the targetDeadband is 2 kV the range is from 99 to 101 kV. | RegulatingControl |
| targetValue | [cim:RegulatingControl.targetValue](http://iec.ch/TC57/CIM100#RegulatingControl.targetValue) | No cardinality available float | The target value specified for case input.   This value can be used for the target value without the use of schedules. The value has the units appropriate to the mode attribute. | RegulatingControl |
| targetValueUnitMultiplier | [cim:RegulatingControl.targetValueUnitMultiplier](http://iec.ch/TC57/CIM100#RegulatingControl.targetValueUnitMultiplier) | No cardinality available UnitMultiplier | Specify the multiplier for used for the targetValue. | RegulatingControl |
| maxAllowedTargetValue | [cim:RegulatingControl.maxAllowedTargetValue](http://iec.ch/TC57/CIM100#RegulatingControl.maxAllowedTargetValue) | No cardinality available float | Maximum allowed target value (RegulatingControl.targetValue). | RegulatingControl |
| minAllowedTargetValue | [cim:RegulatingControl.minAllowedTargetValue](http://iec.ch/TC57/CIM100#RegulatingControl.minAllowedTargetValue) | No cardinality available float | Minimum allowed target value (RegulatingControl.targetValue). | RegulatingControl |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
