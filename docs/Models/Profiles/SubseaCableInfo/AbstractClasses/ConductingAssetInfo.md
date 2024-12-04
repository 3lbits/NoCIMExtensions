# ConductingAssetInfo

_Generic information for conducting asset_

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConductingAssetInfo](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo)<br />
**Type**: Class

```mermaid
classDiagram
    class ConductingAssetInfo
    click ConductingAssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductingAssetInfo/"
    style ConductingAssetInfo fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ConductingAssetInfo <|-- ConductorInfo : inherits
            click ConductingAssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductingAssetInfo/"
            style ConductingAssetInfo rx:10,ry:10

        ConductorInfo
            click ConductorInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductorInfo/"
            style ConductorInfo rx:10,ry:10

        AssetInfo <|-- ConductingAssetInfo : inherits
            click AssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/AssetInfo/"
            style AssetInfo rx:10,ry:10

        IdentifiedObject <|-- AssetInfo : inherits
            click IdentifiedObject href "/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10


        AssetSpecification --> AssetInfo : AssetSpecification.AssetInfo

        AssetSpecification
            click AssetSpecification href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/AssetSpecification/"
            style AssetSpecification fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ProductAssetModel --> AssetInfo : ProductAssetModel.AssetInfo

        ProductAssetModel
            click ProductAssetModel href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ProductAssetModel/"
            style ProductAssetModel fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        ConductingAssetInfo : ConductingAssetInfo.ratedCurrent
        ConductingAssetInfo : ConductingAssetInfo.ratedFrequency
        ConductingAssetInfo : ConductingAssetInfo.ratedVoltage
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [AssetInfo](AssetInfo.md)
        * **ConductingAssetInfo**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ratedCurrent | [cim:ConductingAssetInfo.ratedCurrent](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedCurrent) | 0..1 CurrentFlow | Rated current. | direct |
| ratedFrequency | [cim:ConductingAssetInfo.ratedFrequency](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedFrequency) | 0..1 Frequency | Rated frequency such as 50Hz or 60Hz | direct |
| ratedVoltage | [cim:ConductingAssetInfo.ratedVoltage](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedVoltage) | 0..1 Voltage | Rated voltage. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
