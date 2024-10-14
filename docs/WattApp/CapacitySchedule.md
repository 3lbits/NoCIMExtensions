# CapacitySchedule



**URI**: [nc:CapacitySchedule](http://entsoe.eu/ns/nc#CapacitySchedule)<br />
**Type**: Class




```mermaid
 classDiagram
    class CapacitySchedule
    click CapacitySchedule href "../CapacitySchedule"
      BaseIrregularTimeSeries <|-- CapacitySchedule
        click BaseIrregularTimeSeries href "../BaseIrregularTimeSeries"
      
      CapacitySchedule : BaseTimeSeries.actionMethod
        
      CapacitySchedule : IdentifiedObject.description
        
      CapacitySchedule : CapacitySchedule.Feeder
        
          CapacitySchedule --> Feeder : CapacitySchedule.Feeder
          click Feeder href "../Feeder"
        
      CapacitySchedule : BaseTimeSeries.generatedAtTime
        
      CapacitySchedule : BaseTimeSeries.interpolationKind
        
          CapacitySchedule --> TimeSeriesInterpolationKind : BaseTimeSeries.interpolationKind
          click TimeSeriesInterpolationKind href "../TimeSeriesInterpolationKind"
        
      CapacitySchedule : IdentifiedObject.mRID
        
      CapacitySchedule : IdentifiedObject.name
        
      CapacitySchedule : BaseTimeSeries.percentile
        
      CapacitySchedule : BaseTimeSeries.timeSeriesKind
        
          CapacitySchedule --> BaseTimeSeriesKind : BaseTimeSeries.timeSeriesKind
          click BaseTimeSeriesKind href "../BaseTimeSeriesKind"
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [BaseTimeSeries](BaseTimeSeries.md)
        * [BaseIrregularTimeSeries](BaseIrregularTimeSeries.md)
            * **CapacitySchedule**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Feeder | [nc:CapacitySchedule.Feeder](http://entsoe.eu/ns/nc#CapacitySchedule.Feeder) | 0..1 <br />  [Feeder](Feeder.md)  |  | direct |
| interpolationKind | [nc:BaseTimeSeries.interpolationKind](http://entsoe.eu/ns/nc#BaseTimeSeries.interpolationKind) | 0..1 <br />  [TimeSeriesInterpolationKind](TimeSeriesInterpolationKind.md)  |  | [BaseTimeSeries](BaseTimeSeries.md) |
| timeSeriesKind | [nc:BaseTimeSeries.timeSeriesKind](http://entsoe.eu/ns/nc#BaseTimeSeries.timeSeriesKind) | 0..1 <br />  [BaseTimeSeriesKind](BaseTimeSeriesKind.md)  |  | [BaseTimeSeries](BaseTimeSeries.md) |
| generatedAtTime | [nc:BaseTimeSeries.generatedAtTime](http://entsoe.eu/ns/nc#BaseTimeSeries.generatedAtTime) | 0..1 <br />  [DateTime](DateTime.md)  |  | [BaseTimeSeries](BaseTimeSeries.md) |
| percentile | [nc:BaseTimeSeries.percentile](http://entsoe.eu/ns/nc#BaseTimeSeries.percentile) | 0..1 <br />  integer  |  | [BaseTimeSeries](BaseTimeSeries.md) |
| actionMethod | [nc:BaseTimeSeries.actionMethod](http://entsoe.eu/ns/nc#BaseTimeSeries.actionMethod) | 0..1 <br />  string  |  | [BaseTimeSeries](BaseTimeSeries.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CapacityTimePoint](CapacityTimePoint.md) | CapacitySchedule | range | [CapacitySchedule](CapacitySchedule.md) |
| [Container](Container.md) | CapacitySchedule | range | [CapacitySchedule](CapacitySchedule.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc:CapacitySchedule |
| native | this:CapacitySchedule |




