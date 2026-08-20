# ActivePower

_Product of RMS value of the voltage and the RMS value of the in-phase component of the current._

**URI**: [cim:ActivePower](http://iec.ch/TC57/CIM100#ActivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePower
    click ActivePower href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ActivePower/"
    style ActivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> ActivePower : ACDCConverter.p

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> ActivePower : ACDCConverter.targetPpcc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerLimit --> ActivePower : ActivePowerLimit.value

        ActivePowerLimit
            click ActivePowerLimit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ActivePowerLimit/"
            style ActivePowerLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea --> ActivePower : ControlArea.netInterchange

        ControlArea
            click ControlArea href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ControlArea/"
            style ControlArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea --> ActivePower : ControlArea.pTolerance

        ControlArea
            click ControlArea href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ControlArea/"
            style ControlArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergyConsumer --> ActivePower : EnergyConsumer.p

        EnergyConsumer
            click EnergyConsumer href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> ActivePower : EnergySource.activePower

        EnergySource
            click EnergySource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> ActivePower : EquivalentInjection.p

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ExternalNetworkInjection --> ActivePower : ExternalNetworkInjection.p

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsConnection --> ActivePower : PowerElectronicsConnection.p

        PowerElectronicsConnection
            click PowerElectronicsConnection href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerElectronicsConnection/"
            style PowerElectronicsConnection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> ActivePower : RotatingMachine.p

        RotatingMachine
            click RotatingMachine href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/RotatingMachine/"
            style RotatingMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower --> UnitMultiplier : ActivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePower --> UnitSymbol : ActivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/SteadyStateHypothesis/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower : ActivePower.value
        ActivePower : ActivePower.multiplier
        ActivePower : ActivePower.unit
```

## Inheritance
* **ActivePower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:ActivePower.value](http://iec.ch/TC57/CIM100#ActivePower.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:ActivePower.multiplier](http://iec.ch/TC57/CIM100#ActivePower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:ActivePower.unit](http://iec.ch/TC57/CIM100#ActivePower.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
