# OperationalLimit

_A value and normal value associated with a specific kind of limit. 
The sub class value and normalValue attributes vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short).  
If a particular piece of equipment has multiple operational limits of the same kind (apparent power, current, etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with the smallest acceptableDuration shall have the largest limit value.  Note: A large current can only be allowed to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be allowed to flow for a longer duration._

**URI**: [cim:OperationalLimit](http://iec.ch/TC57/CIM100#OperationalLimit)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class OperationalLimit
    click OperationalLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/OperationalLimit/"
    style OperationalLimit fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit <|-- ActivePowerLimit : inherits

        ActivePowerLimit
            click ActivePowerLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ActivePowerLimit/"
            style ActivePowerLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit <|-- ApparentPowerLimit : inherits

        ApparentPowerLimit
            click ApparentPowerLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ApparentPowerLimit/"
            style ApparentPowerLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit <|-- CurrentLimit : inherits

        CurrentLimit
            click CurrentLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/CurrentLimit/"
            style CurrentLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimit <|-- VoltageLimit : inherits

        VoltageLimit
            click VoltageLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/VoltageLimit/"
            style VoltageLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- OperationalLimit : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * **OperationalLimit**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
