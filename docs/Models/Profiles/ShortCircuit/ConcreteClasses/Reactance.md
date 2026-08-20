# Reactance

_Reactance (imaginary part of impedance), at rated frequency._

**URI**: [cim:Reactance](http://iec.ch/TC57/CIM100#Reactance)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Reactance
    click Reactance href "/Models/Profiles/ShortCircuit/ConcreteClasses/Reactance/"
    style Reactance fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Reactance : ACLineSegment.x0

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Reactance : EnergySource.x

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Reactance : EnergySource.x0

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Reactance : EnergySource.xn

        EnergySource
            click EnergySource href "/Models/Profiles/ShortCircuit/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.negativeX12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.negativeX21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.positiveX12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.positiveX21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.zeroX12

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentBranch --> Reactance : EquivalentBranch.zeroX21

        EquivalentBranch
            click EquivalentBranch href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentBranch/"
            style EquivalentBranch fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Reactance : EquivalentInjection.x

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Reactance : EquivalentInjection.x0

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> Reactance : EquivalentInjection.x2

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/ShortCircuit/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GroundingImpedance --> Reactance : GroundingImpedance.x

        GroundingImpedance
            click GroundingImpedance href "/Models/Profiles/ShortCircuit/ConcreteClasses/GroundingImpedance/"
            style GroundingImpedance fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MutualCoupling --> Reactance : MutualCoupling.x0

        MutualCoupling
            click MutualCoupling href "/Models/Profiles/ShortCircuit/ConcreteClasses/MutualCoupling/"
            style MutualCoupling fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PetersenCoil --> Reactance : PetersenCoil.xGroundMax

        PetersenCoil
            click PetersenCoil href "/Models/Profiles/ShortCircuit/ConcreteClasses/PetersenCoil/"
            style PetersenCoil fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PetersenCoil --> Reactance : PetersenCoil.xGroundMin

        PetersenCoil
            click PetersenCoil href "/Models/Profiles/ShortCircuit/ConcreteClasses/PetersenCoil/"
            style PetersenCoil fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PetersenCoil --> Reactance : PetersenCoil.xGroundNominal

        PetersenCoil
            click PetersenCoil href "/Models/Profiles/ShortCircuit/ConcreteClasses/PetersenCoil/"
            style PetersenCoil fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Reactance : PowerTransformerEnd.x0

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SeriesCompensator --> Reactance : SeriesCompensator.x0

        SeriesCompensator
            click SeriesCompensator href "/Models/Profiles/ShortCircuit/ConcreteClasses/SeriesCompensator/"
            style SeriesCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Reactance : SynchronousMachine.earthingStarPointX

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Reactance : SynchronousMachine.x0

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> Reactance : SynchronousMachine.x2

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/ShortCircuit/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TransformerEnd --> Reactance : TransformerEnd.xground

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/TransformerEnd/"
            style TransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Reactance --> UnitSymbol : Reactance.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Reactance --> UnitMultiplier : Reactance.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Reactance : Reactance.value
        Reactance : Reactance.unit
        Reactance : Reactance.multiplier
```

## Inheritance
* **Reactance**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Reactance.value](http://iec.ch/TC57/CIM100#Reactance.value) | No cardinality available float | No description available | direct |
| unit | [cim:Reactance.unit](http://iec.ch/TC57/CIM100#Reactance.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Reactance.multiplier](http://iec.ch/TC57/CIM100#Reactance.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
