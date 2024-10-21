# Container



**URI**: [this:Container](https://ap-no.cim4.eu/WattApp/1.0#Container)<br />
**Type**: Class




```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : CapacitySchedule
        
          Container --> CapacitySchedule : CapacitySchedule
          click CapacitySchedule href "../CapacitySchedule"
        
      Container : CapacityTimePoint
        
          Container --> CapacityTimePoint : CapacityTimePoint
          click CapacityTimePoint href "../CapacityTimePoint"
        
      Container : Feeder
        
          Container --> Feeder : Feeder
          click Feeder href "../Feeder"
        
      
```




<!-- no inheritance hierarchy -->


## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Feeder | [this:Feeder](https://ap-no.cim4.eu/WattApp/1.0#Feeder) | 0..* <br />  [Feeder](Feeder.md)  |  | direct |
| CapacitySchedule | [this:CapacitySchedule](https://ap-no.cim4.eu/WattApp/1.0#CapacitySchedule) | 0..* <br />  [CapacitySchedule](CapacitySchedule.md)  |  | direct |
| CapacityTimePoint | [this:CapacityTimePoint](https://ap-no.cim4.eu/WattApp/1.0#CapacityTimePoint) | 0..* <br />  [CapacityTimePoint](CapacityTimePoint.md)  |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | this:Container |
| native | this:Container |




