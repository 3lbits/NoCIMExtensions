---
title: "CIM Feeder Model"
type: class-model
author: "Thomas Ranvik Eriksen"
created: 2026-06-04
modified: 2026-06-04
modified-by: "Thomas Ranvik Eriksen"
status: draft
tags: [cim, feeder, topology, connectivity, switch-configuration, grouping]
cim-version: "IEC 61970-301"
norwegian-profile: "CIM4No"
sources:
  - https://github.com/3lbits/cim4no
  - https://github.com/3lbits/NoCIMExtensions
  - https://github.com/3lbits/CIM4NoUtility
---

# CIM Feeder Model

## Overview

The Feeder model provides a **topology-based grouping** of equipment in the power system. Unlike the static container hierarchy (Substation → VoltageLevel → Bay → Line), which represents the physical structure and does not change with switching operations, the Feeder groups equipment based on **connectivity together with switch configuration** — i.e., which components are electrically fed by the same source.

A Feeder represents a radial circuit: all equipment that is energized from a single source point (typically a Bay or PowerTransformer) under a given switching state. This makes Feeder inherently dynamic — the same physical grid can have different Feeder groupings depending on whether switches are in normal, open, or simulated configurations.

### Key Distinction: Containers vs. Feeders

| Aspect | Container (Substation, VoltageLevel, Bay, Line) | Feeder |
|--------|--------------------------------------------------|--------|
| Basis | Physical/structural ownership | Electrical connectivity + switch state |
| Stability | Static — does not change with switching | Dynamic — changes with switch configuration |
| Purpose | Physical grouping | Electrical grouping |
| Overlap | Equipment belongs to exactly one container | Equipment can belong to multiple Feeders |

## Classes

![Feeder UML](feeder_uml.png)

### Feeder

**Description:** A topology-based grouping of equipment that is electrically connected and fed from a common source point under a specific switch configuration. Represents a radial circuit where all members are energized from the same Bay or PowerTransformer.

**Attributes:**

| name | mult | type | description |
|------|------|------|-------------|
| kind | 0..1 | FeederKind | Classification of the feeder type |
| otherKind | 0..1 | String | Free-text description when kind = "other" |
| phaseInfo | 0..1 | PhaseCode | Phase information for the feeder |
| aggregate | 0..1 | Boolean | inherited from: Equipment |
| normallyInService | 0..1 | Boolean | inherited from: Equipment |
| description | 0..1 | String | inherited from: IdentifiedObject |
| mRID | 1..1 | String | inherited from: IdentifiedObject |
| name | 1..1 | String | inherited from: IdentifiedObject |

**Relationships:**

| mult from | name | mult to | type | description |
|-----------|------|---------|------|-------------|
| 0..* | FeederConnection | 1 | FeederConnection | Connections linking equipment to this feeder |
| 1 | NormalHeadTerminal | 1..* | Terminal | The terminal(s) at the head of this feeder in normal configuration |
| 0..* | NormalHeadFeeder | 0..1 | Feeder | Parent feeder in normal switching state |
| 0..1 | HasPart | 0..* | Feeder | Child feeders nested within this feeder |
| 0..* | PartOf | 0..1 | Feeder | Parent feeder containing this feeder |

---

### FeederConnection

**Description:** An association class that links Equipment to Feeders. This enables many-to-many relationships — the same equipment can participate in multiple feeders (representing different switch configurations), and a feeder can contain multiple pieces of equipment.

**Relationships:**

| mult from | name | mult to | type | description |
|-----------|------|---------|------|-------------|
| 0..* | Equipment | 0..* | Equipment | Equipment included in this connection |
| 0..* | Feeder | 0..* | Feeder | Feeders this connection belongs to |

---

### FeederKind (Enumeration)

**Description:** Classifies the type of feeder.

| Value | Description |
|-------|-------------|
| feederArea | A primary feeder area — typically the full radial circuit from a bay |
| secondaryArea | A secondary/sub-area within a larger feeder |
| switchArea | A grouping defined by switch boundaries |
| other | Other classification (use `otherKind` for description) |

## Feeder Nesting (Hierarchical Grouping)

Feeders can be nested hierarchically using the **PartOf / HasPart** self-association:

- A top-level Feeder might represent the entire circuit fed from a PowerTransformer
- Child Feeders can split this by individual Bays in a substation
- Further subdivision can separate Medium Voltage from Low Voltage sections

**Example hierarchy:**

```
Feeder: "Transformer T1 Circuit" (kind: feederArea)
├── Feeder: "Bay B1 MV Feeder" (kind: switchArea)
│   ├── Feeder: "LV Feeder from SecSub 101" (kind: secondaryArea)
│   └── Feeder: "LV Feeder from SecSub 102" (kind: secondaryArea)
└── Feeder: "Bay B2 MV Feeder" (kind: switchArea)
    └── Feeder: "LV Feeder from SecSub 103" (kind: secondaryArea)
```

## Equipment Membership in Multiple Feeders

Unlike containers where equipment belongs to exactly one parent, the FeederConnection association allows equipment to belong to **multiple Feeders simultaneously**. This is essential because:

1. **Normal vs. operational configurations:** A switching configuration can vary depending on the operational situation and we want to be able to switch between these configurations when needed
2. **Simulation scenarios:** When exploring "what if" configurations, equipment may be grouped differently
3. **Open switches included:** A feeder representing a circuit must include the open switches at its boundaries to fully describe the topology

## Use Cases

