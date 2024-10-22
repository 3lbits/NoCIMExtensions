# ConductorInfo


_Common class for rigid and flexible conductors.[IEC 826-14-06]: Conductive part intended to carry a specified electric current_




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:ConductorInfo](http://iec.ch/TC57/CIM-generic#ConductorInfo)<br />
**Type**: Class




```mermaid
 classDiagram
    class ConductorInfo
    click ConductorInfo href "../ConductorInfo"
      ConductingAssetInfo <|-- ConductorInfo
        click ConductingAssetInfo href "../ConductingAssetInfo"
      

      ConductorInfo <|-- WireInfo
        click WireInfo href "../WireInfo"
      
      
      ConductorInfo : ConductorInfo.ConductorPerLengthResistance
        
          ConductorInfo --> ResistancePerLengthTemperaturePoint : ConductorInfo.ConductorPerLengthResistance
          click ResistancePerLengthTemperaturePoint href "../ResistancePerLengthTemperaturePoint"
        
      ConductorInfo : ConductorInfo.crossSection
        
      ConductorInfo : IdentifiedObject.description
        
      ConductorInfo : IdentifiedObject.mRID
        
      ConductorInfo : IdentifiedObject.name
        
      ConductorInfo : ConductingAssetInfo.ratedCurrent
        
      ConductorInfo : ConductingAssetInfo.ratedFrequency
        
      ConductorInfo : ConductingAssetInfo.ratedVoltage
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [AssetInfo](AssetInfo.md)
        * [ConductingAssetInfo](ConductingAssetInfo.md)
            * **ConductorInfo**
                * [WireInfo](WireInfo.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| crossSection | [cim:ConductorInfo.crossSection](http://iec.ch/TC57/CIM-generic#ConductorInfo.crossSection) | 0..1 <br />  [Area](Area.md)  | Area of conducting material cross section | direct |
| ConductorPerLengthResistance | [cim:ConductorInfo.ConductorPerLengthResistance](http://iec.ch/TC57/CIM-generic#ConductorInfo.ConductorPerLengthResistance) | 0..* <br />  [ResistancePerLengthTemperaturePoint](ResistancePerLengthTemperaturePoint.md)  | Resistance per unit length of this conductor at a given temperature | direct |
| ratedCurrent | [cim:ConductingAssetInfo.ratedCurrent](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedCurrent) | 0..1 <br />  [CurrentFlow](CurrentFlow.md)  | Rated current | [ConductingAssetInfo](ConductingAssetInfo.md) |
| ratedFrequency | [cim:ConductingAssetInfo.ratedFrequency](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedFrequency) | 0..1 <br />  [Frequency](Frequency.md)  | Rated frequency such as 50Hz or 60Hz | [ConductingAssetInfo](ConductingAssetInfo.md) |
| ratedVoltage | [cim:ConductingAssetInfo.ratedVoltage](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedVoltage) | 0..1 <br />  [Voltage](Voltage.md)  | Rated voltage | [ConductingAssetInfo](ConductingAssetInfo.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM-generic#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:ConductorInfo |
| native | this:ConductorInfo |




