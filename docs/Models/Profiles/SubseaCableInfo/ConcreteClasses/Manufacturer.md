# Manufacturer

_Organisation that manufactures asset products._

**URI**: [cim:Manufacturer](http://iec.ch/TC57/CIM-generic#Manufacturer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Manufacturer
    click Manufacturer href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/Manufacturer/"
    style Manufacturer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        OrganisationRole <|-- Manufacturer : inherits
            click OrganisationRole href "/Models/Profiles/SubseaCableInfo/AbstractClasses/OrganisationRole/"
            style OrganisationRole fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- OrganisationRole : inherits
            click IdentifiedObject href "/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ProductAssetModel --> Manufacturer : ProductAssetModel.Manufacturer

        ProductAssetModel
            click ProductAssetModel href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ProductAssetModel/"
            style ProductAssetModel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/)
    * [OrganisationRole](/Models/Profiles/SubseaCableInfo/AbstractClasses/OrganisationRole/)
        * **Manufacturer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
