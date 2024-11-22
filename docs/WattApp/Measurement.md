# Measurement

_A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.
The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leaves, e.g. Substation-VoltageLevel-Bay-Switch-Measurement.
Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (VT) or potential transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.
If both a Terminal and PSR are associated, and the PSR is of type ConductingEquipment, the associated Terminal should belong to that ConductingEquipment instance.
When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:Measurement](https://cim.ucaiug.io/ns#Measurement)<br />
**Type**: Class

```mermaid
classDiagram
    class Measurement
    click Measurement href "/WattApp/Measurement/"
    style Measurement fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        Measurement <|-- Analog : inherits
            click Measurement href "/WattApp/Measurement/"
            style Measurement rx:10,ry:10

        Analog
            click Analog href "/WattApp/Analog/"
            style Analog rx:10,ry:10

        IdentifiedObject <|-- Measurement : inherits
            click IdentifiedObject href "/WattApp/IdentifiedObject/"
            style IdentifiedObject rx:10,ry:10

        Measurement --> ACDCTerminal : Measurement.ACDCTerminal

        ACDCTerminal
            click ACDCTerminal href "/WattApp/ACDCTerminal/"
            style ACDCTerminal fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        Measurement --> PhaseCode : Measurement.phases

        PhaseCode
            click PhaseCode href "/WattApp/PhaseCode/"
            style PhaseCode fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        Measurement --> UnitMultiplier : Measurement.unitMultiplier

        UnitMultiplier
            click UnitMultiplier href "/WattApp/UnitMultiplier/"
            style UnitMultiplier fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10
        Measurement --> UnitSymbol : Measurement.unitSymbol

        UnitSymbol
            click UnitSymbol href "/WattApp/UnitSymbol/"
            style UnitSymbol fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        Measurement : Measurement.ACDCTerminal
        Measurement : Measurement.measurementType
        Measurement : Measurement.phases
        Measurement : Measurement.unitMultiplier
        Measurement : Measurement.unitSymbol
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](IdentifiedObject.md)
    * **Measurement**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| ACDCTerminal | [cim:Measurement.ACDCTerminal](https://cim.ucaiug.io/ns#Measurement.ACDCTerminal) | 0..1 ACDCTerminal | One or more measurements may be associated with a terminal in the network. | direct |
| measurementType | [cim:Measurement.measurementType](https://cim.ucaiug.io/ns#Measurement.measurementType) | 0..1 String | Specifies the type of measurement. For example, this specifies if the measurement represents an indoor temperature, outdoor temperature, bus voltage, line flow, etc.
When the measurementType is set to "Specialization", the type of Measurement is defined in more detail by the specialized class which inherits from Measurement. | direct |
| phases | [cim:Measurement.phases](https://cim.ucaiug.io/ns#Measurement.phases) | 0..1 PhaseCode | Indicates to which phases the measurement applies and avoids the need to use 'measurementType' to also encode phase information (which would explode the types). The phase information in Measurement, along with 'measurementType' and 'phases' uniquely defines a Measurement for a device, based on normal network phase. Their meaning will not change when the computed energizing phasing is changed due to jumpers or other reasons.
If the attribute is missing three phases (ABC) shall be assumed. | direct |
| unitMultiplier | [cim:Measurement.unitMultiplier](https://cim.ucaiug.io/ns#Measurement.unitMultiplier) | 0..1 UnitMultiplier | The unit multiplier of the measured quantity. | direct |
| unitSymbol | [cim:Measurement.unitSymbol](https://cim.ucaiug.io/ns#Measurement.unitSymbol) | 0..1 UnitSymbol | The unit of measure of the measured quantity. | direct |
| mRID | [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| description | [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description) | 0..1 [LanguageObject](LanguageObject.md) or string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name) | 0..1 string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
