# StreetAddress

_General purpose street and postal address information._

**URI**: [cim:StreetAddress](http://iec.ch/TC57/CIM100#StreetAddress)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class StreetAddress
    click StreetAddress href "/Models/Profiles/GeographicalLocation/ConcreteClasses/StreetAddress/"
    style StreetAddress fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        StreetAddress --> StreetDetail : StreetAddress.streetDetail

        StreetDetail
            click StreetDetail href "/Models/Profiles/GeographicalLocation/ConcreteClasses/StreetDetail/"
            style StreetDetail fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        StreetAddress --> TownDetail : StreetAddress.townDetail

        TownDetail
            click TownDetail href "/Models/Profiles/GeographicalLocation/ConcreteClasses/TownDetail/"
            style TownDetail fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        StreetAddress --> Status : StreetAddress.status

        Status
            click Status href "/Models/Profiles/GeographicalLocation/ConcreteClasses/Status/"
            style Status fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Location --> StreetAddress : Location.mainAddress

        Location
            click Location href "/Models/Profiles/GeographicalLocation/ConcreteClasses/Location/"
            style Location fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        StreetAddress : StreetAddress.streetDetail
        StreetAddress : StreetAddress.townDetail
        StreetAddress : StreetAddress.status
        StreetAddress : StreetAddress.postalCode
        StreetAddress : StreetAddress.poBox
        StreetAddress : StreetAddress.language
```

## Inheritance
* **StreetAddress**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| streetDetail | [cim:StreetAddress.streetDetail](http://iec.ch/TC57/CIM100#StreetAddress.streetDetail) | No cardinality available StreetDetail | Street detail. | direct |
| townDetail | [cim:StreetAddress.townDetail](http://iec.ch/TC57/CIM100#StreetAddress.townDetail) | No cardinality available TownDetail | Town detail. | direct |
| status | [cim:StreetAddress.status](http://iec.ch/TC57/CIM100#StreetAddress.status) | No cardinality available Status | Status of this address. | direct |
| postalCode | [cim:StreetAddress.postalCode](http://iec.ch/TC57/CIM100#StreetAddress.postalCode) | No cardinality available string | Postal code for the address. | direct |
| poBox | [cim:StreetAddress.poBox](http://iec.ch/TC57/CIM100#StreetAddress.poBox) | No cardinality available string | Post office box. | direct |
| language | [cim:StreetAddress.language](http://iec.ch/TC57/CIM100#StreetAddress.language) | No cardinality available string | The language in which the address is specified, using ISO 639-1 two digit language code. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile](http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile)