### 1. Generate Reduced Equipment Files

Create CIM/XML export files containing only the equipment in a specific feeder, rather than exporting the entire grid model. This is useful for:

- Sharing a subset of the grid with external systems or partners
- Reducing file sizes for targeted analysis tools
- **Note:** These files must include open switches at the feeder boundary to correctly represent the circuit extent

### 2. Outage Impact Analysis

Determine which equipment and customers lose power if a specific Transformer or Bay fails:

- Query the Feeder fed by that source to get all affected equipment
- Identify alternative sources by finding open switches at feeder boundaries that could be closed to restore supply from an adjacent feeder
- Quickly visualize the affected area on a map

### 3. Sharing Simulation Configurations

After running a simulation with a specific switch configuration, persist the resulting equipment grouping as a Feeder:

- A colleague can load the same Feeder definition to reproduce or review the simulation
- The Feeder captures exactly which components were included, avoiding the need to recalculate connectivity

### 4. Pre-computed Topology for Performance

Store the grouping for different grid configurations instead of recalculating connectivity every time:

- Only recompute when a topology change occurs (switch operation, new equipment commissioning)
- Dramatically reduces computation for downstream applications that need to know "what feeds what"

### 5. Simple Aggregation and Equivalent Injection Scope

Use Feeder to define the scope of an aggregation:

- While `EquivalentInjection` is the preferred class for storing aggregated calculation results, the Feeder can define *which* equipment is aggregated
- Provides an easy approach to show what has been collapsed into an EquivalentInjection
- Useful for load flow summaries at feeder level

> **Open question:** There is currently no direct relationship between EquivalentInjection and Feeder in the CIM model. Possible workarounds include naming conventions or placing the EquivalentInjection at the same ConnectivityNode as the Feeder head terminal. Whether a formal association should be introduced (or the EquivalentInjection included in the Feeder via FeederConnection) is unresolved. In this use case NormalHeadTerminal can be very useful to determine the link between EquivalentInjection and Feeder

### 6. Protection Zone Mapping

Map protection relay zones to feeders:

- A protection device at a bay protects the equipment in its downstream feeder
- Feeder membership makes it straightforward to determine which equipment is within a protection zone
- Supports coordination studies by clearly defining zone boundaries

> **TODO:** Emilie needs to talk to her "Vern" specialist friend to validate this use case.

### 7. Filtered Class Queries from Feeder Membership

Since the Feeder already contains the full set of connected equipment, you can filter by CIM class to answer targeted questions without recalculating topology:

- "Give me all ConformLoads that will lose power if this transformer fails" — simply filter the Feeder's equipment by class type
- Works for any class: find all ACLineSegments or Switches in a Feeder
- Avoids expensive graph traversal when you only need a subset of the equipment
- Lowers the competence barrier — graph traversal with connectivity and switch state logic is complex and requires extensive training, while filtering a pre-computed Feeder is a simple query anyone can perform

## Norwegian Extensions

In the Norwegian CIM profile (CIM4No / NoCIMExtensions):

- Feeder is used to model the radial distribution network structure common in Norwegian grids
- The `NormalHeadTerminal` relationship connects the feeder to the source terminal (typically at the bay breaker in a substation)
- Norwegian DSOs use Feeder to represent "avganger" (outgoing feeders) from substations and secondary substations
- The nesting capability supports the Norwegian practice of modelling separate MV and LV feeder areas

## Relationship to Static Containers

Feeder complements but does not replace the static container hierarchy:

| Concept | Role |
|---------|------|
| **Substation / VoltageLevel / Bay** | Physical structure — where equipment is installed |
| **Line / FeederLine** | Physical cable/line ownership — which line segment belongs where |
| **Feeder** | Electrical grouping — what is connected under a switch state |

Equipment always has exactly one static container (e.g., a switch is in a Bay), but may be referenced by zero or more Feeders depending on the modelled configurations.

## Model Justification

### Why FeederConnection exists

The FeederConnection class was introduced to avoid a direct many-to-many relationship between Equipment and Feeder. As described in the use cases above, there are several reasons why an equipment must be able to participate in more than one Feeder (e.g., different network configurations, boundary equipment, simulations).

### Feeder self-association (PartOf / HasPart)

Equipment being associated with several feeders should not be confused with a sub-feeder being a part of a feeder. The PartOf relationship between feeders is used to model functional units that are supplied from the same source but should be distinguished for practical purposes.

### Feeder–Terminal association (NormalHeadTerminal)

Each Feeder should point to at least one Terminal to indicate where in the connectivity model it is supplied from. It is allowed to point to several Terminals to support cases where more than one ConductingEquipment serves as a logical starting point.

### Feeder illustration

The below illustration exemplifies how Feeder can be used to group equipment, including the use of feeder self-association and equipment being part of several feeders.

![Feeder illustration](feederIllustration.png)

## Modeling Guide

### Switch to Feeder connection

Switches contained in a feeder Bay should be connected to the same Feeder as the BusbarSection they are connected to, not the ACLineSegment.

## References

- IEC 61970-301 — CIM Base (defines Feeder as EquipmentContainer)
- [3lbits/cim4no](https://github.com/3lbits/cim4no) — Norwegian CIM profile
- [3lbits/NoCIMExtensions](https://github.com/3lbits/NoCIMExtensions) — Norwegian CIM Extensions
- [3lbits/CIM4NoUtility](https://github.com/3lbits/CIM4NoUtility) — CIM4No Utility tools
