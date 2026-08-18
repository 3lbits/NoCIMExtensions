# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM100#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/"
    style IdentifiedObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ACDCTerminal : inherits

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/Operation/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- IOPoint : inherits

        IOPoint
            click IOPoint href "/Models/Profiles/Operation/AbstractClasses/IOPoint/"
            style IOPoint fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- Limit : inherits

        Limit
            click Limit href "/Models/Profiles/Operation/AbstractClasses/Limit/"
            style Limit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- LimitSet : inherits

        LimitSet
            click LimitSet href "/Models/Profiles/Operation/ConcreteClasses/LimitSet/"
            style LimitSet fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- Measurement : inherits

        Measurement
            click Measurement href "/Models/Profiles/Operation/ConcreteClasses/Measurement/"
            style Measurement fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- MeasurementValueSource : inherits

        MeasurementValueSource
            click MeasurementValueSource href "/Models/Profiles/Operation/ConcreteClasses/MeasurementValueSource/"
            style MeasurementValueSource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- PowerSystemResource : inherits

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Operation/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ValueAliasSet : inherits

        ValueAliasSet
            click ValueAliasSet href "/Models/Profiles/Operation/ConcreteClasses/ValueAliasSet/"
            style ValueAliasSet fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ValueToAlias : inherits

        ValueToAlias
            click ValueToAlias href "/Models/Profiles/Operation/ConcreteClasses/ValueToAlias/"
            style ValueToAlias fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
