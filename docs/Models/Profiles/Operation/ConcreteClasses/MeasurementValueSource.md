# MeasurementValueSource

_MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are defined in IEC 61970-301._

**URI**: [cim:MeasurementValueSource](http://iec.ch/TC57/CIM100#MeasurementValueSource)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class MeasurementValueSource
    click MeasurementValueSource href "/Models/Profiles/Operation/ConcreteClasses/MeasurementValueSource/"
    style MeasurementValueSource fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- MeasurementValueSource : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MeasurementValueSource --> MeasurementValue : MeasurementValueSource.MeasurementValues

        MeasurementValue
            click MeasurementValue href "/Models/Profiles/Operation/AbstractClasses/MeasurementValue/"
            style MeasurementValue fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MeasurementValue --> MeasurementValueSource : MeasurementValue.MeasurementValueSource

        MeasurementValue
            click MeasurementValue href "/Models/Profiles/Operation/AbstractClasses/MeasurementValue/"
            style MeasurementValue fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        MeasurementValueSource : MeasurementValueSource.MeasurementValues
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * **MeasurementValueSource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| MeasurementValues | [cim:MeasurementValueSource.MeasurementValues](http://iec.ch/TC57/CIM100#MeasurementValueSource.MeasurementValues) | No cardinality available MeasurementValue | The MeasurementValues updated by the source. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
