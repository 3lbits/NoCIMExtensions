# Command

_A Command is a discrete control used for supervisory control._

**URI**: [cim:Command](http://iec.ch/TC57/CIM100#Command)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class Command
    click Command href "/Models/Profiles/Operation/ConcreteClasses/Command/"
    style Command fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        Control <|-- Command : inherits
            click Control href "/Models/Profiles/Operation/AbstractClasses/Control/"
            style Control fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IOPoint <|-- Control : inherits
            click IOPoint href "/Models/Profiles/Operation/AbstractClasses/IOPoint/"
            style IOPoint fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- IOPoint : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Command --> ValueAliasSet : Command.ValueAliasSet

        ValueAliasSet
            click ValueAliasSet href "/Models/Profiles/Operation/ConcreteClasses/ValueAliasSet/"
            style ValueAliasSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Command --> DiscreteValue : Command.DiscreteValue

        DiscreteValue
            click DiscreteValue href "/Models/Profiles/Operation/ConcreteClasses/DiscreteValue/"
            style DiscreteValue fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Control --> PowerSystemResource : Control.PowerSystemResource

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Operation/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DiscreteValue --> Command : DiscreteValue.Command

        DiscreteValue
            click DiscreteValue href "/Models/Profiles/Operation/ConcreteClasses/DiscreteValue/"
            style DiscreteValue fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> Control : PowerSystemResource.Controls

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Operation/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ValueAliasSet --> Command : ValueAliasSet.Commands

        ValueAliasSet
            click ValueAliasSet href "/Models/Profiles/Operation/ConcreteClasses/ValueAliasSet/"
            style ValueAliasSet fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Control --> UnitMultiplier : Control.unitMultiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/Operation/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#5729FF,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        Control --> UnitSymbol : Control.unitSymbol

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/Operation/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#5729FF,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        Command : Command.normalValue
        Command : Command.value
        Command : Command.ValueAliasSet
        Command : Command.DiscreteValue
        Control : Control.controlType
        Control : Control.operationInProgress
        Control : Control.timeStamp
        Control : Control.unitMultiplier
        Control : Control.unitSymbol
        Control : Control.PowerSystemResource
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/AbstractClasses/IdentifiedObject/)
    * [IOPoint](/Models/Profiles/Operation/AbstractClasses/IOPoint/)
        * [Control](/Models/Profiles/Operation/AbstractClasses/Control/)
            * **Command**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| normalValue | [cim:Command.normalValue](http://iec.ch/TC57/CIM100#Command.normalValue) | No cardinality available integer | Normal value for Control.value e.g. used for percentage scaling. | direct |
| value | [cim:Command.value](http://iec.ch/TC57/CIM100#Command.value) | No cardinality available integer | The value representing the actuator output. | direct |
| ValueAliasSet | [cim:Command.ValueAliasSet](http://iec.ch/TC57/CIM100#Command.ValueAliasSet) | No cardinality available ValueAliasSet | The ValueAliasSet used for translation of a Control value to a name. | direct |
| DiscreteValue | [cim:Command.DiscreteValue](http://iec.ch/TC57/CIM100#Command.DiscreteValue) | No cardinality available DiscreteValue | The MeasurementValue that is controlled. | direct |
| controlType | [cim:Control.controlType](http://iec.ch/TC57/CIM100#Control.controlType) | No cardinality available string | Specifies the type of Control. For example, this specifies if the Control represents BreakerOpen, BreakerClose, GeneratorVoltageSetPoint, GeneratorRaise, GeneratorLower, etc. | Control |
| operationInProgress | [cim:Control.operationInProgress](http://iec.ch/TC57/CIM100#Control.operationInProgress) | No cardinality available boolean | Indicates that a client is currently sending control commands that has not completed. | Control |
| timeStamp | [cim:Control.timeStamp](http://iec.ch/TC57/CIM100#Control.timeStamp) | No cardinality available date | The last time a control output was sent. | Control |
| unitMultiplier | [cim:Control.unitMultiplier](http://iec.ch/TC57/CIM100#Control.unitMultiplier) | No cardinality available UnitMultiplier | The unit multiplier of the controlled quantity. | Control |
| unitSymbol | [cim:Control.unitSymbol](http://iec.ch/TC57/CIM100#Control.unitSymbol) | No cardinality available UnitSymbol | The unit of measure of the controlled quantity. | Control |
| PowerSystemResource | [cim:Control.PowerSystemResource](http://iec.ch/TC57/CIM100#Control.PowerSystemResource) | No cardinality available PowerSystemResource | Regulating device governed by this control output. | Control |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
