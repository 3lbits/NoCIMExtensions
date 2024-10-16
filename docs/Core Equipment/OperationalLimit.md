# OperationalLimit


_A value and normal value associated with a specific kind of limit.The sub class value and normalValue attributes vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short).If a particular piece of equipment has multiple operational limits of the same kind (apparent power, current, etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with the smallest acceptableDuration shall have the largest limit value.  Note: A large current can only be allowed to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be allowed to flow for a longer duration._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:OperationalLimit](http://iec.ch/TC57/CIM100#OperationalLimit)<br />
**Type**: Class




```mermaid
 classDiagram
    class OperationalLimit
    click OperationalLimit href "../OperationalLimit"
      IdentifiedObject <|-- OperationalLimit
        click IdentifiedObject href "../IdentifiedObject"
      

      OperationalLimit <|-- ActivePowerLimit
        click ActivePowerLimit href "../ActivePowerLimit"
      OperationalLimit <|-- ApparentPowerLimit
        click ApparentPowerLimit href "../ApparentPowerLimit"
      OperationalLimit <|-- CurrentLimit
        click CurrentLimit href "../CurrentLimit"
      OperationalLimit <|-- VoltageLimit
        click VoltageLimit href "../VoltageLimit"
      
      
      OperationalLimit : IdentifiedObject.description
        
      OperationalLimit : IdentifiedObject.mRID
        
      OperationalLimit : IdentifiedObject.name
        
      OperationalLimit : OperationalLimit.OperationalLimitSet
        
          OperationalLimit --> OperationalLimitSet : OperationalLimit.OperationalLimitSet
          click OperationalLimitSet href "../OperationalLimitSet"
        
      OperationalLimit : OperationalLimit.OperationalLimitType
        
          OperationalLimit --> OperationalLimitType : OperationalLimit.OperationalLimitType
          click OperationalLimitType href "../OperationalLimitType"
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **OperationalLimit**
        * [ActivePowerLimit](ActivePowerLimit.md)
        * [ApparentPowerLimit](ApparentPowerLimit.md)
        * [CurrentLimit](CurrentLimit.md)
        * [VoltageLimit](VoltageLimit.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| OperationalLimitSet | [cim:OperationalLimit.OperationalLimitSet](http://iec.ch/TC57/CIM100#OperationalLimit.OperationalLimitSet) | 1 <br />  [OperationalLimitSet](OperationalLimitSet.md)  | The limit set to which the limit values belong | direct |
| OperationalLimitType | [cim:OperationalLimit.OperationalLimitType](http://iec.ch/TC57/CIM100#OperationalLimit.OperationalLimitType) | 1 <br />  [OperationalLimitType](OperationalLimitType.md)  | The limit type associated with this limit | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2020/CPSM-CoreEquipment#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:OperationalLimit |
| native | this:OperationalLimit |




