# WireInfo


_Wire data that can be specified per line segment phase, or for the line segment as a whole in case its phases all have the same wire characteristics._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:WireInfo](http://iec.ch/TC57/CIM-generic#WireInfo)<br />
**Type**: Class




```mermaid
 classDiagram
    class WireInfo
    click WireInfo href "../WireInfo"
      ConductorInfo <|-- WireInfo
        click ConductorInfo href "../ConductorInfo"
      

      WireInfo <|-- CableInfo
        click CableInfo href "../CableInfo"
      
      
      WireInfo : ConductorInfo.ConductorPerLengthResistance
        
          WireInfo --> ResistancePerLengthTemperaturePoint : ConductorInfo.ConductorPerLengthResistance
          click ResistancePerLengthTemperaturePoint href "../ResistancePerLengthTemperaturePoint"
        
      WireInfo : WireInfo.coreRadius
        
      WireInfo : ConductorInfo.crossSection
        
      WireInfo : IdentifiedObject.description
        
      WireInfo : IdentifiedObject.mRID
        
      WireInfo : IdentifiedObject.name
        
      WireInfo : WireInfo.radius
        
      WireInfo : ConductingAssetInfo.ratedCurrent
        
      WireInfo : ConductingAssetInfo.ratedFrequency
        
      WireInfo : ConductingAssetInfo.ratedVoltage
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [AssetInfo](AssetInfo.md)
        * [ConductingAssetInfo](ConductingAssetInfo.md)
            * [ConductorInfo](ConductorInfo.md)
                * **WireInfo**
                    * [CableInfo](CableInfo.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| coreRadius | [cim:WireInfo.coreRadius](http://iec.ch/TC57/CIM-generic#WireInfo.coreRadius) | 0..1 <br />  [Length](Length.md)  | (if there is a different core material) Radius of the central core | direct |
| radius | [cim:WireInfo.radius](http://iec.ch/TC57/CIM-generic#WireInfo.radius) | 0..1 <br />  [Length](Length.md)  | Outside radius of the wire | direct |
| crossSection | [cim:ConductorInfo.crossSection](http://iec.ch/TC57/CIM-generic#ConductorInfo.crossSection) | 0..1 <br />  [Area](Area.md)  | Area of conducting material cross section | [ConductorInfo](ConductorInfo.md) |
| ConductorPerLengthResistance | [cim:ConductorInfo.ConductorPerLengthResistance](http://iec.ch/TC57/CIM-generic#ConductorInfo.ConductorPerLengthResistance) | 0..* <br />  [ResistancePerLengthTemperaturePoint](ResistancePerLengthTemperaturePoint.md)  | Resistance per unit length of this conductor at a given temperature | [ConductorInfo](ConductorInfo.md) |
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
| self | cim:WireInfo |
| native | this:WireInfo |




