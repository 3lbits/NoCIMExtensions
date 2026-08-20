# ActivePower

_Product of RMS value of the voltage and the RMS value of the in-phase component of the current._

**URI**: [cim:ActivePower](http://iec.ch/TC57/CIM100#ActivePower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ActivePower
    click ActivePower href "/Models/Profiles/CoreEquipment/ConcreteClasses/ActivePower/"
    style ActivePower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> ActivePower : ACDCConverter.idleLoss

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> ActivePower : ACDCConverter.maxP

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> ActivePower : ACDCConverter.minP

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePowerLimit --> ActivePower : ActivePowerLimit.normalValue

        ActivePowerLimit
            click ActivePowerLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ActivePowerLimit/"
            style ActivePowerLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergyConsumer --> ActivePower : EnergyConsumer.pfixed

        EnergyConsumer
            click EnergyConsumer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConsumer/"
            style EnergyConsumer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> ActivePower : EnergySource.pMin

        EnergySource
            click EnergySource href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> ActivePower : EnergySource.pMax

        EnergySource
            click EnergySource href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> ActivePower : EquivalentInjection.maxP

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquivalentInjection --> ActivePower : EquivalentInjection.minP

        EquivalentInjection
            click EquivalentInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquivalentInjection/"
            style EquivalentInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ExternalNetworkInjection --> ActivePower : ExternalNetworkInjection.maxP

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ExternalNetworkInjection --> ActivePower : ExternalNetworkInjection.minP

        ExternalNetworkInjection
            click ExternalNetworkInjection href "/Models/Profiles/CoreEquipment/ConcreteClasses/ExternalNetworkInjection/"
            style ExternalNetworkInjection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.maximumAllowableSpinningReserve

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.maxOperatingP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.minOperatingP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.nominalP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.ratedGrossMaxP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.ratedGrossMinP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> ActivePower : GeneratingUnit.ratedNetMaxP

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsUnit --> ActivePower : PowerElectronicsUnit.maxP

        PowerElectronicsUnit
            click PowerElectronicsUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsUnit/"
            style PowerElectronicsUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsUnit --> ActivePower : PowerElectronicsUnit.minP

        PowerElectronicsUnit
            click PowerElectronicsUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsUnit/"
            style PowerElectronicsUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ActivePower --> UnitMultiplier : ActivePower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ActivePower --> UnitSymbol : ActivePower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
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
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
