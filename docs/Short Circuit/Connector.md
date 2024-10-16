# Connector


_A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:Connector](http://iec.ch/TC57/CIM100#Connector)<br />
**Type**: Class




```mermaid
 classDiagram
    class Connector
    click Connector href "../Connector"
      ConductingEquipment <|-- Connector
        click ConductingEquipment href "../ConductingEquipment"
      

      Connector <|-- BusbarSection
        click BusbarSection href "../BusbarSection"
      
      
      Connector : IdentifiedObject.mRID
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * **Connector**
                    * [BusbarSection](BusbarSection.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2020/CPSM-ShortCircuit#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:Connector |
| native | this:Connector |




