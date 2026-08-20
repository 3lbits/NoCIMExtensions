# Voltage

_Electrical voltage, can be both AC and DC._

**URI**: [cim:Voltage](http://iec.ch/TC57/CIM100#Voltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Voltage
    click Voltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/Voltage/"
    style Voltage fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> Voltage : ACDCConverter.maxUdc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> Voltage : ACDCConverter.minUdc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> Voltage : ACDCConverter.ratedUdc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> Voltage : ACDCConverter.valveU0

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BaseVoltage --> Voltage : BaseVoltage.nominalVoltage

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCConductingEquipment --> Voltage : DCConductingEquipment.ratedUdc

        DCConductingEquipment
            click DCConductingEquipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCConductingEquipment/"
            style DCConductingEquipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EnergySource --> Voltage : EnergySource.nominalVoltage

        EnergySource
            click EnergySource href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergySource/"
            style EnergySource fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsConnection --> Voltage : PowerElectronicsConnection.ratedU

        PowerElectronicsConnection
            click PowerElectronicsConnection href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsConnection/"
            style PowerElectronicsConnection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> Voltage : PowerTransformerEnd.ratedU

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> Voltage : RotatingMachine.ratedU

        RotatingMachine
            click RotatingMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/RotatingMachine/"
            style RotatingMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ShuntCompensator --> Voltage : ShuntCompensator.nomU

        ShuntCompensator
            click ShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        StaticVarCompensator --> Voltage : StaticVarCompensator.voltageSetPoint

        StaticVarCompensator
            click StaticVarCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/StaticVarCompensator/"
            style StaticVarCompensator fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapChanger --> Voltage : TapChanger.neutralU

        TapChanger
            click TapChanger href "/Models/Profiles/CoreEquipment/ConcreteClasses/TapChanger/"
            style TapChanger fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltageLevel --> Voltage : VoltageLevel.highVoltageLimit

        VoltageLevel
            click VoltageLevel href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltageLevel/"
            style VoltageLevel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltageLevel --> Voltage : VoltageLevel.lowVoltageLimit

        VoltageLevel
            click VoltageLevel href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltageLevel/"
            style VoltageLevel fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VoltageLimit --> Voltage : VoltageLimit.normalValue

        VoltageLimit
            click VoltageLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltageLimit/"
            style VoltageLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Voltage --> UnitMultiplier : Voltage.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Voltage --> UnitSymbol : Voltage.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
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
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
