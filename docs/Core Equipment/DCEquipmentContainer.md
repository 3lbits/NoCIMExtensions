# DCEquipmentContainer


_A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC equipment._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:DCEquipmentContainer](http://iec.ch/TC57/CIM100#DCEquipmentContainer)<br />
**Type**: Class




```mermaid
 classDiagram
    class DCEquipmentContainer
    click DCEquipmentContainer href "../DCEquipmentContainer"
      EquipmentContainer <|-- DCEquipmentContainer
        click EquipmentContainer href "../EquipmentContainer"
      

      DCEquipmentContainer <|-- DCConverterUnit
        click DCConverterUnit href "../DCConverterUnit"
      DCEquipmentContainer <|-- DCLine
        click DCLine href "../DCLine"
      
      
      DCEquipmentContainer : IdentifiedObject.description
        
      DCEquipmentContainer : IdentifiedObject.mRID
        
      DCEquipmentContainer : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [ConnectivityNodeContainer](ConnectivityNodeContainer.md)
            * [EquipmentContainer](EquipmentContainer.md)
                * **DCEquipmentContainer**
                    * [DCConverterUnit](DCConverterUnit.md)
                    * [DCLine](DCLine.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DCNode](DCNode.md) | DCEquipmentContainer | range | [DCEquipmentContainer](DCEquipmentContainer.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2020/CPSM-CoreEquipment#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:DCEquipmentContainer |
| native | this:DCEquipmentContainer |




