# ConnectivityNodeContainer

_A base class for all objects that may contain connectivity nodes or topological nodes._

**URI**: [cim:ConnectivityNodeContainer](http://iec.ch/TC57/CIM100#ConnectivityNodeContainer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ConnectivityNodeContainer
    click ConnectivityNodeContainer href "/Models/Profiles/Topology/ConcreteClasses/ConnectivityNodeContainer/"
    style ConnectivityNodeContainer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNodeContainer --> TopologicalNode : ConnectivityNodeContainer.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> ConnectivityNodeContainer : TopologicalNode.ConnectivityNodeContainer

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ConnectivityNodeContainer : ConnectivityNodeContainer.TopologicalNode
```

## Inheritance
* **ConnectivityNodeContainer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| TopologicalNode | [cim:ConnectivityNodeContainer.TopologicalNode](http://iec.ch/TC57/CIM100#ConnectivityNodeContainer.TopologicalNode) | No cardinality available TopologicalNode | The topological nodes which belong to this connectivity node container. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
