# ConnectivityNode

_Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance._

**URI**: [cim:ConnectivityNode](http://iec.ch/TC57/CIM100#ConnectivityNode)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ConnectivityNode
    click ConnectivityNode href "/Models/Profiles/Topology/ConcreteClasses/ConnectivityNode/"
    style ConnectivityNode fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> TopologicalNode : ConnectivityNode.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> ConnectivityNode : TopologicalNode.ConnectivityNodes

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        ConnectivityNode : ConnectivityNode.TopologicalNode
```

## Inheritance
* **ConnectivityNode**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| TopologicalNode | [cim:ConnectivityNode.TopologicalNode](http://iec.ch/TC57/CIM100#ConnectivityNode.TopologicalNode) | No cardinality available TopologicalNode | The topological node to which this connectivity node is assigned.  May depend on the current state of switches in the network. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
