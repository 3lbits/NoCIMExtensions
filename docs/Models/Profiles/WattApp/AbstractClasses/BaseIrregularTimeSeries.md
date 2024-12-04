# BaseIrregularTimeSeries

__

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:BaseIrregularTimeSeries](https://cim.ucaiug.io/ns#BaseIrregularTimeSeries)<br />
**Type**: Class

```mermaid
classDiagram
    class BaseIrregularTimeSeries
    click BaseIrregularTimeSeries href "/Models/Profiles/WattApp/AbstractClasses/BaseIrregularTimeSeries/"
    style BaseIrregularTimeSeries fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        BaseIrregularTimeSeries <|-- CapacitySchedule : inherits
            click BaseIrregularTimeSeries href "/Models/Profiles/WattApp/AbstractClasses/BaseIrregularTimeSeries/"
            style BaseIrregularTimeSeries rx:10,ry:10

        CapacitySchedule
            click CapacitySchedule href "/Models/Profiles/WattApp/ConcreteClasses/CapacitySchedule/"
            style CapacitySchedule rx:10,ry:10

        BaseTimeSeries <|-- BaseIrregularTimeSeries : inherits
            click BaseTimeSeries href "/Models/Profiles/WattApp/AbstractClasses/BaseTimeSeries/"
            style BaseTimeSeries rx:10,ry:10

        IdentifiedObject <|-- BaseTimeSeries : inherits
            click IdentifiedObject href "/Models/Profiles/WattApp/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10


        BaseTimeSeries --> TimeSeriesInterpolationKind : BaseTimeSeries.interpolationKind

        TimeSeriesInterpolationKind
            click TimeSeriesInterpolationKind href "/Models/Profiles/WattApp/Enumerations/TimeSeriesInterpolationKind/"
            style TimeSeriesInterpolationKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        BaseTimeSeries --> BaseTimeSeriesKind : BaseTimeSeries.timeSeriesKind

        BaseTimeSeriesKind
            click BaseTimeSeriesKind href "/Models/Profiles/WattApp/Enumerations/BaseTimeSeriesKind/"
            style BaseTimeSeriesKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        BaseTimeSeries : BaseTimeSeries.interpolationKind
        BaseTimeSeries : BaseTimeSeries.timeSeriesKind
        BaseTimeSeries : BaseTimeSeries.generatedAtTime
        BaseTimeSeries : BaseTimeSeries.percentile
        BaseTimeSeries : BaseTimeSeries.actionMethod
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [BaseTimeSeries](BaseTimeSeries.md)
        * **BaseIrregularTimeSeries**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| interpolationKind | [nc:BaseTimeSeries.interpolationKind](https://cim4.eu/ns/nc#BaseTimeSeries.interpolationKind) | 0..1 TimeSeriesInterpolationKind |  | BaseTimeSeries |
| timeSeriesKind | [nc:BaseTimeSeries.timeSeriesKind](https://cim4.eu/ns/nc#BaseTimeSeries.timeSeriesKind) | 0..1 BaseTimeSeriesKind |  | BaseTimeSeries |
| generatedAtTime | [nc:BaseTimeSeries.generatedAtTime](https://cim4.eu/ns/nc#BaseTimeSeries.generatedAtTime) | 0..1 DateTime |  | BaseTimeSeries |
| percentile | [nc:BaseTimeSeries.percentile](https://cim4.eu/ns/nc#BaseTimeSeries.percentile) | 0..1 integer |  | BaseTimeSeries |
| actionMethod | [nc:BaseTimeSeries.actionMethod](https://cim4.eu/ns/nc#BaseTimeSeries.actionMethod) | 0..1 string |  | BaseTimeSeries |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
