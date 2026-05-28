---
title: "CIM Container Model"
type: class-model
author: "Thomas Ranvik Eriksen"
created: 2026-05-07
modified: 2026-05-07
modified-by: "Thomas Ranvik Eriksen"
status: draft
tags: [cim, container, substation, voltage-level, bay, line, feeder]
cim-version: "IEC 61970-301"
norwegian-profile: "CIM4No"
sources:
  - https://github.com/3lbits/cim4no
  - https://github.com/3lbits/NoCIMExtensions
  - https://github.com/3lbits/CIM4NoUtility
---

# CIM Container Model

## Overview

The CIM Container Model defines the hierarchical structure used to organize power system equipment into logical groupings. Containers represent the physical or logical locations where equipment resides — from high-voltage transmission lines down to secondary substations serving end consumers.

This document covers the primary container classes: **Line**, **Substation**, **VoltageLevel**, **Bay**, **FeederLine**, and **SecondarySubstation**.

## Classes

### Line

**Description:** A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point. A Line contains one or more line segments (ACLineSegment).

**Contains:**

- ACLineSegments
- ConnectivityNodes
- Junctions

**When to use Line (required):**

- Substation to Substation
- Substation to SecondarySubstation
- SecondarySubstation to SecondarySubstation

> If the connection does not match the above cases, you can use **FeederLine** instead.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| description | string | Free-text description |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Contains | ACLineSegment | 0..* | Line segments that make up this line |
| Contains | ConnectivityNode | 0..* | Connectivity nodes within this line |
| Region | SubGeographicalRegion | 0..1 | Geographic region the line is located in |

---

### Substation

**Description:** A facility that serves as a point of connection and switching for the electrical network. Contains one or more voltage levels and provides the physical grouping of equipment at a site.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| description | string | Free-text description |
| Region | SubGeographicalRegion | Geographic region |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Contains | VoltageLevel | 1..* | Voltage levels within this substation |
| Region | SubGeographicalRegion | 0..1 | Geographic region the substation is in |

---

### VoltageLevel

**Description:** A collection of equipment at one common system voltage forming a switchgear. The voltage level is contained within a substation and contains bays.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| highVoltageLimit | Voltage | Upper limit of the voltage range |
| lowVoltageLimit | Voltage | Lower limit of the voltage range |
| BaseVoltage | BaseVoltage | Nominal voltage for this level |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Substation | Substation | 1 | Parent substation containing this voltage level |
| Contains | Bay | 0..* | Bays at this voltage level |

---

### Bay

**Description:** A switching arrangement within a voltage level that groups equipment for a specific purpose (e.g., a feeder bay, transformer bay, bus-coupler bay). Bays are the lowest level of the container hierarchy within a substation.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| description | string | Free-text description |
| bayEnergyMeasFlag | boolean | Indicates if energy measurements are taken at the bay |
| bayPowerMeasFlag | boolean | Indicates if power measurements are taken at the bay |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| VoltageLevel | VoltageLevel | 1 | Parent voltage level |
| Contains | ConductingEquipment | 0..* | Equipment within this bay (switches, breakers, etc.) |

---

### FeederLine

**Description:** Represents a distribution feeder line extending from a substation bay out into the distribution network. FeederLine is a simpler way of containerizing compared to Line — it does not require the full substation-to-substation topology. In Norwegian grid modelling, this is commonly used to model the low-voltage feeders leaving a substation.

**Contains:**

- ACLineSegments
- ConnectivityNodes
- Switches
- ConformLoads
- Junctions
- BusbarSections? --> Should this be allowed if you model a CableBox in a FeederLine and a CableBox has a BusbarSection

**When to use FeederLine:**

- SecondarySubstation to ConformLoad
- Any connection that does not require a Line (i.e., not Substation↔Substation, Substation↔SecondarySubstation, or SecondarySubstation↔SecondarySubstation)

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| description | string | Free-text description |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Contains | ACLineSegment | 0..* | Line segments in the feeder |
| Contains | ConnectivityNode | 0..* | Connectivity nodes in the feeder |
| Contains | Switch | 0..* | Switches in the feeder |
| Contains | ConformLoad | 0..* | Loads connected via this feeder |

---

### SecondarySubstation

**Description:** A distribution substation (nettstasjon) that transforms medium voltage to low voltage for end consumers. In the Norwegian grid model, this is a key container for LV equipment and meters.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |
| description | string | Free-text description |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Contains | VoltageLevel | 1..* | Voltage levels (typically one MV and one LV) |
| Region | SubGeographicalRegion | 0..1 | Geographic region |
| NormalEnergizedBy | FeederLine | 0..1 | Feeder that normally supplies this secondary substation |

## Norwegian Extensions

In the Norwegian CIM profile (CIM4No / NoCIMExtensions), the container model is extended with:

- **SecondarySubstation** is explicitly modelled as a distinct class (not just a Substation with a specific function). This reflects Norwegian grid terminology where "nettstasjon" is a first-class concept.
- **FeederLine** is used extensively for medium-voltage distribution feeders, with explicit relationships to energizing substations.
- Container naming conventions follow Norwegian DSO practices (e.g., station identifiers from NIS systems).

