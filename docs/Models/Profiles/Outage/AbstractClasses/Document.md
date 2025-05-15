# Document

_Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:Document](http://iec.ch/TC57/CIM100#Document)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Document
    click Document href "/Models/Profiles/Outage/AbstractClasses/Document/"
    style Document fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Document <|-- Incident : inherits

        Incident
            click Incident href "/Models/Profiles/Outage/AbstractClasses/Incident/"
            style Incident fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Document <|-- Outage : inherits

        Outage
            click Outage href "/Models/Profiles/Outage/AbstractClasses/Outage/"
            style Outage fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Document <|-- OutagePlan : inherits

        OutagePlan
            click OutagePlan href "/Models/Profiles/Outage/AbstractClasses/OutagePlan/"
            style OutagePlan fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Document <|-- SwitchingPlan : inherits

        SwitchingPlan
            click SwitchingPlan href "/Models/Profiles/Outage/AbstractClasses/SwitchingPlan/"
            style SwitchingPlan fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Document : inherits
            click IdentifiedObject href "/Models/Profiles/Outage/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ActivityRecord --> Document : ActivityRecord.Document

        ActivityRecord
            click ActivityRecord href "/Models/Profiles/Outage/AbstractClasses/ActivityRecord/"
            style ActivityRecord fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Document : Document.authorName
        Document : Document.comment
        Document : Document.createdDateTime
        Document : Document.lastModifiedDateTime
        Document : Document.revisionNumber
        Document : Document.subject
        Document : Document.title
        Document : Document.type
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.aliasName
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Outage/AbstractClasses/IdentifiedObject/)
    * **Document**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| authorName | [cim:Document.authorName](http://iec.ch/TC57/CIM100#Document.authorName) | 0..1 string | Name of the author of this document. | direct |
| comment | [cim:Document.comment](http://iec.ch/TC57/CIM100#Document.comment) | 0..1 string | Free text comment. | direct |
| createdDateTime | [cim:Document.createdDateTime](http://iec.ch/TC57/CIM100#Document.createdDateTime) | 0..1 datetime | Date and time that this document was created. | direct |
| lastModifiedDateTime | [cim:Document.lastModifiedDateTime](http://iec.ch/TC57/CIM100#Document.lastModifiedDateTime) | 0..1 datetime | Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. | direct |
| revisionNumber | [cim:Document.revisionNumber](http://iec.ch/TC57/CIM100#Document.revisionNumber) | 0..1 string | Revision number for this document. | direct |
| subject | [cim:Document.subject](http://iec.ch/TC57/CIM100#Document.subject) | 0..1 string | Document subject. | direct |
| title | [cim:Document.title](http://iec.ch/TC57/CIM100#Document.title) | 0..1 string | Document title. | direct |
| type | [cim:Document.type](http://iec.ch/TC57/CIM100#Document.type) | 0..1 string | Utility-specific classification of this document, according to its corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| aliasName | [cim:IdentifiedObject.aliasName](http://iec.ch/TC57/CIM100#IdentifiedObject.aliasName) | 0..1 string | The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The attribute aliasName is retained because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
