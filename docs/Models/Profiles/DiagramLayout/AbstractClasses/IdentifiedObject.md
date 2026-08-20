# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM100#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/DiagramLayout/AbstractClasses/IdentifiedObject/"
    style IdentifiedObject fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- Diagram : inherits

        Diagram
            click Diagram href "/Models/Profiles/DiagramLayout/ConcreteClasses/Diagram/"
            style Diagram fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DiagramObject : inherits

        DiagramObject
            click DiagramObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObject/"
            style DiagramObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DiagramObjectStyle : inherits

        DiagramObjectStyle
            click DiagramObjectStyle href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObjectStyle/"
            style DiagramObjectStyle fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DiagramStyle : inherits

        DiagramStyle
            click DiagramStyle href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramStyle/"
            style DiagramStyle fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- VisibilityLayer : inherits

        VisibilityLayer
            click VisibilityLayer href "/Models/Profiles/DiagramLayout/ConcreteClasses/VisibilityLayer/"
            style VisibilityLayer fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject --> DiagramObject : IdentifiedObject.DiagramObjects

        DiagramObject
            click DiagramObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObject/"
            style DiagramObject fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DiagramObject --> IdentifiedObject : DiagramObject.IdentifiedObject

        DiagramObject
            click DiagramObject href "/Models/Profiles/DiagramLayout/ConcreteClasses/DiagramObject/"
            style DiagramObject fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        IdentifiedObject : IdentifiedObject.DiagramObjects
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.description
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DiagramObjects | [cim:IdentifiedObject.DiagramObjects](http://iec.ch/TC57/CIM100#IdentifiedObject.DiagramObjects) | No cardinality available DiagramObject | The diagram objects that are associated with the domain object. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/DiagramLayout-EUPackage_DiagramLayoutProfile](http://iec.ch/TC57/ns/CIM/DiagramLayout-EUPackage_DiagramLayoutProfile)