## LV Container Modelling Cases

The following cases illustrate different approaches to modelling the low-voltage (LV) distribution network from a secondary substation. Each case shows both the **container hierarchy** (which containers own which equipment) and the **circuit topology** (terminals, connectivity nodes, and equipment).

### Case 1: FeederLine Only

**Container:** [cim_container_lv_feeder_line_only_container.mmd](mmd/cim_container_lv_feeder_line_only_container.mmd)
**Circuit:** [cim_container_lv_feeder_line_only_circuit.mmd](mmd/cim_container_lv_feeder_line_only_circuit.mmd)

**Description:** All LV cables from the substation are modelled as individual FeederLines. No Line containers are used on the LV side.

**Positives:**

- Simplest container model — one FeederLine per outgoing cable
- Each feeder is independently identifiable for fault isolation and metering
- Minimal container hierarchy depth

**Issues:**

- Cable boxes (kabelskap) are not modelled as containers (SecondarySubstation) — junction points in the LV network have no explicit representation
- Cannot model cable junctions or branching points that connect separate substations
- Does not support modelling a cable path between two substations (requires Line)
- All equipment belongs to FeederLine — no intermediate VoltageLevel grouping for junction points

---

### Case 2: FeederLine + Line (Mixed)

**Container:** [cim_container_lv_feeder_line_container.mmd](mmd/cim_container_lv_feeder_line_container.mmd)
**Circuit:** [cim_container_lv_feeder_line_circuit.mmd](mmd/cim_container_lv_feeder_line_circuit.mmd)

**Description:** Some cables use FeederLine (direct to consumer), while others use Line to reach a cable junction (secondary VoltageLevel or cable grid node) where they branch into further FeederLines.

**Positives:**

- Correctly models cable junctions as intermediate VoltageLevels with a Substation
- Supports cable grid topology (ring/mesh networks on LV)
- Clear separation between trunk cables (Line) and consumer feeders (FeederLine)

**Issues:**

- More complex container hierarchy — requires additional Substations and VoltageLevels at junction points
- All ACLS between Bay and intermediate VoltageLevel are directly connected to CN_VoltageLevel without separation
- Harder to understand for simple radial networks where Case 1 suffices

---

### Case 3: Line + Jumper (Separated)

**Container:** [cim_container_lv_line_jumper.mmd](mmd/cim_container_lv_line_jumper.mmd)
**Circuit:** [cim_container_lv_line_jumper_circuit.mmd](mmd/cim_container_lv_line_jumper_circuit.mmd)

**Description:** Like Case 2, but Jumpers are inserted between the Line ACLS and the VoltageLevel ConnectivityNodes. Each Jumper sits in its own Bay, creating a clean boundary between the Line container and the VoltageLevel container.

**Positives:**

- Clean container boundary — ACLS never directly connect to a VoltageLevel CN; Jumpers provide explicit separation
- Each connection point has its own Bay, making it easy to identify and switch individual cable connections
- Supports BusbarSection at each VoltageLevel for explicit bus modelling
- Models the physical reality of cable termination points (bolted/clamped connections)
- Easier to add/remove feeders without restructuring existing topology

**Issues:**

- Most complex container hierarchy — additional Bays and Jumpers increase the object count
- Jumpers add nodes to the topology that must be processed (though zero-impedance)
- May be over-engineering for simple radial LV networks
- Requires tooling to understand that Jumper=zero-impedance connection point

---

### Case 4: Line Only (No FeederLine)

**Container:** [cim_container_lv_line_container.mmd](mmd/cim_container_lv_line_container.mmd)
**Circuit:** [cim_container_lv_line_circuit.mmd](mmd/cim_container_lv_line_circuit.mmd)

**Description:** All LV cables are modelled using Line containers, with intermediate VoltageLevels at junction points. FeederLines are used only for the final consumer drops.

**Positives:**

- Consistent use of Line for all cable segments between switching points
- Full substation-to-substation path modelling even on LV
- Clear where Lines end and FeederLines begin (at the last VoltageLevel before consumer)

**Issues:**

- ACLS connect directly to VoltageLevel CNs without Jumper separation (compare with Case 3)
- Requires Substations at every junction point, which may be excessive for simple cabinet nodes
- FeederLines still needed for consumer connections — so the model is never "Line only" in practice

## MV Feeder Modelling (HV to MV Substation)

This case covers the medium-voltage feeder bay (Norwegian: *avgang*) at a primary substation (HV/MV), where an outgoing MV feeder connects to the distribution network via switches, busbars, and protection equipment.

> **Note:** "Feeder" here refers to the Norwegian concept "avgang" — a physical outgoing circuit from a substation. This is not the CIM class `Feeder`, although the principle is similar.

**Circuit:** [cim_container_mv_feeder_circuit.mmd](mmd/cim_container_mv_feeder_circuit.mmd)

