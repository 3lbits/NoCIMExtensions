# IOPoint

_The class describe a measurement or control value. The purpose is to enable having attributes and associations common for measurement and control._

**URI**: [cim:IOPoint](http://iec.ch/TC57/CIM100#IOPoint)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class IOPoint
    click IOPoint href "/Models/Profiles/Operation/ConcreteClasses/IOPoint/"
    style IOPoint fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IOPoint <|-- Control : inherits

        Control
            click Control href "/Models/Profiles/Operation/ConcreteClasses/Control/"
            style Control fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IOPoint <|-- MeasurementValue : inherits

        MeasurementValue
            click MeasurementValue href "/Models/Profiles/Operation/ConcreteClasses/MeasurementValue/"
            style MeasurementValue fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- IOPoint : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/)
    * **IOPoint**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
