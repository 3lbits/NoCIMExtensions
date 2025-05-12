# BaseVoltage

_Defines a system base voltage which is referenced._

**URI**: [cim:BaseVoltage](https://cim.ucaiug.io/ns#BaseVoltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class BaseVoltage
    click BaseVoltage href "/Models/Profiles/AviationObstacle/ConcreteClasses/BaseVoltage/"
    style BaseVoltage fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- BaseVoltage : inherits
            click IdentifiedObject href "/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AssetDeployment --> BaseVoltage : AssetDeployment.BaseVoltage

        AssetDeployment
            click AssetDeployment href "/Models/Profiles/AviationObstacle/ConcreteClasses/AssetDeployment/"
            style AssetDeployment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        BaseVoltage : BaseVoltage.nominalVoltage
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/AviationObstacle/AbstractClasses/IdentifiedObject/)
    * **BaseVoltage**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| nominalVoltage | [cim:BaseVoltage.nominalVoltage](https://cim.ucaiug.io/ns#BaseVoltage.nominalVoltage) | 0..1 Voltage | The power system resource's base voltage.  Shall be a positive value and not zero. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/AviationObstacle/1.0](https://ap-no.cim4.eu/AviationObstacle/1.0)
