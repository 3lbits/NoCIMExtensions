# SvTapStep


_State variable for transformer tap step._





**URI**: [cim:SvTapStep](http://iec.ch/TC57/CIM100#SvTapStep)<br />
**Type**: Class




```mermaid
 classDiagram
    class SvTapStep
    click SvTapStep href "../SvTapStep"
      SvTapStep : SvTapStep.position
        
      SvTapStep : SvTapStep.TapChanger
        
          SvTapStep --> TapChanger : SvTapStep.TapChanger
          click TapChanger href "../TapChanger"
        
      
```




<!-- no inheritance hierarchy -->


## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| position | [cim:SvTapStep.position](http://iec.ch/TC57/CIM100#SvTapStep.position) | 1 <br />  float  | The floating point tap position | direct |
| TapChanger | [cim:SvTapStep.TapChanger](http://iec.ch/TC57/CIM100#SvTapStep.TapChanger) | 1 <br />  [TapChanger](TapChanger.md)  | The tap changer associated with the tap step state | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/ns/CIM/StateVariables/5.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:SvTapStep |
| native | this:SvTapStep |




