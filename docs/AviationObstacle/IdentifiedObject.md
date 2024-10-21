# IdentifiedObject


_This is a root class to provide common identification for all classes needing identification and naming attributes._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:IdentifiedObject](https://cim.ucaiug.io/ns#IdentifiedObject)<br />
**Type**: Class




```mermaid
 classDiagram
    class IdentifiedObject
    click IdentifiedObject href "../IdentifiedObject"
      IdentifiedObject <|-- PowerSystemResource
        click PowerSystemResource href "../PowerSystemResource"
      IdentifiedObject <|-- ElementResource
        click ElementResource href "../ElementResource"
      IdentifiedObject <|-- AssetDeployment
        click AssetDeployment href "../AssetDeployment"
      IdentifiedObject <|-- BaseVoltage
        click BaseVoltage href "../BaseVoltage"
      
      IdentifiedObject : IdentifiedObject.description
        
      IdentifiedObject : IdentifiedObject.mRID
        
      IdentifiedObject : IdentifiedObject.name
        
      
```





## Inheritance
* **IdentifiedObject**
    * [PowerSystemResource](PowerSystemResource.md) [ [Feature](Feature.md)]
    * [ElementResource](ElementResource.md)
    * [AssetDeployment](AssetDeployment.md)
    * [BaseVoltage](BaseVoltage.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | direct |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | direct |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | direct |









## Comments

* The attribute IdentifiedObject.mRID is exchanged as rdf:ID.

## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:IdentifiedObject |
| native | this:IdentifiedObject |




