# VsCapabilityCurve

_The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and Qmax on Y1-axis and Y2-axis._

**URI**: [cim:VsCapabilityCurve](http://iec.ch/TC57/CIM100#VsCapabilityCurve)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class VsCapabilityCurve
    click VsCapabilityCurve href "/Models/Profiles/CoreEquipment/ConcreteClasses/VsCapabilityCurve/"
    style VsCapabilityCurve fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Curve <|-- VsCapabilityCurve : inherits
            click Curve href "/Models/Profiles/CoreEquipment/AbstractClasses/Curve/"
            style Curve fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- Curve : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VsCapabilityCurve --> VsConverter : VsCapabilityCurve.VsConverterDCSides

        VsConverter
            click VsConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/VsConverter/"
            style VsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Curve --> CurveData : Curve.CurveDatas

        CurveData
            click CurveData href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurveData/"
            style CurveData fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurveData --> Curve : CurveData.Curve

        CurveData
            click CurveData href "/Models/Profiles/CoreEquipment/ConcreteClasses/CurveData/"
            style CurveData fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VsConverter --> VsCapabilityCurve : VsConverter.CapabilityCurve

        VsConverter
            click VsConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/VsConverter/"
            style VsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

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

        VsCapabilityCurve : VsCapabilityCurve.VsConverterDCSides
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
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [Curve](/Models/Profiles/CoreEquipment/AbstractClasses/Curve/)
        * **VsCapabilityCurve**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| VsConverterDCSides | [cim:VsCapabilityCurve.VsConverterDCSides](http://iec.ch/TC57/CIM100#VsCapabilityCurve.VsConverterDCSides) | No cardinality available VsConverter | All converters with this capability curve. | direct |
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
