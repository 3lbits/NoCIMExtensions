# DisconnectingCircuitBreaker


_A circuit breaking device including disconnecting function, eliminating the need for separate disconnectors._





**URI**: [cim:DisconnectingCircuitBreaker](http://iec.ch/TC57/CIM100#DisconnectingCircuitBreaker)<br />
**Type**: Class




```mermaid
 classDiagram
    class DisconnectingCircuitBreaker
    click DisconnectingCircuitBreaker href "../DisconnectingCircuitBreaker"
      Breaker <|-- DisconnectingCircuitBreaker
        click Breaker href "../Breaker"
      
      DisconnectingCircuitBreaker : Equipment.inService
        
      DisconnectingCircuitBreaker : Switch.locked
        
      DisconnectingCircuitBreaker : IdentifiedObject.mRID
        
      DisconnectingCircuitBreaker : Switch.open
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [PowerSystemResource](PowerSystemResource.md)
        * [Equipment](Equipment.md)
            * [ConductingEquipment](ConductingEquipment.md)
                * [Switch](Switch.md)
                    * [ProtectedSwitch](ProtectedSwitch.md)
                        * [Breaker](Breaker.md)
                            * **DisconnectingCircuitBreaker**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| locked | [cim:Switch.locked](http://iec.ch/TC57/CIM100#Switch.locked) | 1 <br />  boolean  | If true, the switch is locked | [Switch](Switch.md) |
| open | [cim:Switch.open](http://iec.ch/TC57/CIM100#Switch.open) | 1 <br />  boolean  | The attribute tells if the switch is considered open when used as input to to... | [Switch](Switch.md) |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | 1 <br />  boolean  | Specifies the availability of the equipment | [Equipment](Equipment.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis/2.0#





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cim:DisconnectingCircuitBreaker |
| native | this:DisconnectingCircuitBreaker |




