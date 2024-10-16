# EquivalentEquipment


_The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:EquivalentEquipment](http://iec.ch/TC57/CIM100#EquivalentEquipment)<br />
**Type**: Class




```mermaid
 classDiagram
    class EquivalentEquipment
    click EquivalentEquipment href "../EquivalentEquipment"
      ConductingEquipment <|-- EquivalentEquipment
        click ConductingEquipment href "../ConductingEquipment"
      

      EquivalentEquipment <|-- EquivalentInjection
        click EquivalentInjection href "../EquivalentInjection"
      
      
      EquivalentEquipment : Equipment.inService
        
      EquivalentEquipment : IdentifiedObject.mRID
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * **EquivalentEquipment**
                    * [EquivalentInjection](EquivalentInjection.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | 1 <br />  boolean  | Specifies the availability of the equipment | [Equipment](Equipment.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis/2.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:EquivalentEquipment |
| native | this:EquivalentEquipment |




