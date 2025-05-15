# PSREvent

_Event recording the change in operational status of a power system resource (PSR); may be for an event that has already occurred or for a planned activity._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:PSREvent](http://iec.ch/TC57/CIM100#PSREvent)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PSREvent
    click PSREvent href "/Models/Profiles/Outage/AbstractClasses/PSREvent/"
    style PSREvent fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ActivityRecord <|-- PSREvent : inherits
            click ActivityRecord href "/Models/Profiles/Outage/AbstractClasses/ActivityRecord/"
            style ActivityRecord fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ActivityRecord : inherits
            click IdentifiedObject href "/Models/Profiles/Outage/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PSREvent --> PSREventKind : PSREvent.kind

        PSREventKind : Not defined in profile

        PSREventKind
            style PSREventKind fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PSREvent --> PowerSystemResource : PSREvent.PowerSystemResource

        PowerSystemResource : Not defined in profile

        PowerSystemResource
            style PowerSystemResource fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivityRecord --> Document : ActivityRecord.Document

        Document
            click Document href "/Models/Profiles/Outage/AbstractClasses/Document/"
            style Document fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PSREvent : PSREvent.kind
        PSREvent : PSREvent.PowerSystemResource
        ActivityRecord : ActivityRecord.createdDateTime
        ActivityRecord : ActivityRecord.reason
        ActivityRecord : ActivityRecord.severity
        ActivityRecord : ActivityRecord.type
        ActivityRecord : ActivityRecord.Document
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.aliasName
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Outage/AbstractClasses/IdentifiedObject/)
    * [ActivityRecord](/Models/Profiles/Outage/AbstractClasses/ActivityRecord/)
        * **PSREvent**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| kind | [cim:PSREvent.kind](http://iec.ch/TC57/CIM100#PSREvent.kind) | 0..1 PSREventKind | Kind of event. | direct |
| PowerSystemResource | [cim:PSREvent.PowerSystemResource](http://iec.ch/TC57/CIM100#PSREvent.PowerSystemResource) | 0..1 PowerSystemResource | Power system resource that generated this event. | direct |
| createdDateTime | [cim:ActivityRecord.createdDateTime](http://iec.ch/TC57/CIM100#ActivityRecord.createdDateTime) | 0..1 datetime | Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). | ActivityRecord |
| reason | [cim:ActivityRecord.reason](http://iec.ch/TC57/CIM100#ActivityRecord.reason) | 0..1 string | Reason for event resulting in this activity record, typically supplied when user initiated. | ActivityRecord |
| severity | [cim:ActivityRecord.severity](http://iec.ch/TC57/CIM100#ActivityRecord.severity) | 0..1 string | Severity level of event resulting in this activity record. | ActivityRecord |
| type | [cim:ActivityRecord.type](http://iec.ch/TC57/CIM100#ActivityRecord.type) | 0..1 string | Type of event resulting in this activity record. | ActivityRecord |
| Document | [cim:ActivityRecord.Document](http://iec.ch/TC57/CIM100#ActivityRecord.Document) | 0..1 Document | The document having associated activity records | ActivityRecord |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| aliasName | [cim:IdentifiedObject.aliasName](http://iec.ch/TC57/CIM100#IdentifiedObject.aliasName) | 0..1 string | The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The attribute aliasName is retained because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
