# ACLineSegmentSpanDeployment


_Deployment of an ACLineSegmentSpan._





**URI**: [nc-no:ACLineSegmentSpanDeployment](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpanDeployment)<br />
**Type**: Class




```mermaid
 classDiagram
    class ACLineSegmentSpanDeployment
    click ACLineSegmentSpanDeployment href "../ACLineSegmentSpanDeployment"
      AssetDeployment <|-- ACLineSegmentSpanDeployment
        click AssetDeployment href "../AssetDeployment"
      
      ACLineSegmentSpanDeployment : ACLineSegmentSpanDeployment.ACLineSegmentSpan
        
          ACLineSegmentSpanDeployment --> ACLineSegmentSpan : ACLineSegmentSpanDeployment.ACLineSegmentSpan
          click ACLineSegmentSpan href "../ACLineSegmentSpan"
        
      ACLineSegmentSpanDeployment : AssetDeployment.BaseVoltage
        
          ACLineSegmentSpanDeployment --> BaseVoltage : AssetDeployment.BaseVoltage
          click BaseVoltage href "../BaseVoltage"
        
      ACLineSegmentSpanDeployment : AssetDeployment.deploymentState
        
          ACLineSegmentSpanDeployment --> DeploymentStateKind : AssetDeployment.deploymentState
          click DeploymentStateKind href "../DeploymentStateKind"
        
      ACLineSegmentSpanDeployment : IdentifiedObject.description
        
      ACLineSegmentSpanDeployment : AssetDeployment.inServiceDate
        
      ACLineSegmentSpanDeployment : AssetDeployment.installedDate
        
      ACLineSegmentSpanDeployment : IdentifiedObject.mRID
        
      ACLineSegmentSpanDeployment : IdentifiedObject.name
        
      ACLineSegmentSpanDeployment : AssetDeployment.notYetInstalledDate
        
      ACLineSegmentSpanDeployment : AssetDeployment.notYetRemovedDate
        
      ACLineSegmentSpanDeployment : AssetDeployment.outOfServiceDate
        
      ACLineSegmentSpanDeployment : AssetDeployment.removedDate
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [AssetDeployment](AssetDeployment.md)
        * **ACLineSegmentSpanDeployment**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ACLineSegmentSpan | [nc-no:ACLineSegmentSpanDeployment.ACLineSegmentSpan](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpanDeployment.ACLineSegmentSpan) | 0..1 <br />  [ACLineSegmentSpan](ACLineSegmentSpan.md)  | The associated AC Line Segment Span | direct |
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


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:ACLineSegmentSpanDeployment |
| native | this:ACLineSegmentSpanDeployment |




