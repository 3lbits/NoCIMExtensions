# AccumulatorLimitSet

_An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement._

**URI**: [cim:AccumulatorLimitSet](http://iec.ch/TC57/CIM100#AccumulatorLimitSet)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class AccumulatorLimitSet
    click AccumulatorLimitSet href "/Models/Profiles/Operation/ConcreteClasses/AccumulatorLimitSet/"
    style AccumulatorLimitSet fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        LimitSet <|-- AccumulatorLimitSet : inherits
            click LimitSet href "/Models/Profiles/Operation/AbstractClasses/LimitSet/"
            style LimitSet fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- LimitSet : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        AccumulatorLimitSet --> Accumulator : AccumulatorLimitSet.Measurements

        Accumulator
            click Accumulator href "/Models/Profiles/Operation/ConcreteClasses/Accumulator/"
            style Accumulator fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        AccumulatorLimitSet --> AccumulatorLimit : AccumulatorLimitSet.Limits

        AccumulatorLimit
            click AccumulatorLimit href "/Models/Profiles/Operation/AbstractClasses/AccumulatorLimit/"
            style AccumulatorLimit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Accumulator --> AccumulatorLimitSet : Accumulator.LimitSets

        Accumulator
            click Accumulator href "/Models/Profiles/Operation/ConcreteClasses/Accumulator/"
            style Accumulator fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        AccumulatorLimit --> AccumulatorLimitSet : AccumulatorLimit.LimitSet

        AccumulatorLimit
            click AccumulatorLimit href "/Models/Profiles/Operation/AbstractClasses/AccumulatorLimit/"
            style AccumulatorLimit fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        AccumulatorLimitSet : AccumulatorLimitSet.Measurements
        AccumulatorLimitSet : AccumulatorLimitSet.Limits
        LimitSet : LimitSet.isPercentageLimits
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * [LimitSet](/Models/Profiles/Operation/AbstractClasses/LimitSet/)
        * **AccumulatorLimitSet**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Measurements | [cim:AccumulatorLimitSet.Measurements](http://iec.ch/TC57/CIM100#AccumulatorLimitSet.Measurements) | No cardinality available Accumulator | The Measurements using the LimitSet. | direct |
| Limits | [cim:AccumulatorLimitSet.Limits](http://iec.ch/TC57/CIM100#AccumulatorLimitSet.Limits) | No cardinality available AccumulatorLimit | The limit values used for supervision of Measurements. | direct |
| isPercentageLimits | [cim:LimitSet.isPercentageLimits](http://iec.ch/TC57/CIM100#LimitSet.isPercentageLimits) | No cardinality available boolean | Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. | LimitSet |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
