# MultiCoreCableInfo

_No description available_

**URI**: [cim:MultiCoreCableInfo](http://iec.ch/TC57/CIM-generic#MultiCoreCableInfo)<br />
**Type**: Class

```mermaid
classDiagram
    class MultiCoreCableInfo
    click MultiCoreCableInfo href "../MultiCoreCableInfo"
    style MultiCoreCableInfo fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        CableInfo <|-- MultiCoreCableInfo : inherits
            click CableInfo href "../CableInfo"
            style CableInfo rx:10,ry:10

        MultiCoreCableInfo
            click MultiCoreCableInfo href "../MultiCoreCableInfo"
            style MultiCoreCableInfo rx:10,ry:10

        WireInfo <|-- CableInfo : inherits
            click WireInfo href "../WireInfo"
            style WireInfo rx:10,ry:10

        ConductorInfo <|-- WireInfo : inherits
            click ConductorInfo href "../ConductorInfo"
            style ConductorInfo rx:10,ry:10

        ConductingAssetInfo <|-- ConductorInfo : inherits
            click ConductingAssetInfo href "../ConductingAssetInfo"
            style ConductingAssetInfo rx:10,ry:10

        AssetInfo <|-- ConductingAssetInfo : inherits
            click AssetInfo href "../AssetInfo"
            style AssetInfo rx:10,ry:10

        IdentifiedObject <|-- AssetInfo : inherits
            click IdentifiedObject href "../IdentifiedObject"
            style IdentifiedObject rx:10,ry:10

        MultiCoreCableInfo --> CableLayer : MultiCoreCableInfo.BeltedLayer

        CableLayer
            click CableLayer href "../CableLayer"
            style CableLayer fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10
        CableInfo --> CableLayer : CableInfo.Layer

        CableLayer
            click CableLayer href "../CableLayer"
            style CableLayer fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        AssetSpecification --> AssetInfo : AssetSpecification.AssetInfo

        AssetSpecification
            click AssetSpecification href "../AssetSpecification"
            style AssetSpecification fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        PerLengthConductorParameter --> ConductorInfo : PerLengthConductorParameter.ConductorInfo

        PerLengthConductorParameter
            click PerLengthConductorParameter href "../PerLengthConductorParameter"
            style PerLengthConductorParameter fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ProductAssetModel --> AssetInfo : ProductAssetModel.AssetInfo

        ProductAssetModel
            click ProductAssetModel href "../ProductAssetModel"
            style ProductAssetModel fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ResistancePerLengthTemperaturePoint --> ConductorInfo : ResistancePerLengthTemperaturePoint.ConductorInfo

        ResistancePerLengthTemperaturePoint
            click ResistancePerLengthTemperaturePoint href "../ResistancePerLengthTemperaturePoint"
            style ResistancePerLengthTemperaturePoint fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        ConductorInfo --> WireMaterialKind : ConductorInfo.material

        WireMaterialKind
            click WireMaterialKind href "../WireMaterialKind"
            style WireMaterialKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        MultiCoreCableInfo : MultiCoreCableInfo.layLength
        MultiCoreCableInfo : MultiCoreCableInfo.BeltedLayer
        CableInfo : CableInfo.lossFactorArmour
        CableInfo : CableInfo.lossFactorSheathScreen
        CableInfo : CableInfo.nominalTemperature
        CableInfo : CableInfo.Layer
        WireInfo : WireInfo.coreRadius
        WireInfo : WireInfo.radius
        ConductorInfo : ConductorInfo.crossSection
        ConductorInfo : ConductorInfo.material
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
        * [ConductingAssetInfo](ConductingAssetInfo.md)
            * [ConductorInfo](ConductorInfo.md)
                * [WireInfo](WireInfo.md)
                    * [CableInfo](CableInfo.md)
                        * **MultiCoreCableInfo**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| layLength | [cim:MultiCoreCableInfo.layLength](http://iec.ch/TC57/CIM-generic#MultiCoreCableInfo.layLength) | 0..1 | Longitudinal distance required for core to perform one turn around the diameter of the cable. | direct |
| BeltedLayer | [cim:MultiCoreCableInfo.BeltedLayer](http://iec.ch/TC57/CIM-generic#MultiCoreCableInfo.BeltedLayer) | 0..* | No description available | direct |
| lossFactorArmour | [cim:CableInfo.lossFactorArmour](http://iec.ch/TC57/CIM-generic#CableInfo.lossFactorArmour) | 0..1 | No description available | CableInfo |
| lossFactorSheathScreen | [cim:CableInfo.lossFactorSheathScreen](http://iec.ch/TC57/CIM-generic#CableInfo.lossFactorSheathScreen) | 0..1 | No description available | CableInfo |
| nominalTemperature | [cim:CableInfo.nominalTemperature](http://iec.ch/TC57/CIM-generic#CableInfo.nominalTemperature) | 0..1 | Maximum nominal design operating temperature. | CableInfo |
| Layer | [cim:CableInfo.Layer](http://iec.ch/TC57/CIM-generic#CableInfo.Layer) | 0..* | No description available | CableInfo |
| coreRadius | [cim:WireInfo.coreRadius](http://iec.ch/TC57/CIM-generic#WireInfo.coreRadius) | 0..1 | (if there is a different core material) Radius of the central core. | WireInfo |
| radius | [cim:WireInfo.radius](http://iec.ch/TC57/CIM-generic#WireInfo.radius) | 0..1 | Outside radius of the wire. | WireInfo |
| crossSection | [cim:ConductorInfo.crossSection](http://iec.ch/TC57/CIM-generic#ConductorInfo.crossSection) | 0..1 | Area of conducting material cross section | ConductorInfo |
| material | [cim:ConductorInfo.material](http://iec.ch/TC57/CIM-generic#ConductorInfo.material) | 0..1 | Conductor material. | ConductorInfo |
| ratedCurrent | [cim:ConductingAssetInfo.ratedCurrent](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedCurrent) | 0..1 | Rated current. | ConductingAssetInfo |
| ratedFrequency | [cim:ConductingAssetInfo.ratedFrequency](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedFrequency) | 0..1 | Rated frequency such as 50Hz or 60Hz | ConductingAssetInfo |
| ratedVoltage | [cim:ConductingAssetInfo.ratedVoltage](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedVoltage) | 0..1 | Rated voltage. | ConductingAssetInfo |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile#](http://iec.ch/TC57/2007/profile#)
