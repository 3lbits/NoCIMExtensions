# ACDCTerminal

_An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ACDCTerminal](http://iec.ch/TC57/CIM100#ACDCTerminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ACDCTerminal
    click ACDCTerminal href "/Models/Profiles/Operation/AbstractClasses/ACDCTerminal/"
    style ACDCTerminal fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCTerminal <|-- Terminal : inherits

        Terminal
            click Terminal href "/Models/Profiles/Operation/ConcreteClasses/Terminal/"
            style Terminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCTerminal --> Measurement : ACDCTerminal.Measurements

        Measurement
            click Measurement href "/Models/Profiles/Operation/AbstractClasses/Measurement/"
            style Measurement fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Measurement --> ACDCTerminal : Measurement.Terminal

        Measurement
            click Measurement href "/Models/Profiles/Operation/AbstractClasses/Measurement/"
            style Measurement fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCTerminal : ACDCTerminal.Measurements
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * **ACDCTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Measurements | [cim:ACDCTerminal.Measurements](http://iec.ch/TC57/CIM100#ACDCTerminal.Measurements) | No cardinality available Measurement | Measurements associated with this terminal defining  where the measurement is placed in the network topology.  It may be used, for instance, to capture the sensor position, such as a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
