# EnergyArea

_Describes an area having energy production or consumption.  Specializations are intended to support the load allocation function as typically required in energy management systems or planning studies to allocate hypothesized load levels to individual load points for power flow analysis.  Often the energy area can be linked to both measured and forecast load levels._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:EnergyArea](https://cim.ucaiug.io/ns#EnergyArea)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class EnergyArea
    click EnergyArea href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/EnergyArea/"
    style EnergyArea fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergyArea <|-- LoadArea : inherits

        LoadArea
            click LoadArea href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/LoadArea/"
            style LoadArea fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- EnergyArea : inherits
            click IdentifiedObject href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ControlArea --> EnergyArea : ControlArea.EnergyArea

        ControlArea
            click ControlArea href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/ControlArea/"
            style ControlArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/)
    * **EnergyArea**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
