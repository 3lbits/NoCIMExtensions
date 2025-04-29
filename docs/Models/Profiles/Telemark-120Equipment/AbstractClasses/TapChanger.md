# TapChanger

_Mechanism for changing transformer winding tap positions._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:TapChanger](https://cim.ucaiug.io/ns#TapChanger)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class TapChanger
    click TapChanger href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/TapChanger/"
    style TapChanger fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChanger <|-- RatioTapChanger : inherits

        RatioTapChanger
            click RatioTapChanger href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/RatioTapChanger/"
            style RatioTapChanger fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- TapChanger : inherits
            click PowerSystemResource href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> AssetInfo : PowerSystemResource.AssetDataSheet

        AssetInfo
            click AssetInfo href "/Models/Profiles/Telemark-120Equipment/ConcreteClasses/AssetInfo/"
            style AssetInfo fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        TapChanger : TapChanger.highStep
        TapChanger : TapChanger.lowStep
        TapChanger : TapChanger.ltcFlag
        TapChanger : TapChanger.neutralStep
        TapChanger : TapChanger.neutralU
        TapChanger : TapChanger.normalStep
        PowerSystemResource : PowerSystemResource.locationMethodKind
        PowerSystemResource : PowerSystemResource.AssetDataSheet
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Telemark-120Equipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/Telemark-120Equipment/AbstractClasses/PowerSystemResource/)
        * **TapChanger**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| highStep | [cim:TapChanger.highStep](https://cim.ucaiug.io/ns#TapChanger.highStep) | 0..1 integer | Highest possible tap step position, advance from neutral.The attribute shall be greater than lowStep. | direct |
| lowStep | [cim:TapChanger.lowStep](https://cim.ucaiug.io/ns#TapChanger.lowStep) | 0..1 integer | Lowest possible tap step position, retard from neutral. | direct |
| ltcFlag | [cim:TapChanger.ltcFlag](https://cim.ucaiug.io/ns#TapChanger.ltcFlag) | 0..1 boolean | Specifies whether or not a TapChanger has load tap changing capabilities. | direct |
| neutralStep | [cim:TapChanger.neutralStep](https://cim.ucaiug.io/ns#TapChanger.neutralStep) | 0..1 integer | The neutral tap step position for this winding.The attribute shall be equal to or greater than lowStep and equal or less than highStep.It is the step position where the voltage is neutralU when the other terminals of the transformer are at the ratedU.  If there are other tap changers on the transformer those taps are kept constant at their neutralStep. | direct |
| neutralU | [cim:TapChanger.neutralU](https://cim.ucaiug.io/ns#TapChanger.neutralU) | 0..1 Voltage | Voltage at which the winding operates at the neutral tap setting. It is the voltage at the terminal of the PowerTransformerEnd associated with the tap changer when all tap changers on the transformer are at their neutralStep position.  Normally neutralU of the tap changer is the same as ratedU of the PowerTransformerEnd, but it can differ in special cases such as when the tapping mechanism is separate from the winding more common on lower voltage transformers.This attribute is not relevant for PhaseTapChangerAsymmetrical, PhaseTapChangerSymmetrical and PhaseTapChangerLinear. | direct |
| normalStep | [cim:TapChanger.normalStep](https://cim.ucaiug.io/ns#TapChanger.normalStep) | 0..1 integer | The tap step position used in normal network operation for this winding. For a Fixed tap changer indicates the current physical tap setting.The attribute shall be equal to or greater than lowStep and equal to or less than highStep. | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| AssetDataSheet | [cim:PowerSystemResource.AssetDataSheet](https://cim.ucaiug.io/ns#PowerSystemResource.AssetDataSheet) | 0..1 AssetInfo | Datasheet information for this power system resource. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
