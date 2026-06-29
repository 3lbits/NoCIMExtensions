# PerCent

_Percentage on a defined base.   For example, specify as 100 to indicate at the defined base._

**URI**: [cim:PerCent](http://iec.ch/TC57/CIM100#PerCent)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PerCent
    click PerCent href "/Models/Profiles/CoreEquipment/ConcreteClasses/PerCent/"
    style PerCent fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EnergyConsumer --> PerCent : EnergyConsumer.pfixedPct

        EnergyConsumer
            click EnergyConsumer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergyConsumer --> PerCent : EnergyConsumer.qfixedPct

        EnergyConsumer
            click EnergyConsumer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> PerCent : GeneratingUnit.governorSCD

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> PerCent : GeneratingUnit.totalEfficiency

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PhaseTapChangerNonLinear --> PerCent : PhaseTapChangerNonLinear.voltageStepIncrement

        PhaseTapChangerNonLinear
            click PhaseTapChangerNonLinear href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerNonLinear/"
            style PhaseTapChangerNonLinear fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RatioTapChanger --> PerCent : RatioTapChanger.stepVoltageIncrement

        RatioTapChanger
            click RatioTapChanger href "/Models/Profiles/CoreEquipment/ConcreteClasses/RatioTapChanger/"
            style RatioTapChanger fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> PerCent : SynchronousMachine.qPercent

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChangerTablePoint --> PerCent : TapChangerTablePoint.b

        TapChangerTablePoint
            click TapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerTablePoint/"
            style TapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChangerTablePoint --> PerCent : TapChangerTablePoint.g

        TapChangerTablePoint
            click TapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerTablePoint/"
            style TapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChangerTablePoint --> PerCent : TapChangerTablePoint.r

        TapChangerTablePoint
            click TapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerTablePoint/"
            style TapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChangerTablePoint --> PerCent : TapChangerTablePoint.x

        TapChangerTablePoint
            click TapChangerTablePoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChangerTablePoint/"
            style TapChangerTablePoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PerCent --> UnitSymbol : PerCent.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PerCent --> UnitMultiplier : PerCent.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PerCent : PerCent.value
        PerCent : PerCent.unit
        PerCent : PerCent.multiplier
```

## Inheritance
* **PerCent**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:PerCent.value](http://iec.ch/TC57/CIM100#PerCent.value) | No cardinality available float | Normally 0 to 100 on a defined base. | direct |
| unit | [cim:PerCent.unit](http://iec.ch/TC57/CIM100#PerCent.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:PerCent.multiplier](http://iec.ch/TC57/CIM100#PerCent.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
