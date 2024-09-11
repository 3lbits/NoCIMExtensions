# StructureDeployment


_Deployment of a structure._





**URI**: [nc-no:StructureDeployment](https://ap-no.cim4.eu/AviationObstacle/1.0#StructureDeployment)<br />
**Type**: Class




```mermaid
 classDiagram
    class StructureDeployment
    click StructureDeployment href "../StructureDeployment"
      AssetDeployment <|-- StructureDeployment
        click AssetDeployment href "../AssetDeployment"
      
      StructureDeployment : StructureDeployment.Structure
        
          StructureDeployment --> Structure : StructureDeployment.Structure
          click Structure href "../Structure"
        
      StructureDeployment : AssetDeployment.BaseVoltage
        
          StructureDeployment --> BaseVoltage : AssetDeployment.BaseVoltage
          click BaseVoltage href "../BaseVoltage"
        
      StructureDeployment : AssetDeployment.deploymentState
        
          StructureDeployment --> DeploymentStateKind : AssetDeployment.deploymentState
          click DeploymentStateKind href "../DeploymentStateKind"
        
      StructureDeployment : IdentifiedObject.description
        
      StructureDeployment : AssetDeployment.inServiceDate
        
      StructureDeployment : AssetDeployment.installedDate
        
      StructureDeployment : IdentifiedObject.mRID
        
      StructureDeployment : IdentifiedObject.name
        
      StructureDeployment : AssetDeployment.notYetInstalledDate
        
      StructureDeployment : AssetDeployment.notYetRemovedDate
        
      StructureDeployment : AssetDeployment.outOfServiceDate
        
      StructureDeployment : AssetDeployment.removedDate
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [AssetDeployment](AssetDeployment.md)
        * **StructureDeployment**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ACLineSegmentSpan | [nc-no:StructureDeployment.Structure](https://ap-no.cim4.eu/AviationObstacle/1.0#StructureDeployment.Structure) | 0..1 <br />  [Structure](Structure.md)  | The associated Structure | direct |
| deploymentState | [cim:AssetDeployment.deploymentState](http://iec.ch/TC57/CIM100#AssetDeployment.deploymentState) | 0..1 <br />  [DeploymentStateKind](DeploymentStateKind.md)  | Current deployment state of asset | [AssetDeployment](AssetDeployment.md) |
| BaseVoltage | [cim:AssetDeployment.BaseVoltage](http://iec.ch/TC57/CIM100#AssetDeployment.BaseVoltage) | 0..1 <br />  [BaseVoltage](BaseVoltage.md)  | The associated Base Voltage | [AssetDeployment](AssetDeployment.md) |
| inServiceDate | [nc-no:AssetDeployment.inServiceDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.inServiceDate) | 0..1 <br />  datetime  | Date and time asset was most recently put in service | [AssetDeployment](AssetDeployment.md) |
| installedDate | [nc-no:AssetDeployment.installedDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.installedDate) | 0..1 <br />  datetime  | Date and time asset was most recently installed | [AssetDeployment](AssetDeployment.md) |
| notYetInstalledDate | [nc-no:AssetDeployment.notYetInstalledDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.notYetInstalledDate) | 0..1 <br />  datetime  | Date and time of asset deployment transition to not yet installed | [AssetDeployment](AssetDeployment.md) |
| notYetRemovedDate | [nc-no:AssetDeployment.notYetRemovedDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.notYetRemovedDate) | 0..1 <br />  datetime  | Date and time of asset deployment transition to not yet removed | [AssetDeployment](AssetDeployment.md) |
| outOfServiceDate | [nc-no:AssetDeployment.outOfServiceDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.outOfServiceDate) | 0..1 <br />  datetime  | Date and time asset was most recently taken out of service | [AssetDeployment](AssetDeployment.md) |
| removedDate | [nc-no:AssetDeployment.removedDate](https://ap-no.cim4.eu/AviationObstacle/1.0#AssetDeployment.removedDate) | 0..1 <br />  datetime  | Date and time asset was most recently removed | [AssetDeployment](AssetDeployment.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:StructureDeployment |
| native | this:StructureDeployment |



