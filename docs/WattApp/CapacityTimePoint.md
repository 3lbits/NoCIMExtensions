# CapacityTimePoint

__

**URI**: [nc:CapacityTimePoint](https://cim4.eu/ns/nc#CapacityTimePoint)<br />
**Type**: Class

```mermaid
classDiagram
    class CapacityTimePoint
    click CapacityTimePoint href "../CapacityTimePoint"
    style CapacityTimePoint fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        BaseIrregularTimeSeries <|-- CapacityTimePoint : inherits
            click BaseIrregularTimeSeries href "../BaseIrregularTimeSeries"
            style BaseIrregularTimeSeries rx:10,ry:10

        CapacityTimePoint
            click CapacityTimePoint href "../CapacityTimePoint"
            style CapacityTimePoint rx:10,ry:10

        BaseTimeSeries <|-- BaseIrregularTimeSeries : inherits
            click BaseTimeSeries href "../BaseTimeSeries"
            style BaseTimeSeries rx:10,ry:10

        IdentifiedObject <|-- BaseTimeSeries : inherits
            click IdentifiedObject href "../IdentifiedObject"
            style IdentifiedObject rx:10,ry:10

        CapacityTimePoint --> CapacitySchedule : CapacityTimePoint.CapacitySchedule

        CapacitySchedule
            click CapacitySchedule href "../CapacitySchedule"
            style CapacitySchedule fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        BaseTimeSeries --> TimeSeriesInterpolationKind : BaseTimeSeries.interpolationKind

        TimeSeriesInterpolationKind
            click TimeSeriesInterpolationKind href "../TimeSeriesInterpolationKind"
            style TimeSeriesInterpolationKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        BaseTimeSeries --> BaseTimeSeriesKind : BaseTimeSeries.timeSeriesKind

        BaseTimeSeriesKind
            click BaseTimeSeriesKind href "../BaseTimeSeriesKind"
            style BaseTimeSeriesKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        CapacityTimePoint : CapacityTimePoint.atTime
        CapacityTimePoint : CapacityTimePoint.maxP
        CapacityTimePoint : CapacityTimePoint.minP
        CapacityTimePoint : CapacityTimePoint.maxQ
        CapacityTimePoint : CapacityTimePoint.minQ
        CapacityTimePoint : CapacityTimePoint.maxAllocatedP
        CapacityTimePoint : CapacityTimePoint.minAllocatedP
        CapacityTimePoint : CapacityTimePoint.maxAllocatedQ
        CapacityTimePoint : CapacityTimePoint.minAllocatedQ
        CapacityTimePoint : CapacityTimePoint.CapacitySchedule
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
        * [BaseIrregularTimeSeries](BaseIrregularTimeSeries.md)
            * **CapacityTimePoint**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| atTime | [nc:CapacityTimePoint.atTime](https://cim4.eu/ns/nc#CapacityTimePoint.atTime) | 0..1 |  | direct |
| maxP | [nc:CapacityTimePoint.maxP](https://cim4.eu/ns/nc#CapacityTimePoint.maxP) | 0..1 |  | direct |
| minP | [nc:CapacityTimePoint.minP](https://cim4.eu/ns/nc#CapacityTimePoint.minP) | 0..1 |  | direct |
| maxQ | [nc:CapacityTimePoint.maxQ](https://cim4.eu/ns/nc#CapacityTimePoint.maxQ) | 0..1 |  | direct |
| minQ | [nc:CapacityTimePoint.minQ](https://cim4.eu/ns/nc#CapacityTimePoint.minQ) | 0..1 |  | direct |
| maxAllocatedP | [nc:CapacityTimePoint.maxAllocatedP](https://cim4.eu/ns/nc#CapacityTimePoint.maxAllocatedP) | 0..1 |  | direct |
| minAllocatedP | [nc:CapacityTimePoint.minAllocatedP](https://cim4.eu/ns/nc#CapacityTimePoint.minAllocatedP) | 0..1 |  | direct |
| maxAllocatedQ | [nc:CapacityTimePoint.maxAllocatedQ](https://cim4.eu/ns/nc#CapacityTimePoint.maxAllocatedQ) | 0..1 |  | direct |
| minAllocatedQ | [nc:CapacityTimePoint.minAllocatedQ](https://cim4.eu/ns/nc#CapacityTimePoint.minAllocatedQ) | 0..1 |  | direct |
| CapacitySchedule | [nc:CapacityTimePoint.CapacitySchedule](https://cim4.eu/ns/nc#CapacityTimePoint.CapacitySchedule) | 0..1 |  | direct |
| interpolationKind | [nc:BaseTimeSeries.interpolationKind](https://cim4.eu/ns/nc#BaseTimeSeries.interpolationKind) | 0..1 |  | BaseTimeSeries |
| timeSeriesKind | [nc:BaseTimeSeries.timeSeriesKind](https://cim4.eu/ns/nc#BaseTimeSeries.timeSeriesKind) | 0..1 |  | BaseTimeSeries |
| generatedAtTime | [nc:BaseTimeSeries.generatedAtTime](https://cim4.eu/ns/nc#BaseTimeSeries.generatedAtTime) | 0..1 |  | BaseTimeSeries |
| percentile | [nc:BaseTimeSeries.percentile](https://cim4.eu/ns/nc#BaseTimeSeries.percentile) | 0..1 |  | BaseTimeSeries |
| actionMethod | [nc:BaseTimeSeries.actionMethod](https://cim4.eu/ns/nc#BaseTimeSeries.actionMethod) | 0..1 |  | BaseTimeSeries |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
