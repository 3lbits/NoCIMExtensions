# Zone


_Defines a system base voltage which is referenced._





**URI**: [nc-no:Zone](https://ap-no.cim4.eu/AviationObstacle/1.0#Zone)<br />
**Type**: Class




```mermaid
 classDiagram
    class Zone
    click Zone href "../Zone"
      LocationResource <|-- Zone
        click LocationResource href "../LocationResource"
      
      Zone : IdentifiedObject.description
        
      Zone : hasGeometry
        
          Zone --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      Zone : PowerSystemResource.locationMethod
        
          Zone --> LocationMethodKind : PowerSystemResource.locationMethod
          click LocationMethodKind href "../LocationMethodKind"
        
      Zone : IdentifiedObject.mRID
        
      Zone : IdentifiedObject.name
        
      Zone : Zone.state
        
          Zone --> ZoneStateKind : Zone.state
          click ZoneStateKind href "../ZoneStateKind"
        
      Zone : Zone.zoneKind
        
          Zone --> ZoneKind : Zone.zoneKind
          click ZoneKind href "../ZoneKind"
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ElementResource](ElementResource.md)
        * [LocationResource](LocationResource.md) [ [Feature](Feature.md)]
            * **Zone**



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| state | [cim:Zone.state](http://iec.ch/TC57/CIM100#Zone.state) | 0..1 <br />  [ZoneStateKind](ZoneStateKind.md)  | Current state of zone | direct |
| zoneKind | [cim:Zone.zoneKind](http://iec.ch/TC57/CIM100#Zone.zoneKind) | 0..1 <br />  [ZoneKind](ZoneKind.md)  | Kind of zone | direct |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](https://ap-no.cim4.eu/AviationObstacle/1.0#PowerSystemResource.locationMethod) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Method used to derive geographical location for this entity | [LocationResource](LocationResource.md) |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:Zone |
| native | this:Zone |




