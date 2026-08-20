# AccumulatorLimit

_Limit values for Accumulator measurements._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:AccumulatorLimit](http://iec.ch/TC57/CIM100#AccumulatorLimit)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class AccumulatorLimit
    click AccumulatorLimit href "/Models/Profiles/Operation/AbstractClasses/AccumulatorLimit/"
    style AccumulatorLimit fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        Limit <|-- AccumulatorLimit : inherits
            click Limit href "/Models/Profiles/Operation/AbstractClasses/Limit/"
            style Limit fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Limit : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        AccumulatorLimit --> AccumulatorLimitSet : AccumulatorLimit.LimitSet

        AccumulatorLimitSet
            click AccumulatorLimitSet href "/Models/Profiles/Operation/ConcreteClasses/AccumulatorLimitSet/"
            style AccumulatorLimitSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        AccumulatorLimitSet --> AccumulatorLimit : AccumulatorLimitSet.Limits

        AccumulatorLimitSet
            click AccumulatorLimitSet href "/Models/Profiles/Operation/ConcreteClasses/AccumulatorLimitSet/"
            style AccumulatorLimitSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        AccumulatorLimit : AccumulatorLimit.value
        AccumulatorLimit : AccumulatorLimit.LimitSet
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * [Limit](/Models/Profiles/Operation/AbstractClasses/Limit/)
        * **AccumulatorLimit**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:AccumulatorLimit.value](http://iec.ch/TC57/CIM100#AccumulatorLimit.value) | No cardinality available integer | The value to supervise against. The value is positive. | direct |
| LimitSet | [cim:AccumulatorLimit.LimitSet](http://iec.ch/TC57/CIM100#AccumulatorLimit.LimitSet) | No cardinality available AccumulatorLimitSet | The set of limits. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
