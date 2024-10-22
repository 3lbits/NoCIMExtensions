# Slot: ACLineSegment


_The associated AC Line Segment_



URI: [nc-no:ACLineSegmentSpan.ACLineSegment](http://cim4.eu/ns/nc-no#ACLineSegmentSpan.ACLineSegment)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ACLineSegmentSpan](ACLineSegmentSpan.md) | The part of a segment line between two consecutive points of support |  no  |







## Properties

* Range: [ACLineSegment](ACLineSegment.md)

* Multivalued: True

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ACLineSegmentSpan](ACLineSegmentSpan.md) | [ACLineSegment](ACLineSegment.md) | range | [ACLineSegment](ACLineSegment.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: ACLineSegment
description: The associated AC Line Segment
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:ACLineSegmentSpan.ACLineSegment
alias: ACLineSegment
owner: ACLineSegmentSpan
domain_of:
- ACLineSegmentSpan
range: ACLineSegment
multivalued: true
minimum_cardinality: 0

```
</details>