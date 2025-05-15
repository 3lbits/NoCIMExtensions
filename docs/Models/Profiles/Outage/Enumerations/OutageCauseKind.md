# OutageCauseKind

_This enumeration describes the primary cause of the outage - planned, unplanned, etc._

**URI**: http://iec.ch/TC57/CIM100#OutageCauseKind

**Type**: Enumeration

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| animal | [cim:OutageCauseKind.animal](http://iec.ch/TC57/CIM100#OutageCauseKind.animal) | This outage was caused by an animal is was unplanned.  As such it is treated as a forced outage and is probably classified as trouble with a Trouble Ticket as well as a work/service order.  The primary difference between this and an unplanned outage is the reason for the outage.  If an animal caused this and perished as a result, the utility may have other actions that are required to be taken by the EPA or other groups with whom the utility has an agreement. |
| lightingStrike | [cim:OutageCauseKind.lightingStrike](http://iec.ch/TC57/CIM100#OutageCauseKind.lightingStrike) | Outage is caused by a lighting strike |
| lineDown | [cim:OutageCauseKind.lineDown](http://iec.ch/TC57/CIM100#OutageCauseKind.lineDown) | The outage is caused by a line down |
| poleDown | [cim:OutageCauseKind.poleDown](http://iec.ch/TC57/CIM100#OutageCauseKind.poleDown) | The outage is caused by a pole down |
| treeDown | [cim:OutageCauseKind.treeDown](http://iec.ch/TC57/CIM100#OutageCauseKind.treeDown) | The outage is caused by a tree down |
## Schema Source

from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
