# SwitchingPlan

_A sequence of grouped or atomic steps intended to:- de-energise equipment or part of the network for safe work, and/or- bring back in service previously de-energised equipment or part of the network._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:SwitchingPlan](http://iec.ch/TC57/CIM100#SwitchingPlan)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SwitchingPlan
    click SwitchingPlan href "/Models/Profiles/Outage/AbstractClasses/SwitchingPlan/"
    style SwitchingPlan fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Document <|-- SwitchingPlan : inherits
            click Document href "/Models/Profiles/Outage/AbstractClasses/Document/"
            style Document fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Document : inherits
            click IdentifiedObject href "/Models/Profiles/Outage/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SwitchingPlan --> Outage : SwitchingPlan.Outage

        Outage
            click Outage href "/Models/Profiles/Outage/AbstractClasses/Outage/"
            style Outage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivityRecord --> Document : ActivityRecord.Document

        ActivityRecord
            click ActivityRecord href "/Models/Profiles/Outage/AbstractClasses/ActivityRecord/"
            style ActivityRecord fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OutagePlan --> SwitchingPlan : OutagePlan.SwitchingPlan

        OutagePlan
            click OutagePlan href "/Models/Profiles/Outage/AbstractClasses/OutagePlan/"
            style OutagePlan fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SwitchingPlan : SwitchingPlan.approvedDateTime
        SwitchingPlan : SwitchingPlan.cancelledDateTime
        SwitchingPlan : SwitchingPlan.purpose
        SwitchingPlan : SwitchingPlan.rank
        SwitchingPlan : SwitchingPlan.Outage
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
    * [Document](/Models/Profiles/Outage/AbstractClasses/Document/)
        * **SwitchingPlan**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| approvedDateTime | [cim:SwitchingPlan.approvedDateTime](http://iec.ch/TC57/CIM100#SwitchingPlan.approvedDateTime) | 0..1 datetime | The date and time the switching plan was approved | direct |
| cancelledDateTime | [cim:SwitchingPlan.cancelledDateTime](http://iec.ch/TC57/CIM100#SwitchingPlan.cancelledDateTime) | 0..1 datetime | Date and Time the switching plan was cancelled. | direct |
| purpose | [cim:SwitchingPlan.purpose](http://iec.ch/TC57/CIM100#SwitchingPlan.purpose) | 0..1 string | Purpose of  this plan, such as whether it is to move the state from normal to some abnormal condition, or to restore the normal state after an abnormal condition, or to perform some kind of optimisation such as correction of overload, voltage control, etc. | direct |
| rank | [cim:SwitchingPlan.rank](http://iec.ch/TC57/CIM100#SwitchingPlan.rank) | 0..1 integer | Ranking in comparison to other switching plans. | direct |
| Outage | [cim:SwitchingPlan.Outage](http://iec.ch/TC57/CIM100#SwitchingPlan.Outage) | 0..1 Outage | Outage that will be activated or eliminated when this switching plan gets executed. | direct |
| authorName | [cim:Document.authorName](http://iec.ch/TC57/CIM100#Document.authorName) | 0..1 string | Name of the author of this document. | Document |
| comment | [cim:Document.comment](http://iec.ch/TC57/CIM100#Document.comment) | 0..1 string | Free text comment. | Document |
| createdDateTime | [cim:Document.createdDateTime](http://iec.ch/TC57/CIM100#Document.createdDateTime) | 0..1 datetime | Date and time that this document was created. | Document |
| lastModifiedDateTime | [cim:Document.lastModifiedDateTime](http://iec.ch/TC57/CIM100#Document.lastModifiedDateTime) | 0..1 datetime | Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. | Document |
| revisionNumber | [cim:Document.revisionNumber](http://iec.ch/TC57/CIM100#Document.revisionNumber) | 0..1 string | Revision number for this document. | Document |
| subject | [cim:Document.subject](http://iec.ch/TC57/CIM100#Document.subject) | 0..1 string | Document subject. | Document |
| title | [cim:Document.title](http://iec.ch/TC57/CIM100#Document.title) | 0..1 string | Document title. | Document |
| type | [cim:Document.type](http://iec.ch/TC57/CIM100#Document.type) | 0..1 string | Utility-specific classification of this document, according to its corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). | Document |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| aliasName | [cim:IdentifiedObject.aliasName](http://iec.ch/TC57/CIM100#IdentifiedObject.aliasName) | 0..1 string | The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The attribute aliasName is retained because of backwards compatibility between CIM relases. It is however recommended to replace aliasName with the Name class as aliasName is planned for retirement at a future time. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
