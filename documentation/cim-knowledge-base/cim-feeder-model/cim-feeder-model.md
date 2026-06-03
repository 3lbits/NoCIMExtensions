---
title: "CIM Feeder Containment Model"
type: class-model
author: "NoCIMExtensions"
created: 2026-06-01
modified: 2026-06-01
modified-by: "GitHub Copilot"
status: draft
tags: [cim, feeder, containment, resource-container, terminal]
cim-version: "IEC 61970-301"
norwegian-profile: "NoCIMExtensions"
sources:
  - https://github.com/3lbits/NoCIMExtensions
---

# CIM Feeder Containment Model

## Overview

This document defines how feeder containment is modeled in NoCIMExtensions. Large parts of the distribution grid are operated as single/radial feeders, therefore, there is a need to express which feeder conducting equipment is part of. Feeder refers to a grouping of equipment that is supplied from one end only.

## Classes

### Class diagram
![alt text](feederModel.png)

### nc:Feeder

**Inherits from:** nc:ResourceContainer

**Description:** A Feeder is a ResourceContainer that groups distribution resources as a system functional unit of the distribution network.
It may represent equipment supplied from or supplying to one or more substations, and does not prescribe power flow direction or topology. A Feeder may contain installations, prosumers, or other feeders.
A Feeder serves as an organizational and operational unit for applying measurement, scheduling, and operational limits, independent of its instantaneous connectivity or state.


**Attributes:**

|Namespace| Attribute | Type | Description |
|---------|-----------|------|-------------|
|cim| mRID | string | Master resource identifier |
|cim| name | string | Human-readable name |
|cim| description | string | Free-text description |
|nc| kind | FeederKind | Kind of Feeder |
|nc| otherKind | string | Text describing the feeder kind when other is selected in the kind |
|nc| phaseInfo | PhaseCode | Phase information |


**Relationships:**

| Namespace | Target Class | Cardinality from | Cardinality to | Description |
|-----------|--------------|------------------|----------------|-------------|
|nc| Feeder | 0..* | 0..1 | The feeder is part of this feeder |
|nc| Terminal | 0..1 | 1..* | The normal head of terminals of the feeder |
|nc-no| FeederConnection | 1..1 | 0..*| The connection the feeder has to an equipment |


### nc-no:FeederConnection

**Inherits from:** cim:IdentifiedObject

**Description:** A logical connection point between Equipment and Feeder.


**Attributes:**

|Namespace| Attribute | Type | Description |
|---------|-----------|------|-------------|
|cim| mRID | string | Master resource identifier |
|cim| name | string | Human-readable name |
|cim| description | string | Free-text description |


**Relationships:**

| Namespace | Target Class | Cardinality from | Cardinality to | Description |
|-----------|--------------|------------------|----------------|-------------|
|nc-no| Equipment | 0..* | 0..1 | A connection to a feeder for this equipment |
|nc-no| Feeder | 0..* | 1..1| The connection to a feeder for an equipment |

### cim:Terminal

**Inherits from:** cim:ACDCTerminal

**Description:** An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.


**Attributes:**

|Namespace| Attribute | Type | Description |
|---------|-----------|------|-------------|
|cim| mRID | string | Master resource identifier |
|cim| name | string | Human-readable name |
|cim| description | string | Free-text description |
|cim| phases | PhaseCode | Represents the normal network phasing condition. If the attribute is missing, three phases (ABC) shall be assumed, except for terminals of grounding classes (specializations of EarthFaultCompensator, GroundDisconnector, and Ground) which will be assumed to be N. Therefore, phase code ABCN is explicitly declared when needed, e.g. for star point grounding equipment. <br> The phase code on terminals connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two terminals shall be consistent |


**Relationships:**

| Namespace | Target Class | Cardinality from | Cardinality to | Description |
|-----------|--------------|------------------|----------------|-------------|
|nc| Feeder | 1..* | 0..1 | The feeder that this terminal normally feeds. Only specified for the terminal at head of feeders |



### nc:ResourceContainer

**Inherits from:** cim:PowerSystemResource

**Description:** Containment of resources that collectively provide a system function and are subject to measurement, scheduling and operable within defined limits.


**Attributes:**

|Namespace| Attribute | Type | Description |
|---------|-----------|------|-------------|
|cim| mRID | string | Master resource identifier |
|cim| name | string | Human-readable name |
|cim| description | string | Free-text description |


**Relationships:**

| Namespace | Target Class | Cardinality from | Cardinality to | Description |
|-----------|--------------|------------------|----------------|-------------|
|nc| Equipment | 0..1 | 0..* | The resource container to which the equipment belongs to. |


## Model justification

### FeederConnection
The FeederConnection class was introduced to avoid many-to-many relationships between Equipment and Feeder. The feeder is to be considered a functional unit that is "independent of its instantaneous connectivity or state", for it to serve its organisational and operational purpose there is a need to support that equipment may participate in several Feeders. 

Use cases for when it may be desireable to associate one Equipment to multiple Feeders are: 
> When the utility needs feeder definitions for more than one network configuration. In practice, this means the same Equipment may be part of one Feeder in the normal configuration and part of another Feeder in an operational or contingency configuration.

> Boundary equipment that ties distinct feeders together that the utility want to include in feeder based model exchange for all feeders. Examples include tie switches or transformers at the edge of a radial feeder.

### Feeder self-association
	
Equipment being associated with several feeders should not to be confused with a subfeeder being a part of a feeder. The part of relationship between feeders is used to model functional units that are supplied from the same source but should be distinguished for practical purposes. 

### Feeder-Terminal association

Each Feeder should point to at least one Terminal to indicate where in the connectivity model it is supplied from. It is allowed to point to several Terminals to support cases where more than one ConductingEquipment serves as a logical starting point. 

### Feeder illustration
The below illustration examplifies how Feeder can be used to group equipment, including the use of feeder self-association and equipment being part of several feeders.
![alt text](feederIllustration.png)

## Modeling Guide

### Switch to Feeder connection
Switches contained in a feeder Bay should be connected to the same Feeder as the Busbarsection they are connected to, not the ACLineSegment.

