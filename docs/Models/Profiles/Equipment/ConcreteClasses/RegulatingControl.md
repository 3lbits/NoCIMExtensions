# RegulatingControl

_Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Remote bus voltage control is possible by specifying the controlled terminal located at some place remote from the controlling equipment.The specified terminal shall be associated with the connectivity node of the controlled point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers.For flow control, load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment.The attribute minAllowedTargetValue and maxAllowedTargetValue are required in the following cases:- For a power generating module operated in power factor control mode to specify maximum and minimum power factor values;- Whenever it is necessary to have an off center target voltage for the tap changer regulator. For instance, due to long cables to off shore wind farms and the need to have a simpler setup at the off shore transformer platform, the voltage is controlled from the land at the connection point for the off shore wind farm. Since there usually is a voltage rise along the cable, there is typical and overvoltage of up 3-4 kV compared to the on shore station. Thus in normal operation the tap changer on the on shore station is operated with a target set point, which is in the lower parts of the dead band.The attributes minAllowedTargetValue and maxAllowedTargetValue are not related to the attribute targetDeadband and thus they are not treated as an alternative of the targetDeadband. They are needed due to limitations in the local substation controller. The attribute targetDeadband is used to prevent the power flow from move the tap position in circles (hunting) that is to be used regardless of the attributes minAllowedTargetValue and maxAllowedTargetValue._

**URI**: [cim:RegulatingControl](https://cim.ucaiug.io/ns#RegulatingControl)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class RegulatingControl
    click RegulatingControl href "/Models/Profiles/Equipment/ConcreteClasses/RegulatingControl/"
    style RegulatingControl fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl <|-- TapChangerControl : inherits

        TapChangerControl
            click TapChangerControl href "/Models/Profiles/Equipment/ConcreteClasses/TapChangerControl/"
            style TapChangerControl fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- RegulatingControl : inherits
            click PowerSystemResource href "/Models/Profiles/Equipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl --> Terminal : RegulatingControl.Terminal

        Terminal
            click Terminal href "/Models/Profiles/Equipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerSystemResource --> AssetInfo : PowerSystemResource.AssetDataSheet

        AssetInfo : Not defined in profile

        AssetInfo
            style AssetInfo fill:#A9A9A9,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingCondEq --> RegulatingControl : RegulatingCondEq.RegulatingControl

        RegulatingCondEq
            click RegulatingCondEq href "/Models/Profiles/Equipment/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl --> RegulatingControlModeKind : RegulatingControl.mode

        RegulatingControlModeKind
            click RegulatingControlModeKind href "/Models/Profiles/Equipment/Enumerations/RegulatingControlModeKind/"
            style RegulatingControlModeKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerSystemResource --> LocationMethodKind : PowerSystemResource.locationMethodKind

        LocationMethodKind
            click LocationMethodKind href "/Models/Profiles/Equipment/Enumerations/LocationMethodKind/"
            style LocationMethodKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl : RegulatingControl.mode
        RegulatingControl : RegulatingControl.Terminal
        PowerSystemResource : PowerSystemResource.locationMethodKind
        PowerSystemResource : PowerSystemResource.AssetDataSheet
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Equipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/Equipment/AbstractClasses/PowerSystemResource/)
        * **RegulatingControl**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mode | [cim:RegulatingControl.mode](https://cim.ucaiug.io/ns#RegulatingControl.mode) | 0..1 RegulatingControlModeKind | The regulating control mode presently available.  This specification allows for determining the kind of regulation without need for obtaining the units from a schedule. | direct |
| Terminal | [cim:RegulatingControl.Terminal](https://cim.ucaiug.io/ns#RegulatingControl.Terminal) | 0..1 Terminal | The terminal associated with this regulating control.  The terminal is associated instead of a node, since the terminal could connect into either a topological node or a connectivity node.  Sometimes it is useful to model regulation at a terminal of a bus bar object. | direct |
| locationMethodKind | [nc-no:PowerSystemResource.locationMethodKind](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethodKind) | 0..1 LocationMethodKind | Possible methods to derive geographical location. | PowerSystemResource |
| AssetDataSheet | [cim:PowerSystemResource.AssetDataSheet](https://cim.ucaiug.io/ns#PowerSystemResource.AssetDataSheet) | 0..1 AssetInfo | Datasheet information for this power system resource. | PowerSystemResource |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/Equipment/1.0](https://ap-no.cim4.eu/Equipment/1.0)
