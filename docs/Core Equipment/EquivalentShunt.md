# EquivalentShunt


_The class represents equivalent shunts._





**URI**: [cim:EquivalentShunt](http://iec.ch/TC57/CIM100#EquivalentShunt)<br />
**Type**: Class




```mermaid
 classDiagram
    class EquivalentShunt
    click EquivalentShunt href "../EquivalentShunt"
      EquivalentEquipment <|-- EquivalentShunt
        click EquivalentEquipment href "../EquivalentEquipment"
      
      EquivalentShunt : Equipment.aggregate
        
      EquivalentShunt : EquivalentShunt.b
        
      EquivalentShunt : ConductingEquipment.BaseVoltage
        
          EquivalentShunt --> BaseVoltage : ConductingEquipment.BaseVoltage
          click BaseVoltage href "../BaseVoltage"
        
      EquivalentShunt : IdentifiedObject.description
        
      EquivalentShunt : Equipment.EquipmentContainer
        
          EquivalentShunt --> EquipmentContainer : Equipment.EquipmentContainer
          click EquipmentContainer href "../EquipmentContainer"
        
      EquivalentShunt : EquivalentEquipment.EquivalentNetwork
        
          EquivalentShunt --> EquivalentNetwork : EquivalentEquipment.EquivalentNetwork
          click EquivalentNetwork href "../EquivalentNetwork"
        
      EquivalentShunt : EquivalentShunt.g
        
      EquivalentShunt : IdentifiedObject.mRID
        
      EquivalentShunt : IdentifiedObject.name
        
      EquivalentShunt : Equipment.normallyInService
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * [EquivalentEquipment](EquivalentEquipment.md)
                    * **EquivalentShunt**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| b | [cim:EquivalentShunt.b](http://iec.ch/TC57/CIM100#EquivalentShunt.b) | 1 <br />  [Susceptance](Susceptance.md)  | Positive sequence shunt susceptance | direct |
| g | [cim:EquivalentShunt.g](http://iec.ch/TC57/CIM100#EquivalentShunt.g) | 1 <br />  [Conductance](Conductance.md)  | Positive sequence shunt conductance | direct |
| EquivalentNetwork | [cim:EquivalentEquipment.EquivalentNetwork](http://iec.ch/TC57/CIM100#EquivalentEquipment.EquivalentNetwork) | 0..1 <br />  [EquivalentNetwork](EquivalentNetwork.md)  | The equivalent where the reduced model belongs | [EquivalentEquipment](EquivalentEquipment.md) |
| BaseVoltage | [cim:ConductingEquipment.BaseVoltage](http://iec.ch/TC57/CIM100#ConductingEquipment.BaseVoltage) | 0..1 <br />  [BaseVoltage](BaseVoltage.md)  | Base voltage of this conducting equipment | [ConductingEquipment](ConductingEquipment.md) |
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
| self | cim:EquivalentShunt |
| native | this:EquivalentShunt |




