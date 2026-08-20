# Terminal

_An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes._

**URI**: [cim:Terminal](http://iec.ch/TC57/CIM100#Terminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class Terminal
    click Terminal href "/Models/Profiles/StateVariables/ConcreteClasses/Terminal/"
    style Terminal fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCTerminal <|-- Terminal : inherits
            click ACDCTerminal href "/Models/Profiles/StateVariables/AbstractClasses/ACDCTerminal/"
            style ACDCTerminal fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/StateVariables/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> SvPowerFlow : Terminal.SvPowerFlow

        SvPowerFlow
            click SvPowerFlow href "/Models/Profiles/StateVariables/ConcreteClasses/SvPowerFlow/"
            style SvPowerFlow fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        SvPowerFlow --> Terminal : SvPowerFlow.Terminal

        SvPowerFlow
            click SvPowerFlow href "/Models/Profiles/StateVariables/ConcreteClasses/SvPowerFlow/"
            style SvPowerFlow fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        Terminal : Terminal.SvPowerFlow
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/StateVariables/AbstractClasses/IdentifiedObject/)
    * [ACDCTerminal](/Models/Profiles/StateVariables/AbstractClasses/ACDCTerminal/)
        * **Terminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SvPowerFlow | [cim:Terminal.SvPowerFlow](http://iec.ch/TC57/CIM100#Terminal.SvPowerFlow) | No cardinality available SvPowerFlow | The power flow state variable associated with the terminal. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
