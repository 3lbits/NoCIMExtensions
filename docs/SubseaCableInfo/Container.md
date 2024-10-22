# Container



**URI**: [this:Container](http://iec.ch/TC57/2007/profile#Container)<br />
**Type**: Class




```mermaid
 classDiagram
    class Container
    click Container href "../Container"
      Container : CableInfo
        
          Container --> CableInfo : CableInfo
          click CableInfo href "../CableInfo"
        
      Container : InsulationLayer
        
          Container --> InsulationLayer : InsulationLayer
          click InsulationLayer href "../InsulationLayer"
        
      Container : MetallicSheathLayer
        
          Container --> MetallicSheathLayer : MetallicSheathLayer
          click MetallicSheathLayer href "../MetallicSheathLayer"
        
      Container : MultiCoreCableInfo
        
          Container --> MultiCoreCableInfo : MultiCoreCableInfo
          click MultiCoreCableInfo href "../MultiCoreCableInfo"
        
      Container : NonMetallicSheathLayer
        
          Container --> NonMetallicSheathLayer : NonMetallicSheathLayer
          click NonMetallicSheathLayer href "../NonMetallicSheathLayer"
        
      Container : ProductAssetModel
        
          Container --> ProductAssetModel : ProductAssetModel
          click ProductAssetModel href "../ProductAssetModel"
        
      Container : ScreenLayer
        
          Container --> ScreenLayer : ScreenLayer
          click ScreenLayer href "../ScreenLayer"
        
      
```




<!-- no inheritance hierarchy -->


## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| CableInfo | [this:CableInfo](http://iec.ch/TC57/2007/profile#CableInfo) | 0..* <br />  [CableInfo](CableInfo.md)  |  | direct |
| MultiCoreCableInfo | [this:MultiCoreCableInfo](http://iec.ch/TC57/2007/profile#MultiCoreCableInfo) | 0..* <br />  [MultiCoreCableInfo](MultiCoreCableInfo.md)  |  | direct |
| ProductAssetModel | [this:ProductAssetModel](http://iec.ch/TC57/2007/profile#ProductAssetModel) | 0..* <br />  [ProductAssetModel](ProductAssetModel.md)  |  | direct |
| InsulationLayer | [this:InsulationLayer](http://iec.ch/TC57/2007/profile#InsulationLayer) | 0..* <br />  [InsulationLayer](InsulationLayer.md)  |  | direct |
| MetallicSheathLayer | [this:MetallicSheathLayer](http://iec.ch/TC57/2007/profile#MetallicSheathLayer) | 0..* <br />  [MetallicSheathLayer](MetallicSheathLayer.md)  |  | direct |
| ScreenLayer | [this:ScreenLayer](http://iec.ch/TC57/2007/profile#ScreenLayer) | 0..* <br />  [ScreenLayer](ScreenLayer.md)  |  | direct |
| NonMetallicSheathLayer | [this:NonMetallicSheathLayer](http://iec.ch/TC57/2007/profile#NonMetallicSheathLayer) | 0..* <br />  [NonMetallicSheathLayer](NonMetallicSheathLayer.md)  |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | this:Container |
| native | this:Container |




