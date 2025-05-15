# CustomerNotification

_Conditions for notifying the customer about the changes in the status of their service (e.g., outage restore, estimated restoration time, tariff or service level change, etc.)_

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:CustomerNotification](http://iec.ch/TC57/CIM100#CustomerNotification)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class CustomerNotification
    click CustomerNotification href "/Models/Profiles/Outage/AbstractClasses/CustomerNotification/"
    style CustomerNotification fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CustomerNotification --> Customer : CustomerNotification.Customer

        Customer : Not defined in profile

        Customer
            style Customer fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        CustomerNotification --> Incident : CustomerNotification.Incident

        Incident
            click Incident href "/Models/Profiles/Outage/AbstractClasses/Incident/"
            style Incident fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CustomerNotification --> NotificationTriggerKind : CustomerNotification.trigger

        NotificationTriggerKind
            click NotificationTriggerKind href "/Models/Profiles/Outage/Enumerations/NotificationTriggerKind/"
            style NotificationTriggerKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CustomerNotification : CustomerNotification.contactType
        CustomerNotification : CustomerNotification.contactValue
        CustomerNotification : CustomerNotification.earliestDateTimeToCall
        CustomerNotification : CustomerNotification.latestDateTimeToCall
        CustomerNotification : CustomerNotification.trigger
        CustomerNotification : CustomerNotification.Customer
        CustomerNotification : CustomerNotification.Incident
```

## Inheritance
* **CustomerNotification**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| contactType | [cim:CustomerNotification.contactType](http://iec.ch/TC57/CIM100#CustomerNotification.contactType) | 0..1 string | Type of contact (e.g., phone, email, etc.). | direct |
| contactValue | [cim:CustomerNotification.contactValue](http://iec.ch/TC57/CIM100#CustomerNotification.contactValue) | 0..1 string | Value of contact type (e.g., phone number, email address, etc.). | direct |
| earliestDateTimeToCall | [cim:CustomerNotification.earliestDateTimeToCall](http://iec.ch/TC57/CIM100#CustomerNotification.earliestDateTimeToCall) | 0..1 datetime | Earliest date time to call the customer. | direct |
| latestDateTimeToCall | [cim:CustomerNotification.latestDateTimeToCall](http://iec.ch/TC57/CIM100#CustomerNotification.latestDateTimeToCall) | 0..1 datetime | Latest date time to call the customer. | direct |
| trigger | [cim:CustomerNotification.trigger](http://iec.ch/TC57/CIM100#CustomerNotification.trigger) | 0..1 NotificationTriggerKind | Trigger for this notification. | direct |
| Customer | [cim:CustomerNotification.Customer](http://iec.ch/TC57/CIM100#CustomerNotification.Customer) | 0..1 Customer | Customer requiring this notification. | direct |
| Incident | [cim:CustomerNotification.Incident](http://iec.ch/TC57/CIM100#CustomerNotification.Incident) | 0..1 Incident | Incident as a subject of this customer notification. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
