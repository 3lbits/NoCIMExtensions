# SvVoltage

_State variable for voltage._

**URI**: [cim:SvVoltage](http://iec.ch/TC57/CIM100#SvVoltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SvVoltage
    click SvVoltage href "/Models/Profiles/StateVariables/ConcreteClasses/SvVoltage/"
    style SvVoltage fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvVoltage --> AngleDegrees : SvVoltage.angle

        AngleDegrees
            click AngleDegrees href "/Models/Profiles/StateVariables/ConcreteClasses/AngleDegrees/"
            style AngleDegrees fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        SvVoltage --> Voltage : SvVoltage.v

        Voltage
            click Voltage href "/Models/Profiles/StateVariables/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        SvVoltage --> TopologicalNode : SvVoltage.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> SvVoltage : TopologicalNode.SvVoltage

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SvVoltage : SvVoltage.angle
        SvVoltage : SvVoltage.v
        SvVoltage : SvVoltage.TopologicalNode
```

## Inheritance
* **SvVoltage**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| angle | [cim:SvVoltage.angle](http://iec.ch/TC57/CIM100#SvVoltage.angle) | No cardinality available AngleDegrees | The voltage angle of the topological node complex voltage with respect to system reference. | direct |
| v | [cim:SvVoltage.v](http://iec.ch/TC57/CIM100#SvVoltage.v) | No cardinality available Voltage | The voltage magnitude at the topological node. The attribute shall be a positive value. | direct |
| TopologicalNode | [cim:SvVoltage.TopologicalNode](http://iec.ch/TC57/CIM100#SvVoltage.TopologicalNode) | No cardinality available TopologicalNode | The topological node associated with the voltage state. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
