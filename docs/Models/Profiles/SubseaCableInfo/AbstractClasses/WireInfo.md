# WireInfo

_Wire data that can be specified per line segment phase, or for the line segment as a whole in case its phases all have the same wire characteristics._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:WireInfo](http://iec.ch/TC57/CIM-generic#WireInfo)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class WireInfo
    click WireInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/WireInfo/"
    style WireInfo fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        WireInfo <|-- CableInfo : inherits

        CableInfo
            click CableInfo href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/CableInfo/"
            style CableInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductorInfo <|-- WireInfo : inherits
            click ConductorInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductorInfo/"
            style ConductorInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingAssetInfo <|-- ConductorInfo : inherits
            click ConductingAssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductingAssetInfo/"
            style ConductingAssetInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        AssetInfo <|-- ConductingAssetInfo : inherits
            click AssetInfo href "/Models/Profiles/SubseaCableInfo/AbstractClasses/AssetInfo/"
            style AssetInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- AssetInfo : inherits
            click IdentifiedObject href "/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AssetSpecification --> AssetInfo : AssetSpecification.AssetInfo

        AssetSpecification
            click AssetSpecification href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/AssetSpecification/"
            style AssetSpecification fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PerLengthConductorParameter --> ConductorInfo : PerLengthConductorParameter.ConductorInfo

        PerLengthConductorParameter
            click PerLengthConductorParameter href "/Models/Profiles/SubseaCableInfo/AbstractClasses/PerLengthConductorParameter/"
            style PerLengthConductorParameter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ProductAssetModel --> AssetInfo : ProductAssetModel.AssetInfo

        ProductAssetModel
            click ProductAssetModel href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ProductAssetModel/"
            style ProductAssetModel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ResistancePerLengthTemperaturePoint --> ConductorInfo : ResistancePerLengthTemperaturePoint.ConductorInfo

        ResistancePerLengthTemperaturePoint
            click ResistancePerLengthTemperaturePoint href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ResistancePerLengthTemperaturePoint/"
            style ResistancePerLengthTemperaturePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConductorInfo --> WireMaterialKind : ConductorInfo.material

        WireMaterialKind
            click WireMaterialKind href "/Models/Profiles/SubseaCableInfo/Enumerations/WireMaterialKind/"
            style WireMaterialKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

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
* [IdentifiedObject](/Models/Profiles/SubseaCableInfo/AbstractClasses/IdentifiedObject/)
    * [AssetInfo](/Models/Profiles/SubseaCableInfo/AbstractClasses/AssetInfo/)
        * [ConductingAssetInfo](/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductingAssetInfo/)
            * [ConductorInfo](/Models/Profiles/SubseaCableInfo/AbstractClasses/ConductorInfo/)
                * **WireInfo**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| coreRadius | [cim:WireInfo.coreRadius](http://iec.ch/TC57/CIM-generic#WireInfo.coreRadius) | 0..1 Length | (if there is a different core material) Radius of the central core. | direct |
| radius | [cim:WireInfo.radius](http://iec.ch/TC57/CIM-generic#WireInfo.radius) | 0..1 Length | Outside radius of the wire. | direct |
| crossSection | [cim:ConductorInfo.crossSection](http://iec.ch/TC57/CIM-generic#ConductorInfo.crossSection) | 0..1 Area | Area of conducting material cross section | ConductorInfo |
| material | [cim:ConductorInfo.material](http://iec.ch/TC57/CIM-generic#ConductorInfo.material) | 0..1 WireMaterialKind | Conductor material. | ConductorInfo |
| ratedCurrent | [cim:ConductingAssetInfo.ratedCurrent](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedCurrent) | 0..1 CurrentFlow | Rated current. | ConductingAssetInfo |
| ratedFrequency | [cim:ConductingAssetInfo.ratedFrequency](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedFrequency) | 0..1 Frequency | Rated frequency such as 50Hz or 60Hz | ConductingAssetInfo |
| ratedVoltage | [cim:ConductingAssetInfo.ratedVoltage](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedVoltage) | 0..1 Voltage | Rated voltage. | ConductingAssetInfo |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
