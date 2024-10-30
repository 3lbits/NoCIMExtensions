# ProductAssetModel

_Asset model by a specific manufacturer._

**URI**: [cim:ProductAssetModel](http://iec.ch/TC57/CIM-generic#ProductAssetModel)<br />
**Type**: Class

```mermaid
classDiagram
    class ProductAssetModel
    click ProductAssetModel href "../ProductAssetModel"
    style ProductAssetModel fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        IdentifiedObject <|-- ProductAssetModel : inherits
            click IdentifiedObject href "../IdentifiedObject"
            style IdentifiedObject rx:10,ry:10

        ProductAssetModel
            click ProductAssetModel href "../ProductAssetModel"
            style ProductAssetModel rx:10,ry:10

        ProductAssetModel --> AssetInfo : ProductAssetModel.AssetInfo

        AssetInfo
            click AssetInfo href "../AssetInfo"
            style AssetInfo fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10
        ProductAssetModel --> Manufacturer : ProductAssetModel.Manufacturer

        Manufacturer
            click Manufacturer href "../Manufacturer"
            style Manufacturer fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        ProductAssetModel : ProductAssetModel.AssetInfo
        ProductAssetModel : ProductAssetModel.Manufacturer
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **ProductAssetModel**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| AssetInfo | [cim:ProductAssetModel.AssetInfo](http://iec.ch/TC57/CIM-generic#ProductAssetModel.AssetInfo) | 0..1 | Asset information (nameplate) for this product asset model. | direct |
| Manufacturer | [cim:ProductAssetModel.Manufacturer](http://iec.ch/TC57/CIM-generic#ProductAssetModel.Manufacturer) | 0..1 | Manufacturer of this asset model. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
