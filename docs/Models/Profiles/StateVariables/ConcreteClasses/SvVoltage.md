# SvVoltage

_State variable for voltage._

**URI**: [cim:SvVoltage](http://iec.ch/TC57/CIM100#SvVoltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class SvVoltage
    click SvVoltage href "/Models/Profiles/StateVariables/ConcreteClasses/SvVoltage/"
    style SvVoltage fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        SvVoltage --> TopologicalNode : SvVoltage.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> SvVoltage : TopologicalNode.SvVoltage

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


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
