# Slot: deploymentState


_Current deployment state of asset._



URI: [cim:AssetDeployment.deploymentState](https://cim.ucaiug.io/ns#AssetDeployment.deploymentState)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AssetDeployment](AssetDeployment.md) | Deployment of asset deployment in a power system resource role |  no  |
[ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan |  no  |
[StructureDeployment](StructureDeployment.md) | Deployment of a structure |  no  |







## Properties

* Range: [DeploymentStateKind](DeploymentStateKind.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: deploymentState
description: Current deployment state of asset.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: cim:AssetDeployment.deploymentState
alias: deploymentState
owner: AssetDeployment
domain_of:
- AssetDeployment
range: DeploymentStateKind
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>