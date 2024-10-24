# RegulatingCondEq


_A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network._





**URI**: [cim:RegulatingCondEq](http://iec.ch/TC57/CIM100#RegulatingCondEq)<br />
**Type**: Class




```mermaid
 classDiagram
    class RegulatingCondEq
    click RegulatingCondEq href "../RegulatingCondEq"
      EnergyConnection <|-- RegulatingCondEq
        click EnergyConnection href "../EnergyConnection"
      

      RegulatingCondEq <|-- ExternalNetworkInjection
        click ExternalNetworkInjection href "../ExternalNetworkInjection"
      RegulatingCondEq <|-- PowerElectronicsConnection
        click PowerElectronicsConnection href "../PowerElectronicsConnection"
      RegulatingCondEq <|-- RotatingMachine
        click RotatingMachine href "../RotatingMachine"
      RegulatingCondEq <|-- ShuntCompensator
        click ShuntCompensator href "../ShuntCompensator"
      RegulatingCondEq <|-- StaticVarCompensator
        click StaticVarCompensator href "../StaticVarCompensator"
      
      
      RegulatingCondEq : RegulatingCondEq.controlEnabled
        
      RegulatingCondEq : Equipment.inService
        
      RegulatingCondEq : IdentifiedObject.mRID
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * [EnergyConnection](EnergyConnection.md)
                    * **RegulatingCondEq**
                        * [ExternalNetworkInjection](ExternalNetworkInjection.md)
                        * [PowerElectronicsConnection](PowerElectronicsConnection.md)
                        * [RotatingMachine](RotatingMachine.md)
                        * [ShuntCompensator](ShuntCompensator.md)
                        * [StaticVarCompensator](StaticVarCompensator.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| controlEnabled | [cim:RegulatingCondEq.controlEnabled](http://iec.ch/TC57/CIM100#RegulatingCondEq.controlEnabled) | 1 <br />  boolean  | Specifies the regulation status of the equipment | direct |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | 1 <br />  boolean  | Specifies the availability of the equipment | [Equipment](Equipment.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis/2.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:RegulatingCondEq |
| native | this:RegulatingCondEq |




