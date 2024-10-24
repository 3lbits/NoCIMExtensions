# TapChanger


_Mechanism for changing transformer winding tap positions._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [cim:TapChanger](http://iec.ch/TC57/CIM100#TapChanger)<br />
**Type**: Class




```mermaid
 classDiagram
    class TapChanger
    click TapChanger href "../TapChanger"
      PowerSystemResource <|-- TapChanger
        click PowerSystemResource href "../PowerSystemResource"
      

      TapChanger <|-- PhaseTapChanger
        click PhaseTapChanger href "../PhaseTapChanger"
      TapChanger <|-- RatioTapChanger
        click RatioTapChanger href "../RatioTapChanger"
      
      
      TapChanger : TapChanger.controlEnabled
        
      TapChanger : IdentifiedObject.mRID
        
      TapChanger : TapChanger.step
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * **TapChanger**
            * [PhaseTapChanger](PhaseTapChanger.md)
            * [RatioTapChanger](RatioTapChanger.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| controlEnabled | [cim:TapChanger.controlEnabled](http://iec.ch/TC57/CIM100#TapChanger.controlEnabled) | 1 <br />  boolean  | Specifies the regulation status of the equipment | direct |
| step | [cim:TapChanger.step](http://iec.ch/TC57/CIM100#TapChanger.step) | 1 <br />  float  | Tap changer position | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis/2.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:TapChanger |
| native | this:TapChanger |