**Description:** The MV feeder bay is modelled within a Substation's VoltageLevel. Two BusbarSections (double busbar) connect through Switches in Bays to a central ConnectivityNode. From that CN, the outgoing ACLS (Line) feeds the MV distribution network. A Junction marks the connection point, and a GroundDisconnector with Ground provides earthing capability.

**Structure:**

- Substation contains VoltageLevel (MV)
- VoltageLevel contains 2 BusbarSections (double busbar arrangement — both belong to the same VoltageLevel)
- All protection equipment and contained equipment in the "avgang" belongs to a single Bay
- Central CN connects to: Junction, outgoing ACLS (in Line), GroundDisconnector → Ground

**Positives:**

- Standard substation bay model — well-understood and widely used
- Double busbar provides redundancy and maintenance flexibility
- Junction explicitly marks the feeder connection point
- GroundDisconnector/Ground supports safety switching procedures
- Clear container boundaries — all switching equipment in Bays, busbars at VoltageLevel

**Issues:**

- Only covers the substation-side of the feeder — the Line to the next substation is a separate container
- Requires consistent modelling of all feeder bays to maintain uniformity

## T-Junction Modelling

A T-junction occurs where an overhead line branches into multiple directions (typically 3 ACLS meeting at a single ConnectivityNode). This is the normal case for overhead line junctions where you clamp a second overhead line to the first.

> **Note:** You can also use this pattern for cable cabinets (kabelskap), but for cable junctions it is recommended to use a full Substation model (see LV Container Modelling Cases above).

There are four ways to model a T-junction:

### Option A: Substation + VoltageLevel + Junction + Line

**Diagram:** [cim_container_t-junction_a.mmd](mmd/cim_container_t-junction_a.mmd)

Model the junction point as a Substation with a VoltageLevel. The Junction element sits inside the VoltageLevel. Each ACLS is contained in a separate Line connecting this Substation to the adjacent Substations/SecondarySubstations.

**Positives:**

- Junction point is explicitly modelled as a switching/connection site
- Clean container separation — each Line has its own ACLS
- Supports future expansion (adding switches, metering, etc.)
- Junction is identifiable as a physical location

**Issues:**

- Higher object count for a simple overhead line branching point
- May be over-engineering for a pole-mounted clamp junction

---

### Option B: Substation + VoltageLevel + Bay + Jumper + Line

**Diagram:** [cim_container_t-junction_b.mmd](mmd/cim_container_t-junction_b.mmd)

Model the junction point as a Substation with a VoltageLevel and Bays. Each Line connects via a Jumper in its own Bay, providing explicit separation between the Line container and the VoltageLevel container.

**Positives:**

- Cleanest container boundaries — Jumpers provide explicit separation between containers
- Each connection has its own Bay for individual identification and switching
- Consistent with Case 3 (Line + Jumper) pattern
- Models physical termination points (bolted connections at the cabinet)

**Issues:**

- Most complex option — additional Bays and Jumpers increase object count
- Over-engineering for a simple T-junction that has no switchgear
- Jumpers add zero-impedance nodes to the topology

---

### Option C: Single Line with Junction (Simplest)

**Diagram:** [cim_container_t-junction_c.mmd](mmd/cim_container_t-junction_c.mmd)

All 3 ACLS and the Junction are placed in the same Line container. The ConnectivityNode at the branching point is also inside that Line.

**Positives:**

- Simplest possible model — one Line container holds everything
- No extra Substations, VoltageLevels, or Bays needed
- Minimal object count
- Easy to implement and understand

**Issues:**

- Junction point has no separate container identity — cannot be independently addressed
- All branches belong to the same Line, which may conflict with the rule that Line is Substation-to-Substation
- Cannot easily separate the branches for fault isolation or asset management
- Adding switchgear later requires restructuring the container model

---

### Option D: Single FeederLine with Junction (LV only)

**Diagram:** [cim_container_t-junction_d.mmd](mmd/cim_container_t-junction_d.mmd)

For low-voltage grids, all 3 ACLS are placed in the same FeederLine container. The ConnectivityNode at the branching point is also inside that FeederLine. A Junction element is optional — it can be included to explicitly mark the branching point, but is not required.

**Positives:**

- Simplest possible model for LV T-junctions — one FeederLine holds everything
- No extra Substations, VoltageLevels, Bays, or Lines needed
- Minimal object count
- Appropriate for LV where the Substation-to-Substation Line rule does not apply

**Issues:**

- Junction point has no separate container identity
- Cannot easily separate branches for fault isolation or asset management
- Adding switchgear later requires restructuring the container model
- Only valid for LV — MV/HV junctions between substations require Line

## References

- [3lbits/cim4no](https://github.com/3lbits/cim4no) — Norwegian CIM profile definitions
- [3lbits/NoCIMExtensions](https://github.com/3lbits/NoCIMExtensions) — Norwegian CIM Extensions
- [3lbits/CIM4NoUtility](https://github.com/3lbits/CIM4NoUtility) — CIM4No Utility tools
- IEC 61970-301 — CIM Base (Energy Management System Application Program Interface)
- IEC 61968-11 — CIM Extensions for Distribution
- CIM meetings
