# Voltage

_Electrical voltage, can be both AC and DC._

**URI**: [cim:Voltage](http://iec.ch/TC57/CIM100#Voltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Voltage
    click Voltage href "/Models/Profiles/ShortCircuit/ConcreteClasses/Voltage/"
    style Voltage fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PetersenCoil --> Voltage : PetersenCoil.nominalU

        PetersenCoil
            click PetersenCoil href "/Models/Profiles/ShortCircuit/ConcreteClasses/PetersenCoil/"
            style PetersenCoil fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformer --> Voltage : PowerTransformer.beforeShCircuitHighestOperatingVoltage

        PowerTransformer
            click PowerTransformer href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformer/"
            style PowerTransformer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformer --> Voltage : PowerTransformer.highSideMinOperatingU

        PowerTransformer
            click PowerTransformer href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformer/"
            style PowerTransformer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SeriesCompensator --> Voltage : SeriesCompensator.varistorVoltageThreshold

        SeriesCompensator
            click SeriesCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/SeriesCompensator/"
            style SeriesCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Voltage --> UnitMultiplier : Voltage.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Voltage --> UnitSymbol : Voltage.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Voltage : Voltage.value
        Voltage : Voltage.multiplier
        Voltage : Voltage.unit
```

## Inheritance
* **Voltage**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Voltage.value](http://iec.ch/TC57/CIM100#Voltage.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:Voltage.multiplier](http://iec.ch/TC57/CIM100#Voltage.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:Voltage.unit](http://iec.ch/TC57/CIM100#Voltage.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
