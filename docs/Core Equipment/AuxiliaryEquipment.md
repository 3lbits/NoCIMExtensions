# AuxiliaryEquipment


_AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function.AuxiliaryEquipment is attached to primary equipment via an association with Terminal._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:AuxiliaryEquipment](http://iec.ch/TC57/CIM100#AuxiliaryEquipment)<br />
**Type**: Class




```mermaid
 classDiagram
    class AuxiliaryEquipment
    click AuxiliaryEquipment href "../AuxiliaryEquipment"
      Equipment <|-- AuxiliaryEquipment
        click Equipment href "../Equipment"
      

      AuxiliaryEquipment <|-- FaultIndicator
        click FaultIndicator href "../FaultIndicator"
      AuxiliaryEquipment <|-- Sensor
        click Sensor href "../Sensor"
      AuxiliaryEquipment <|-- SurgeArrester
        click SurgeArrester href "../SurgeArrester"
      AuxiliaryEquipment <|-- WaveTrap
        click WaveTrap href "../WaveTrap"
      
      
      AuxiliaryEquipment : Equipment.aggregate
        
      AuxiliaryEquipment : IdentifiedObject.description
        
      AuxiliaryEquipment : Equipment.EquipmentContainer
        
          AuxiliaryEquipment --> EquipmentContainer : Equipment.EquipmentContainer
          click EquipmentContainer href "../EquipmentContainer"
        
      AuxiliaryEquipment : IdentifiedObject.mRID
        
      AuxiliaryEquipment : IdentifiedObject.name
        
      AuxiliaryEquipment : Equipment.normallyInService
        
      AuxiliaryEquipment : AuxiliaryEquipment.Terminal
        
          AuxiliaryEquipment --> Terminal : AuxiliaryEquipment.Terminal
          click Terminal href "../Terminal"
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * **AuxiliaryEquipment**
                * [FaultIndicator](FaultIndicator.md)
                * [Sensor](Sensor.md)
                * [SurgeArrester](SurgeArrester.md)
                * [WaveTrap](WaveTrap.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Terminal | [cim:AuxiliaryEquipment.Terminal](http://iec.ch/TC57/CIM100#AuxiliaryEquipment.Terminal) | 1 <br />  [Terminal](Terminal.md)  | The Terminal at the equipment where the AuxiliaryEquipment is attached | direct |
| aggregate | [cim:Equipment.aggregate](http://iec.ch/TC57/CIM100#Equipment.aggregate) | 0..1 <br />  boolean  | The aggregate flag provides an alternative way of representing an aggregated ... | [Equipment](Equipment.md) |
| normallyInService | [cim:Equipment.normallyInService](http://iec.ch/TC57/CIM100#Equipment.normallyInService) | 0..1 <br />  boolean  | Specifies the availability of the equipment under normal operating conditions | [Equipment](Equipment.md) |
| EquipmentContainer | [cim:Equipment.EquipmentContainer](http://iec.ch/TC57/CIM100#Equipment.EquipmentContainer) | 0..1 <br />  [EquipmentContainer](EquipmentContainer.md)  | Container of this equipment | [Equipment](Equipment.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2020/CPSM-CoreEquipment#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:AuxiliaryEquipment |
| native | this:AuxiliaryEquipment |




