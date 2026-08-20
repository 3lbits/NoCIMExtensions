# Location

_The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more position points (coordinates) in a given coordinate system._

**URI**: [cim:Location](http://iec.ch/TC57/CIM100#Location)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class Location
    click Location href "/Models/Profiles/GeographicalLocation/ConcreteClasses/Location/"
    style Location fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Location <|-- WorkLocation : inherits

        WorkLocation
            click WorkLocation href "/Models/Profiles/GeographicalLocation/ConcreteClasses/WorkLocation/"
            style WorkLocation fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Location : inherits
            click IdentifiedObject href "/Models/Profiles/GeographicalLocation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Location --> CoordinateSystem : Location.CoordinateSystem

        CoordinateSystem
            click CoordinateSystem href "/Models/Profiles/GeographicalLocation/ConcreteClasses/CoordinateSystem/"
            style CoordinateSystem fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Location --> StreetAddress : Location.mainAddress

        StreetAddress
            click StreetAddress href "/Models/Profiles/GeographicalLocation/ConcreteClasses/StreetAddress/"
            style StreetAddress fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Location --> PowerSystemResource : Location.PowerSystemResources

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/GeographicalLocation/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Location --> PositionPoint : Location.PositionPoints

        PositionPoint
            click PositionPoint href "/Models/Profiles/GeographicalLocation/ConcreteClasses/PositionPoint/"
            style PositionPoint fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        CoordinateSystem --> Location : CoordinateSystem.Locations

        CoordinateSystem
            click CoordinateSystem href "/Models/Profiles/GeographicalLocation/ConcreteClasses/CoordinateSystem/"
            style CoordinateSystem fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        PositionPoint --> Location : PositionPoint.Location

        PositionPoint
            click PositionPoint href "/Models/Profiles/GeographicalLocation/ConcreteClasses/PositionPoint/"
            style PositionPoint fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> Location : PowerSystemResource.Location

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/GeographicalLocation/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        Location : Location.CoordinateSystem
        Location : Location.mainAddress
        Location : Location.PowerSystemResources
        Location : Location.PositionPoints
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/GeographicalLocation/AbstractClasses/IdentifiedObject/)
    * **Location**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| CoordinateSystem | [cim:Location.CoordinateSystem](http://iec.ch/TC57/CIM100#Location.CoordinateSystem) | No cardinality available CoordinateSystem | Coordinate system used to describe position points of this location. | direct |
| mainAddress | [cim:Location.mainAddress](http://iec.ch/TC57/CIM100#Location.mainAddress) | No cardinality available StreetAddress | Main address of the location. | direct |
| PowerSystemResources | [cim:Location.PowerSystemResources](http://iec.ch/TC57/CIM100#Location.PowerSystemResources) | No cardinality available PowerSystemResource | All power system resources at this location. | direct |
| PositionPoints | [cim:Location.PositionPoints](http://iec.ch/TC57/CIM100#Location.PositionPoints) | No cardinality available PositionPoint | Sequence of position points describing this location, expressed in coordinate system 'Location.CoordinateSystem'. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile](http://iec.ch/TC57/ns/CIM/GeographicalLocation-EUPackage_GeographicalLocationProfile)
