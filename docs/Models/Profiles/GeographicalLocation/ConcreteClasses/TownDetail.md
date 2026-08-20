# TownDetail

_Town details, in the context of address._

**URI**: [cim:TownDetail](http://iec.ch/TC57/CIM100#TownDetail)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class TownDetail
    click TownDetail href "/Models/Profiles/GeographicalLocation/ConcreteClasses/TownDetail/"
    style TownDetail fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        StreetAddress --> TownDetail : StreetAddress.townDetail

        StreetAddress
            click StreetAddress href "/Models/Profiles/GeographicalLocation/ConcreteClasses/StreetAddress/"
            style StreetAddress fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        TownDetail : TownDetail.code
        TownDetail : TownDetail.section
        TownDetail : TownDetail.name
        TownDetail : TownDetail.stateOrProvince
        TownDetail : TownDetail.country
```

## Inheritance
* **TownDetail**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| code | [cim:TownDetail.code](http://iec.ch/TC57/CIM100#TownDetail.code) | No cardinality available string | Town code. | direct |
| section | [cim:TownDetail.section](http://iec.ch/TC57/CIM100#TownDetail.section) | No cardinality available string | Town section. For example, it is common for there to be 36 sections per township. | direct |
| name | [cim:TownDetail.name](http://iec.ch/TC57/CIM100#TownDetail.name) | No cardinality available string | Town name. | direct |
| stateOrProvince | [cim:TownDetail.stateOrProvince](http://iec.ch/TC57/CIM100#TownDetail.stateOrProvince) | No cardinality available string | Name of the state or province. | direct |
| country | [cim:TownDetail.country](http://iec.ch/TC57/CIM100#TownDetail.country) | No cardinality available string | Name of the country. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile](http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile)
