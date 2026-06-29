# DiagramStyle

_The diagram style refers to a style used by the originating system for a diagram.  A diagram style describes information such as schematic, geographic, etc._

**URI**: [cim:DiagramStyle](http://iec.ch/TC57/CIM100#DiagramStyle)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DiagramStyle
    click DiagramStyle href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramStyle/"
    style DiagramStyle fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- DiagramStyle : inherits
            click IdentifiedObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DiagramStyle --> Diagram : DiagramStyle.Diagram

        Diagram
            click Diagram href "/Models/Profiles/DiagramLayout/ConcreteClasses/Diagram/"
            style Diagram fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        IdentifiedObject --> DiagramObject : IdentifiedObject.DiagramObjects

        DiagramObject
            click DiagramObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObject/"
            style DiagramObject fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Diagram --> DiagramStyle : Diagram.DiagramStyle

        Diagram
            click Diagram href "/Models/Profiles/DiagramLayout/ConcreteClasses/Diagram/"
            style Diagram fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DiagramObject --> IdentifiedObject : DiagramObject.IdentifiedObject

        DiagramObject
            click DiagramObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObject/"
            style DiagramObject fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DiagramStyle : DiagramStyle.Diagram
        IdentifiedObject : IdentifiedObject.DiagramObjects
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.description
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/DiagramLayout/ConcreteClasses/IdentifiedObject/)
    * **DiagramStyle**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Diagram | [cim:DiagramStyle.Diagram](http://iec.ch/TC57/CIM100#DiagramStyle.Diagram) | No cardinality available Diagram | A DiagramStyle can be used by many Diagrams. | direct |
| DiagramObjects | [cim:IdentifiedObject.DiagramObjects](http://iec.ch/TC57/CIM100#IdentifiedObject.DiagramObjects) | No cardinality available DiagramObject | The diagram objects that are associated with the domain object. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/DiagramLayout-EUPackage_DiagramLayoutProfile](http://iec.ch/TC57/ns/CIM/DiagramLayout-EUPackage_DiagramLayoutProfile)
