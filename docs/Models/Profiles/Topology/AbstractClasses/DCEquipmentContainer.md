# DCEquipmentContainer

_A modelling construct to provide a root class for containment of DC as well as AC equipment. The class differ from the EquipmentContaner for AC in that it may also contain DCNode-s. Hence it can contain both AC and DC equipment._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:DCEquipmentContainer](http://iec.ch/TC57/CIM100#DCEquipmentContainer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DCEquipmentContainer
    click DCEquipmentContainer href "/Models/Profiles/Topology/AbstractClasses/DCEquipmentContainer/"
    style DCEquipmentContainer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCEquipmentContainer --> DCTopologicalNode : DCEquipmentContainer.DCTopologicalNode

        DCTopologicalNode
            click DCTopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/DCTopologicalNode/"
            style DCTopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCTopologicalNode --> DCEquipmentContainer : DCTopologicalNode.DCEquipmentContainer

        DCTopologicalNode
            click DCTopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/DCTopologicalNode/"
            style DCTopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCEquipmentContainer : DCEquipmentContainer.DCTopologicalNode
```

## Inheritance
* **DCEquipmentContainer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCTopologicalNode | [cim:DCEquipmentContainer.DCTopologicalNode](http://iec.ch/TC57/CIM100#DCEquipmentContainer.DCTopologicalNode) | No cardinality available DCTopologicalNode | The topological nodes which belong to this connectivity node container. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
