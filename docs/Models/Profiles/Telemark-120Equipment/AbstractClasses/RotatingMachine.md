# RotatingMachine

_A rotating machine which may be used as a generator or motor._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:RotatingMachine](https://cim.ucaiug.io/ns#RotatingMachine)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RotatingMachine
    click RotatingMachine href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/RotatingMachine/"
    style RotatingMachine fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine <|-- SynchronousMachine : inherits

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- RotatingMachine : inherits
            click RegulatingCondEq href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> GeneratingUnit : RotatingMachine.GeneratingUnit

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RegulatingCondEq --> RegulatingControl : RegulatingCondEq.RegulatingControl

        RegulatingControl
            click RegulatingControl href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/RegulatingControl/"
            style RegulatingControl fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConductingEquipment --> BaseVoltage : ConductingEquipment.BaseVoltage

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerSystemResource --> AssetInfo : PowerSystemResource.AssetDataSheet

        AssetInfo
            click AssetInfo href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/AssetInfo/"
            style AssetInfo fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> Equipment : OperationalLimitSet.Equipment

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> ConductingEquipment : Terminal.ConductingEquipment

        Terminal
            click Terminal href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        RotatingMachine : RotatingMachine.GeneratingUnit
        RegulatingCondEq : RegulatingCondEq.RegulatingControl
        ConductingEquipment : ConductingEquipment.BaseVoltage
        Equipment : Equipment.aggregate
        Equipment : Equipment.normallyInService
        Equipment : Equipment.EquipmentContainer
        PowerSystemResource : PowerSystemResource.locationMethodKind
        PowerSystemResource : PowerSystemResource.AssetDataSheet
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/Telemark-120Equipment/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/Telemark-120Equipment/AbstractClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/Telemark-120Equipment/AbstractClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/Telemark-120Equipment/AbstractClasses/RegulatingCondEq/)
                        * **RotatingMachine**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| GeneratingUnit | [cim:RotatingMachine.GeneratingUnit](https://cim.ucaiug.io/ns#RotatingMachine.GeneratingUnit) | 0..1 GeneratingUnit | A synchronous machine may operate as a generator and as such becomes a member of a generating unit. | direct |
| RegulatingControl | [cim:RegulatingCondEq.RegulatingControl](https://cim.ucaiug.io/ns#RegulatingCondEq.RegulatingControl) | 0..1 RegulatingControl | The regulating control scheme in which this equipment participates. | RegulatingCondEq |
| BaseVoltage | [cim:ConductingEquipment.BaseVoltage](https://cim.ucaiug.io/ns#ConductingEquipment.BaseVoltage) | 0..1 BaseVoltage | Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. | ConductingEquipment |
| aggregate | [cim:Equipment.aggregate](https://cim.ucaiug.io/ns#Equipment.aggregate) | 0..1 boolean | The aggregate attribute is used to indicate that the object is an aggregate of other objects. The aggregate attribute is used to indicate that the object is an aggregate of other objects. The aggregate attribute is used to indicate that the object is an aggregate of other objects. | Equipment |
| normallyInService | [cim:Equipment.normallyInService](https://cim.ucaiug.io/ns#Equipment.normallyInService) | 0..1 boolean | The normallyInService attribute is used to indicate that the object is normally in service. The normallyInService attribute is used to indicate that the object is normally in service. The normallyInService attribute is used to indicate that the object is normally in service. | Equipment |
| EquipmentContainer | [cim:Equipment.EquipmentContainer](https://cim.ucaiug.io/ns#Equipment.EquipmentContainer) | 0..1 EquipmentContainer | Container of this equipment. | Equipment |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| AssetDataSheet | [cim:PowerSystemResource.AssetDataSheet](https://cim.ucaiug.io/ns#PowerSystemResource.AssetDataSheet) | 0..1 AssetInfo | Datasheet information for this power system resource. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
