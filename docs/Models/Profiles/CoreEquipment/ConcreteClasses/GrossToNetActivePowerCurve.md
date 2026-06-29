# GrossToNetActivePowerCurve

_Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modelled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service._

**URI**: [cim:GrossToNetActivePowerCurve](http://iec.ch/TC57/CIM100#GrossToNetActivePowerCurve)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class GrossToNetActivePowerCurve
    click GrossToNetActivePowerCurve href "/Models/Profiles/CoreEquipment/ConcreteClasses/GrossToNetActivePowerCurve/"
    style GrossToNetActivePowerCurve fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Curve <|-- GrossToNetActivePowerCurve : inherits
            click Curve href "/Models/Profiles/CoreEquipment/ConcreteClasses/Curve/"
            style Curve fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Curve : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GrossToNetActivePowerCurve --> GeneratingUnit : GrossToNetActivePowerCurve.GeneratingUnit

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Curve --> CurveData : Curve.CurveDatas

        CurveData
            click CurveData href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurveData/"
            style CurveData fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurveData --> Curve : CurveData.Curve

        CurveData
            click CurveData href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurveData/"
            style CurveData fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> GrossToNetActivePowerCurve : GeneratingUnit.GrossToNetActivePowerCurves

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Curve --> CurveStyle : Curve.curveStyle

        CurveStyle
            click CurveStyle href "/Models/Profiles/CoreEquipment/Enumerations/CurveStyle/"
            style CurveStyle fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Curve --> UnitSymbol : Curve.xUnit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Curve --> UnitSymbol : Curve.y1Unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Curve --> UnitSymbol : Curve.y2Unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GrossToNetActivePowerCurve : GrossToNetActivePowerCurve.GeneratingUnit
        Curve : Curve.curveStyle
        Curve : Curve.xUnit
        Curve : Curve.y1Unit
        Curve : Curve.y2Unit
        Curve : Curve.CurveDatas
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * [Curve](/Models/Profiles/CoreEquipment/ConcreteClasses/Curve/)
        * **GrossToNetActivePowerCurve**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| GeneratingUnit | [cim:GrossToNetActivePowerCurve.GeneratingUnit](http://iec.ch/TC57/CIM100#GrossToNetActivePowerCurve.GeneratingUnit) | No cardinality available GeneratingUnit | A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit. | direct |
| curveStyle | [cim:Curve.curveStyle](http://iec.ch/TC57/CIM100#Curve.curveStyle) | No cardinality available CurveStyle | The style or shape of the curve. | Curve |
| xUnit | [cim:Curve.xUnit](http://iec.ch/TC57/CIM100#Curve.xUnit) | No cardinality available UnitSymbol | The X-axis units of measure. | Curve |
| y1Unit | [cim:Curve.y1Unit](http://iec.ch/TC57/CIM100#Curve.y1Unit) | No cardinality available UnitSymbol | The Y1-axis units of measure. | Curve |
| y2Unit | [cim:Curve.y2Unit](http://iec.ch/TC57/CIM100#Curve.y2Unit) | No cardinality available UnitSymbol | The Y2-axis units of measure. | Curve |
| CurveDatas | [cim:Curve.CurveDatas](http://iec.ch/TC57/CIM100#Curve.CurveDatas) | No cardinality available CurveData | The point data values that define this curve. | Curve |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
