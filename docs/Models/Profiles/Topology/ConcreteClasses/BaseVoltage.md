# BaseVoltage

_Defines a system base voltage which is referenced._

**URI**: [cim:BaseVoltage](http://iec.ch/TC57/CIM100#BaseVoltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class BaseVoltage
    click BaseVoltage href "/Models/Profiles/Topology/ConcreteClasses/BaseVoltage/"
    style BaseVoltage fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        BaseVoltage --> TopologicalNode : BaseVoltage.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> BaseVoltage : TopologicalNode.BaseVoltage

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        BaseVoltage : BaseVoltage.TopologicalNode
```

## Inheritance
* **BaseVoltage**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| TopologicalNode | [cim:BaseVoltage.TopologicalNode](http://iec.ch/TC57/CIM100#BaseVoltage.TopologicalNode) | No cardinality available TopologicalNode | The topological nodes at the base voltage. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
