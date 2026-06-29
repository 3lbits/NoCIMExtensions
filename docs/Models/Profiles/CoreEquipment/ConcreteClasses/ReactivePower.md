# ReactivePower

_Product of RMS value of the voltage and the RMS value of the quadrature component of the current._

**URI**: [cim:ReactivePower](http://iec.ch/TC57/CIM100#ReactivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ReactivePower
    click ReactivePower href "/Models/Profiles/CoreEquipment/ConcreteClasses/ReactivePower/"
    style ReactivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EnergyConsumer --> ReactivePower : EnergyConsumer.qfixed

        EnergyConsumer
            click EnergyConsumer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> ReactivePower : EquivalentInjection.maxQ

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> ReactivePower : EquivalentInjection.minQ

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ExternalNetworkInjection --> ReactivePower : ExternalNetworkInjection.maxQ

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ExternalNetworkInjection --> ReactivePower : ExternalNetworkInjection.minQ

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsConnection --> ReactivePower : PowerElectronicsConnection.maxQ

        PowerElectronicsConnection
            click PowerElectronicsConnection href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsConnection/"
            style PowerElectronicsConnection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsConnection --> ReactivePower : PowerElectronicsConnection.minQ

        PowerElectronicsConnection
            click PowerElectronicsConnection href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsConnection/"
            style PowerElectronicsConnection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> ReactivePower : SynchronousMachine.maxQ

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SynchronousMachine --> ReactivePower : SynchronousMachine.minQ

        SynchronousMachine
            click SynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/SynchronousMachine/"
            style SynchronousMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ReactivePower --> UnitSymbol : ReactivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ReactivePower --> UnitMultiplier : ReactivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ReactivePower : ReactivePower.value
        ReactivePower : ReactivePower.unit
        ReactivePower : ReactivePower.multiplier
```

## Inheritance
* **ReactivePower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:ReactivePower.value](http://iec.ch/TC57/CIM100#ReactivePower.value) | No cardinality available float | No description available | direct |
| unit | [cim:ReactivePower.unit](http://iec.ch/TC57/CIM100#ReactivePower.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:ReactivePower.multiplier](http://iec.ch/TC57/CIM100#ReactivePower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
