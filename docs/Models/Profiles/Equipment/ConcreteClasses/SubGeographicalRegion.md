# SubGeographicalRegion

_A subset of a geographical region of a power system network model._

**URI**: [cim:SubGeographicalRegion](https://cim.ucaiug.io/ns#SubGeographicalRegion)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class SubGeographicalRegion
    click SubGeographicalRegion href "/Models/Profiles/Equipment/ConcreteClasses/SubGeographicalRegion/"
    style SubGeographicalRegion fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- SubGeographicalRegion : inherits
            click IdentifiedObject href "/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SubGeographicalRegion --> GeographicalRegion : SubGeographicalRegion.Region

        GeographicalRegion
            click GeographicalRegion href "/Models/Profiles/Equipment/ConcreteClasses/GeographicalRegion/"
            style GeographicalRegion fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Line --> SubGeographicalRegion : Line.Region

        Line
            click Line href "/Models/Profiles/Equipment/ConcreteClasses/Line/"
            style Line fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Substation --> SubGeographicalRegion : Substation.Region

        Substation
            click Substation href "/Models/Profiles/Equipment/ConcreteClasses/Substation/"
            style Substation fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        SubGeographicalRegion : SubGeographicalRegion.Region
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/)
    * **SubGeographicalRegion**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Region | [cim:SubGeographicalRegion.Region](https://cim.ucaiug.io/ns#SubGeographicalRegion.Region) | 0..1 GeographicalRegion | The geographical region which this sub-geographical region is within. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
