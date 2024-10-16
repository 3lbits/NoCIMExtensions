# AnalogLimitSet


_An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement._





**URI**: [cim:AnalogLimitSet](http://iec.ch/TC57/CIM100#AnalogLimitSet)<br />
**Type**: Class




```mermaid
 classDiagram
    class AnalogLimitSet
    click AnalogLimitSet href "../AnalogLimitSet"
      LimitSet <|-- AnalogLimitSet
        click LimitSet href "../LimitSet"
      
      AnalogLimitSet : IdentifiedObject.description
        
      AnalogLimitSet : LimitSet.isPercentageLimits
        
      AnalogLimitSet : AnalogLimitSet.Measurements
        
          AnalogLimitSet --> Analog : AnalogLimitSet.Measurements
          click Analog href "../Analog"
        
      AnalogLimitSet : IdentifiedObject.mRID
        
      AnalogLimitSet : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [LimitSet](LimitSet.md)
        * **AnalogLimitSet**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Measurements | [cim:AnalogLimitSet.Measurements](http://iec.ch/TC57/CIM100#AnalogLimitSet.Measurements) | 1..* <br />  [Analog](Analog.md)  | The Measurements using the LimitSet | direct |
| isPercentageLimits | [cim:LimitSet.isPercentageLimits](http://iec.ch/TC57/CIM100#LimitSet.isPercentageLimits) | 0..1 <br />  boolean  | Tells if the limit values are in percentage of normalValue or the specified U... | [LimitSet](LimitSet.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AnalogLimit](AnalogLimit.md) | LimitSet | range | [AnalogLimitSet](AnalogLimitSet.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2020/CPSM-Operation#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:AnalogLimitSet |
| native | this:AnalogLimitSet |




