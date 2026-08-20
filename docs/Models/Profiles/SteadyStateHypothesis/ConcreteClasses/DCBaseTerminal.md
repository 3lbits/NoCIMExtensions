# DCBaseTerminal

_An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model requires that DC connections are distinct from AC connections._

**URI**: [cim:DCBaseTerminal](http://iec.ch/TC57/CIM100#DCBaseTerminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DCBaseTerminal
    click DCBaseTerminal href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/DCBaseTerminal/"
    style DCBaseTerminal fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal <|-- ACDCConverterDCTerminal : inherits

        ACDCConverterDCTerminal
            click ACDCConverterDCTerminal href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ACDCConverterDCTerminal/"
            style ACDCConverterDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal <|-- DCTerminal : inherits

        DCTerminal
            click DCTerminal href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/DCTerminal/"
            style DCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCTerminal <|-- DCBaseTerminal : inherits
            click ACDCTerminal href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        ACDCTerminal : ACDCTerminal.connected
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [ACDCTerminal](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ACDCTerminal/)
        * **DCBaseTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| connected | [cim:ACDCTerminal.connected](http://iec.ch/TC57/CIM100#ACDCTerminal.connected) | No cardinality available boolean | The connected status is related to a bus-branch model and the topological node to terminal relation.  True implies the terminal is connected to the related topological node and false implies it is not. 
In a bus-branch model, the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the topological node to terminal relation. A valid case is that conducting equipment can be connected in one end and open in the other. In particular for an AC line segment, where the reactive line charging can be significant, this is a relevant case. | ACDCTerminal |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
