# AssetInfo

_Set of attributes of an asset, representing typical datasheet information of a physical device that can be instantiated and shared in different data exchange contexts:- as attributes of an asset instance (installed or in stock)- as attributes of an asset model (product by a manufacturer)- as attributes of a type asset (generic type of an asset as used in designs/extension planning)._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:AssetInfo](http://iec.ch/TC57/CIM-generic#AssetInfo)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AssetInfo
    click AssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/AssetInfo/"
    style AssetInfo fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AssetInfo <|-- ConductingAssetInfo : inherits

        ConductingAssetInfo
            click ConductingAssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductingAssetInfo/"
            style ConductingAssetInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- AssetInfo : inherits
            click IdentifiedObject href "/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AssetSpecification --> AssetInfo : AssetSpecification.AssetInfo

        AssetSpecification
            click AssetSpecification href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/AssetSpecification/"
            style AssetSpecification fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ProductAssetModel --> AssetInfo : ProductAssetModel.AssetInfo

        ProductAssetModel
            click ProductAssetModel href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ProductAssetModel/"
            style ProductAssetModel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/)
    * **AssetInfo**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
