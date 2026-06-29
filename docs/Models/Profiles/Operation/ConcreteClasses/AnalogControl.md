# AnalogControl

_An analog control used for supervisory control._

**URI**: [cim:AnalogControl](http://iec.ch/TC57/CIM100#AnalogControl)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AnalogControl
    click AnalogControl href "/Models/Profiles/Operation/ConcreteClasses/AnalogControl/"
    style AnalogControl fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AnalogControl <|-- RaiseLowerCommand : inherits

        RaiseLowerCommand
            click RaiseLowerCommand href "/Models/Profiles/Operation/ConcreteClasses/RaiseLowerCommand/"
            style RaiseLowerCommand fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AnalogControl <|-- SetPoint : inherits

        SetPoint
            click SetPoint href "/Models/Profiles/Operation/ConcreteClasses/SetPoint/"
            style SetPoint fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Control <|-- AnalogControl : inherits
            click Control href "/Models/Profiles/Operation/ConcreteClasses/Control/"
            style Control fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IOPoint <|-- Control : inherits
            click IOPoint href "/Models/Profiles/Operation/ConcreteClasses/IOPoint/"
            style IOPoint fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- IOPoint : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AnalogControl --> AnalogValue : AnalogControl.AnalogValue

        AnalogValue
            click AnalogValue href "/Models/Profiles/Operation/ConcreteClasses/AnalogValue/"
            style AnalogValue fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Control --> PowerSystemResource : Control.PowerSystemResource

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Operation/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AnalogValue --> AnalogControl : AnalogValue.AnalogControl

        AnalogValue
            click AnalogValue href "/Models/Profiles/Operation/ConcreteClasses/AnalogValue/"
            style AnalogValue fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> Control : PowerSystemResource.Controls

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Operation/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Control --> UnitMultiplier : Control.unitMultiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/Operation/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Control --> UnitSymbol : Control.unitSymbol

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/Operation/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AnalogControl : AnalogControl.maxValue
        AnalogControl : AnalogControl.minValue
        AnalogControl : AnalogControl.AnalogValue
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
* [IdentifiedObject](/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/)
    * [IOPoint](/Models/Profiles/Operation/ConcreteClasses/IOPoint/)
        * [Control](/Models/Profiles/Operation/ConcreteClasses/Control/)
            * **AnalogControl**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| maxValue | [cim:AnalogControl.maxValue](http://iec.ch/TC57/CIM100#AnalogControl.maxValue) | No cardinality available float | Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. | direct |
| minValue | [cim:AnalogControl.minValue](http://iec.ch/TC57/CIM100#AnalogControl.minValue) | No cardinality available float | Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. | direct |
| AnalogValue | [cim:AnalogControl.AnalogValue](http://iec.ch/TC57/CIM100#AnalogControl.AnalogValue) | No cardinality available AnalogValue | The MeasurementValue that is controlled. | direct |
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
