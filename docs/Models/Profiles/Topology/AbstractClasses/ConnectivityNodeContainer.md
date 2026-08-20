# ConnectivityNodeContainer

_A base class for all objects that may contain connectivity nodes or topological nodes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConnectivityNodeContainer](http://iec.ch/TC57/CIM100#ConnectivityNodeContainer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ConnectivityNodeContainer
    click ConnectivityNodeContainer href "/Models/Profiles/Topology/AbstractClasses/ConnectivityNodeContainer/"
    style ConnectivityNodeContainer fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNodeContainer --> TopologicalNode : ConnectivityNodeContainer.TopologicalNode

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TopologicalNode --> ConnectivityNodeContainer : TopologicalNode.ConnectivityNodeContainer

        TopologicalNode
            click TopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/TopologicalNode/"
            style TopologicalNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


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
