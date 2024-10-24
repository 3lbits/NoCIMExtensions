# ExternalNetworkInjection


_This class represents the external network and it is used for IEC 60909 calculations._





**URI**: [cim:ExternalNetworkInjection](http://iec.ch/TC57/CIM100#ExternalNetworkInjection)<br />
**Type**: Class




```mermaid
 classDiagram
    class ExternalNetworkInjection
    click ExternalNetworkInjection href "../ExternalNetworkInjection"
      RegulatingCondEq <|-- ExternalNetworkInjection
        click RegulatingCondEq href "../RegulatingCondEq"
      
      ExternalNetworkInjection : Equipment.aggregate
        
      ExternalNetworkInjection : ConductingEquipment.BaseVoltage
        
          ExternalNetworkInjection --> BaseVoltage : ConductingEquipment.BaseVoltage
          click BaseVoltage href "../BaseVoltage"
        
      ExternalNetworkInjection : IdentifiedObject.description
        
      ExternalNetworkInjection : Equipment.EquipmentContainer
        
          ExternalNetworkInjection --> EquipmentContainer : Equipment.EquipmentContainer
          click EquipmentContainer href "../EquipmentContainer"
        
      ExternalNetworkInjection : ExternalNetworkInjection.governorSCD
        
      ExternalNetworkInjection : ExternalNetworkInjection.maxP
        
      ExternalNetworkInjection : ExternalNetworkInjection.maxQ
        
      ExternalNetworkInjection : ExternalNetworkInjection.minP
        
      ExternalNetworkInjection : ExternalNetworkInjection.minQ
        
      ExternalNetworkInjection : IdentifiedObject.mRID
        
      ExternalNetworkInjection : IdentifiedObject.name
        
      ExternalNetworkInjection : Equipment.normallyInService
        
      ExternalNetworkInjection : RegulatingCondEq.RegulatingControl
        
          ExternalNetworkInjection --> RegulatingControl : RegulatingCondEq.RegulatingControl
          click RegulatingControl href "../RegulatingControl"
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * [EnergyConnection](EnergyConnection.md)
                    * [RegulatingCondEq](RegulatingCondEq.md)
                        * **ExternalNetworkInjection**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| governorSCD | [cim:ExternalNetworkInjection.governorSCD](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.governorSCD) | 1 <br />  [ActivePowerPerFrequency](ActivePowerPerFrequency.md)  | Power Frequency Bias | direct |
| maxP | [cim:ExternalNetworkInjection.maxP](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxP) | 1 <br />  [ActivePower](ActivePower.md)  | Maximum active power of the injection | direct |
| maxQ | [cim:ExternalNetworkInjection.maxQ](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.maxQ) | 1 <br />  [ReactivePower](ReactivePower.md)  | Maximum reactive power limit | direct |
| minP | [cim:ExternalNetworkInjection.minP](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minP) | 1 <br />  [ActivePower](ActivePower.md)  | Minimum active power of the injection | direct |
| minQ | [cim:ExternalNetworkInjection.minQ](http://iec.ch/TC57/CIM100#ExternalNetworkInjection.minQ) | 1 <br />  [ReactivePower](ReactivePower.md)  | Minimum reactive power limit | direct |
| RegulatingControl | [cim:RegulatingCondEq.RegulatingControl](http://iec.ch/TC57/CIM100#RegulatingCondEq.RegulatingControl) | 0..1 <br />  [RegulatingControl](RegulatingControl.md)  | The regulating control scheme in which this equipment participates | [RegulatingCondEq](RegulatingCondEq.md) |
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
| self | cim:ExternalNetworkInjection |
| native | this:ExternalNetworkInjection |




