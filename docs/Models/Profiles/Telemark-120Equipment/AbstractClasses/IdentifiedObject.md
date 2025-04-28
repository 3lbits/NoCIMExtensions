# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:IdentifiedObject](https://cim.ucaiug.io/ns#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/"
    style IdentifiedObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ACDCTerminal : inherits

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- AssetInfo : inherits

        AssetInfo
            click AssetInfo href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/AssetInfo/"
            style AssetInfo fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- BaseVoltage : inherits

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ConnectivityNode : inherits

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- EnergyArea : inherits

        EnergyArea
            click EnergyArea href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/EnergyArea/"
            style EnergyArea fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- GeographicalRegion : inherits

        GeographicalRegion
            click GeographicalRegion href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/GeographicalRegion/"
            style GeographicalRegion fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- LoadGroup : inherits

        LoadGroup
            click LoadGroup href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/LoadGroup/"
            style LoadGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- LoadResponseCharacteristic : inherits

        LoadResponseCharacteristic
            click LoadResponseCharacteristic href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/LoadResponseCharacteristic/"
            style LoadResponseCharacteristic fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimit : inherits

        OperationalLimit
            click OperationalLimit href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/OperationalLimit/"
            style OperationalLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimitSet : inherits

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimitType : inherits

        OperationalLimitType
            click OperationalLimitType href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/OperationalLimitType/"
            style OperationalLimitType fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- PowerSystemResource : inherits

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- SubGeographicalRegion : inherits

        SubGeographicalRegion
            click SubGeographicalRegion href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/SubGeographicalRegion/"
            style SubGeographicalRegion fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- TransformerEnd : inherits

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/TransformerEnd/"
            style TransformerEnd fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | direct |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | direct |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
