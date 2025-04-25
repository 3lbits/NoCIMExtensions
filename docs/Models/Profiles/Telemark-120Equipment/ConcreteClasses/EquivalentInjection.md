# EquivalentInjection

_This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point of connection._

**URI**: [cim:EquivalentInjection](https://cim.ucaiug.io/ns#EquivalentInjection)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class EquivalentInjection
    click EquivalentInjection href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/EquivalentInjection/"
    style EquivalentInjection fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EquivalentEquipment <|-- EquivalentInjection : inherits
            click EquivalentEquipment href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/EquivalentEquipment/"
            style EquivalentEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EquivalentEquipment : inherits
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

        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> Equipment : OperationalLimitSet.Equipment

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> ConductingEquipment : Terminal.ConductingEquipment

        Terminal
            click Terminal href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EquivalentInjection : EquivalentInjection.maxP
        EquivalentInjection : EquivalentInjection.maxQ
        EquivalentInjection : EquivalentInjection.minP
        EquivalentInjection : EquivalentInjection.minQ
        EquivalentInjection : EquivalentInjection.regulationCapability
        EquivalentEquipment : EquivalentEquipment.EquivalentNetwork
        Equipment : Equipment.aggregate
        Equipment : Equipment.normallyInService
        Equipment : Equipment.EquipmentContainer
        PowerSystemResource : PowerSystemResource.locationMethodKind
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/Telemark-120Equipment/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/Telemark-120Equipment/AbstractClasses/ConductingEquipment/)
                * [EquivalentEquipment](/Models/Profiles/Telemark-120Equipment/AbstractClasses/EquivalentEquipment/)
                    * **EquivalentInjection**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| maxP | [cim:EquivalentInjection.maxP](https://cim.ucaiug.io/ns#EquivalentInjection.maxP) | 0..1 ActivePower | Maximum active power of the injection. | direct |
| maxQ | [cim:EquivalentInjection.maxQ](https://cim.ucaiug.io/ns#EquivalentInjection.maxQ) | 0..1 ReactivePower | Maximum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. | direct |
| minP | [cim:EquivalentInjection.minP](https://cim.ucaiug.io/ns#EquivalentInjection.minP) | 0..1 ActivePower | Minimum active power of the injection. | direct |
| minQ | [cim:EquivalentInjection.minQ](https://cim.ucaiug.io/ns#EquivalentInjection.minQ) | 0..1 ReactivePower | Minimum reactive power of the injection.  Used for modelling of infeed for load flow exchange. Not used for short circuit modelling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used. | direct |
| regulationCapability | [cim:EquivalentInjection.regulationCapability](https://cim.ucaiug.io/ns#EquivalentInjection.regulationCapability) | 0..1 boolean | Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. If true the EquivalentInjection can regulate. If false the EquivalentInjection cannot regulate. ReactiveCapabilityCurve can only be associated with EquivalentInjection  if the flag is true. | direct |
| EquivalentNetwork | [cim:EquivalentEquipment.EquivalentNetwork](https://cim.ucaiug.io/ns#EquivalentEquipment.EquivalentNetwork) | 0..1 EquivalentNetwork | The equivalent where the reduced model belongs. | EquivalentEquipment |
| aggregate | [cim:Equipment.aggregate](https://cim.ucaiug.io/ns#Equipment.aggregate) | 0..1 boolean | The aggregate attribute is used to indicate that the object is an aggregate of other objects. The aggregate attribute is used to indicate that the object is an aggregate of other objects. The aggregate attribute is used to indicate that the object is an aggregate of other objects. | Equipment |
| normallyInService | [cim:Equipment.normallyInService](https://cim.ucaiug.io/ns#Equipment.normallyInService) | 0..1 boolean | The normallyInService attribute is used to indicate that the object is normally in service. The normallyInService attribute is used to indicate that the object is normally in service. The normallyInService attribute is used to indicate that the object is normally in service. | Equipment |
| EquipmentContainer | [cim:Equipment.EquipmentContainer](https://cim.ucaiug.io/ns#Equipment.EquipmentContainer) | 0..1 EquipmentContainer | Container of this equipment. | Equipment |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
