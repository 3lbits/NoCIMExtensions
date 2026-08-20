# Limit

_Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:Limit](http://iec.ch/TC57/CIM100#Limit)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class Limit
    click Limit href "/Models/Profiles/Operation/AbstractClasses/Limit/"
    style Limit fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Limit <|-- AccumulatorLimit : inherits

        AccumulatorLimit
            click AccumulatorLimit href "/Models/Profiles/Operation/AbstractClasses/AccumulatorLimit/"
            style AccumulatorLimit fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Limit <|-- AnalogLimit : inherits

        AnalogLimit
            click AnalogLimit href "/Models/Profiles/Operation/ConcreteClasses/AnalogLimit/"
            style AnalogLimit fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Limit : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * **Limit**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
