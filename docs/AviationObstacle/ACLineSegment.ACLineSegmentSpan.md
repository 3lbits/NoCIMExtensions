# Slot: ACLineSegmentSpan

URI: [this:ACLineSegmentSpan](https://ap-no.cim4.eu/AviationObstacle/1.0#ACLineSegmentSpan)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan |  no  |
[ACLineSegment](ACLineSegment.md) | A wire or combination of wires, with consistent electrical characteristics, b... |  no  |
[Container](Container.md) |  |  no  |
[StructureDeployment](StructureDeployment.md) | Deployment of a structure |  no  |







## Properties

* Range: [String](String.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ACLineSegment](ACLineSegment.md) | [ACLineSegmentSpan](ACLineSegmentSpan.md) | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |
| [ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | [ACLineSegmentSpan](ACLineSegmentSpan.md) | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |
| [Container](Container.md) | [ACLineSegmentSpan](ACLineSegmentSpan.md) | range | [ACLineSegmentSpan](ACLineSegmentSpan.md) |






## Identifier and Mapping Information








## LinkML Source

<details>
```yaml
name: ACLineSegmentSpan
alias: ACLineSegmentSpan
domain_of:
- ACLineSegment
- ACLineSegmentSpanDeployment
- StructureDeployment
- Container
range: string

```
</details>