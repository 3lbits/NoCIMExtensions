# Resistance

_Resistance (real part of impedance)._

**URI**: [cim:Resistance](http://iec.ch/TC57/CIM100#Resistance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Resistance
    click Resistance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Resistance/"
    style Resistance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Resistance : ACLineSegment.r0

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EarthFaultCompensator --> Resistance : EarthFaultCompensator.r

        EarthFaultCompensator
            click EarthFaultCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/EarthFaultCompensator/"
            style EarthFaultCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Resistance : EnergySource.r

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Resistance : EnergySource.r0

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Resistance : EnergySource.rn

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.negativeR12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.negativeR21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.positiveR12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.positiveR21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.zeroR12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Resistance : EquivalentBranch.zeroR21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Resistance : EquivalentInjection.r

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Resistance : EquivalentInjection.r0

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Resistance : EquivalentInjection.r2

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MutualCoupling --> Resistance : MutualCoupling.r0

        MutualCoupling
            click MutualCoupling href "/Models/Profiles/ShortCircuit/ConcreteClasses/MutualCoupling/"
            style MutualCoupling fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Resistance : PowerTransformerEnd.r0

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SeriesCompensator --> Resistance : SeriesCompensator.r0

        SeriesCompensator
            click SeriesCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/SeriesCompensator/"
            style SeriesCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Resistance : SynchronousMachine.earthingStarPointR

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Resistance : SynchronousMachine.r0

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Resistance : SynchronousMachine.r2

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Resistance : SynchronousMachine.r

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TransformerEnd --> Resistance : TransformerEnd.rground

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/TransformerEnd/"
            style TransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Resistance --> UnitSymbol : Resistance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Resistance --> UnitMultiplier : Resistance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Resistance : Resistance.value
        Resistance : Resistance.unit
        Resistance : Resistance.multiplier
```

## Inheritance
* **Resistance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Resistance.value](http://iec.ch/TC57/CIM100#Resistance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Resistance.unit](http://iec.ch/TC57/CIM100#Resistance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Resistance.multiplier](http://iec.ch/TC57/CIM100#Resistance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
