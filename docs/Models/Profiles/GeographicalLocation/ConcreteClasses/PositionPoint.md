# PositionPoint

_Set of spatial coordinates that determine a point, defined in the coordinate system specified in 'Location.CoordinateSystem'. Use a single position point instance to describe a point-oriented location. Use a sequence of position points to describe a line-oriented object (physical location of non-point oriented objects like cables or lines), or area of an object (like a substation or a geographical zone - in this case, have first and last position point with the same values)._

**URI**: [cim:PositionPoint](http://iec.ch/TC57/CIM100#PositionPoint)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PositionPoint
    click PositionPoint href "/Models/Profiles/GeographicalLocation/ConcreteClasses/PositionPoint/"
    style PositionPoint fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PositionPoint --> Location : PositionPoint.Location

        Location
            click Location href "/Models/Profiles/GeographicalLocation/ConcreteClasses/Location/"
            style Location fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Location --> PositionPoint : Location.PositionPoints

        Location
            click Location href "/Models/Profiles/GeographicalLocation/ConcreteClasses/Location/"
            style Location fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PositionPoint : PositionPoint.Location
        PositionPoint : PositionPoint.sequenceNumber
        PositionPoint : PositionPoint.xPosition
        PositionPoint : PositionPoint.yPosition
        PositionPoint : PositionPoint.zPosition
```

## Inheritance
* **PositionPoint**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Location | [cim:PositionPoint.Location](http://iec.ch/TC57/CIM100#PositionPoint.Location) | No cardinality available Location | Location described by this position point. | direct |
| sequenceNumber | [cim:PositionPoint.sequenceNumber](http://iec.ch/TC57/CIM100#PositionPoint.sequenceNumber) | No cardinality available integer | Zero-relative sequence number of this point within a series of points. | direct |
| xPosition | [cim:PositionPoint.xPosition](http://iec.ch/TC57/CIM100#PositionPoint.xPosition) | No cardinality available string | X axis position. | direct |
| yPosition | [cim:PositionPoint.yPosition](http://iec.ch/TC57/CIM100#PositionPoint.yPosition) | No cardinality available string | Y axis position. | direct |
| zPosition | [cim:PositionPoint.zPosition](http://iec.ch/TC57/CIM100#PositionPoint.zPosition) | No cardinality available string | (if applicable) Z axis position. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile](http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile)
