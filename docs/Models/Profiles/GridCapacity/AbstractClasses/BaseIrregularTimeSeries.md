# BaseIrregularTimeSeries

__

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:BaseIrregularTimeSeries](https://cim.ucaiug.io/ns#BaseIrregularTimeSeries)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class BaseIrregularTimeSeries
    click BaseIrregularTimeSeries href "/Models/Profiles/GridCapacity/AbstractClasses/BaseIrregularTimeSeries/"
    style BaseIrregularTimeSeries fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BaseIrregularTimeSeries <|-- CapacitySchedule : inherits

        CapacitySchedule
            click CapacitySchedule href "/Models/Profiles/GridCapacity/ConcreteClasses/CapacitySchedule/"
            style CapacitySchedule fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BaseIrregularTimeSeries <|-- CapacityTimePoint : inherits

        CapacityTimePoint
            click CapacityTimePoint href "/Models/Profiles/GridCapacity/ConcreteClasses/CapacityTimePoint/"
            style CapacityTimePoint fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        BaseTimeSeries <|-- BaseIrregularTimeSeries : inherits
            click BaseTimeSeries href "/Models/Profiles/GridCapacity/AbstractClasses/BaseTimeSeries/"
            style BaseTimeSeries fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- BaseTimeSeries : inherits
            click IdentifiedObject href "/Models/Profiles/GridCapacity/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        BaseTimeSeries --> TimeSeriesInterpolationKind : BaseTimeSeries.interpolationKind

        TimeSeriesInterpolationKind
            click TimeSeriesInterpolationKind href "/Models/Profiles/GridCapacity/Enumerations/TimeSeriesInterpolationKind/"
            style TimeSeriesInterpolationKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        BaseTimeSeries --> BaseTimeSeriesKind : BaseTimeSeries.timeSeriesKind

        BaseTimeSeriesKind
            click BaseTimeSeriesKind href "/Models/Profiles/GridCapacity/Enumerations/BaseTimeSeriesKind/"
            style BaseTimeSeriesKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

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
* [IdentifiedObject](/Models/Profiles/GridCapacity/AbstractClasses/IdentifiedObject/)
    * [BaseTimeSeries](/Models/Profiles/GridCapacity/AbstractClasses/BaseTimeSeries/)
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
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/GridCapacity/1.0](https://ap-no.cim4.eu/GridCapacity/1.0)
