---
name: cim-knowledge-base
description: "Create, update, and look up CIM (Common Information Model) knowledge base documents. Use when: documenting CIM classes, container models, profile structures, Norwegian extensions, or looking up CIM domain knowledge for the data platform."
argument-hint: "Describe what CIM topic to create, update, or look up"
---

# CIM Knowledge Base

## When to Use

- Creating a new CIM knowledge base document (class descriptions, container models, profiles)
- Looking up CIM domain knowledge (classes, attributes, relationships, extensions)
- Updating existing CIM documentation with new insights or corrections
- Understanding how Norwegian CIM extensions relate to IEC standards
- Referencing CIM models during development or integration work

> **Not research.** If you are evaluating CIM-related tooling or comparing approaches, use the `create-research` skill. The CIM knowledge base is for documenting the domain model itself.

## Knowledge Base Conventions

All CIM knowledge base documents are stored in the `cim-knowledge-base/` folder at the repository root.

### File Naming

- Use **kebab-case** (lowercase, hyphens, no spaces or special characters): `cim-container-model.md`
- Always use `.md` extension
- Prefix with `cim-` only when it adds clarity; otherwise use the domain concept name

### Frontmatter

Every CIM knowledge base document must include YAML frontmatter:

```yaml
---
title: "CIM Container Model"
type: class-model           # class-model | profile | mapping | overview | extension
author: ""                  # who created the document
created: 2026-05-07         # ISO 8601 date
modified: 2026-05-07        # updated on each edit
modified-by: ""             # who last edited
status: draft               # draft | in-progress | complete | superseded
tags: []                    # e.g. [cim, container, substation, voltage-level]
cim-version: ""             # e.g. "CIM100", "IEC 61970-301:2020"
norwegian-profile: ""       # e.g. "CIM4No v2.0", "NoCIMExtensions"
sources: []                 # URLs or references consulted
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Human-readable title |
| `type` | Yes | One of: `class-model`, `profile`, `mapping`, `overview`, `extension` |
| `author` | Yes | Creator of the document |
| `created` | Yes | ISO 8601 date |
| `modified` | Yes | ISO 8601 date, updated on each edit |
| `modified-by` | Yes | Who last edited |
| `status` | Yes | Lifecycle: `draft` → `in-progress` → `complete` (or `superseded`) |
| `tags` | No | Freeform tags for discoverability |
| `cim-version` | No | IEC CIM version the document relates to |
| `norwegian-profile` | No | Norwegian CIM profile/extension version |
| `sources` | No | URLs, documentation links, or references consulted |

### Language

- Write CIM knowledge base documents in **English**

### Document Structure (class-model type)

```markdown
# Title

## Overview
Brief description of what this model covers, its purpose in the CIM, and scope.

## Classes

### ClassName

**Description:** What this class represents in the power system domain.

**Attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| mRID | string | Master resource identifier |
| name | string | Human-readable name |

**Relationships:**

| Relationship | Target Class | Cardinality | Description |
|--------------|--------------|-------------|-------------|
| Contains | ChildClass | 0..* | Description of the relationship |

## Norwegian Extensions
How this model is extended or profiled in Norwegian CIM standards (CIM4No, NoCIMExtensions).

## References
- Links to relevant IEC standards, GitHub repos, or other sources
```

### Document Structure (profile type)

```markdown
# Title

## Overview
What this profile defines and its purpose.

## Profile Scope
Which CIM classes and attributes are included/constrained.

## Constraints
Specific rules, cardinality restrictions, or mandatory attributes.

## References
```

### Document Structure (overview type)

```markdown
# Title

## Overview
High-level summary of the CIM topic.

## Key Concepts
Important terms and their meanings.

## Relationships
How concepts relate to each other.

## References
```

## Key Reference Repositories

These open-source GitHub repositories are primary references for Norwegian CIM work:

| Repository | Description |
|------------|-------------|
| [3lbits/cim4no](https://github.com/3lbits/cim4no) | CIM for Norway — Norwegian CIM profile |
| [3lbits/NoCIMExtensions](https://github.com/3lbits/NoCIMExtensions) | Norwegian CIM Extensions |
| [3lbits/CIM4NoUtility](https://github.com/3lbits/CIM4NoUtility) | CIM4No Utility tools and resources |

## Workflow

### Creating a new document

1. Determine the document type (`class-model`, `profile`, `mapping`, `overview`, `extension`)
2. Create the file in `cim-knowledge-base/` with kebab-case naming
3. Add frontmatter with all required fields
4. Follow the appropriate structure template
5. Include references to relevant GitHub repos and IEC standards

### Looking up information

1. Search existing documents in `cim-knowledge-base/` for the topic
2. If found, read and present the relevant information
3. If not found, inform the user and offer to create a new document

### Updating a document

1. Read the existing document
2. Update the content and `modified` / `modified-by` fields
3. If the document status changes, update `status` accordingly
