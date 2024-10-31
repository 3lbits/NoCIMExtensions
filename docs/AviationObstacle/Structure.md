# Structure


_Construction holding assets such as conductors, transformers, switchgear, etc._




* __NOTE__: this is an abstract class and should not be instantiated directly


**URI**: [nc-no:Structure](http://cim4.eu/ns/nc-no#Structure)<br />
**Type**: Class




```mermaid
 classDiagram
    class Structure
    click Structure href "../Structure"
      LocationResource <|-- Structure
        click LocationResource href "../LocationResource"
      

      Structure <|-- OverheadStructure
        click OverheadStructure href "../OverheadStructure"
      
      
      Structure : IdentifiedObject.description
        
      Structure : hasGeometry
        
          Structure --> Geometry : hasGeometry
          click Geometry href "../Geometry"
        
      Structure : Structure.height
        
      Structure : PowerSystemResource.locationMethod
        
          Structure --> LocationMethodKind : PowerSystemResource.locationMethod
          click LocationMethodKind href "../LocationMethodKind"
        
      Structure : IdentifiedObject.mRID
        
      Structure : IdentifiedObject.name
        
      
```





## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * [ElementResource](ElementResource.md)
        * [LocationResource](LocationResource.md) [ [Feature](Feature.md)]
            * **Structure**
                * [OverheadStructure](OverheadStructure.md)



## Attributes


| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| height | [nc-no:Structure.height](http://cim4.eu/ns/nc-no#Structure.height) | 0..1 <br />  [Length](Length.md)  | Visible height of structure above ground level for overhead construction (e | direct |
| locationMethod | [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod) | 0..1 <br />  [LocationMethodKind](LocationMethodKind.md)  | Method used to derive geographical location for this entity | [LocationResource](LocationResource.md) |
| hasGeometry | [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry) | 0..1 <br />  [Geometry](Geometry.md)  | Geometric representation of the spatial object | [Feature](Feature.md) |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 <br />  string  | Master resource identifier issued by a model authority | [IdentifiedObject](IdentifiedObject.md) |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 <br />  string  | The description is a free human readable text describing or naming the object | [IdentifiedObject](IdentifiedObject.md) |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 <br />  string  | The name is any free human readable and possibly non unique text naming the o... | [IdentifiedObject](IdentifiedObject.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StructureDeployment](StructureDeployment.md) | ACLineSegmentSpan | range | [Structure](Structure.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nc-no:Structure |
| native | this:Structure |




