# ApparentPower

_Product of the RMS value of the voltage and the RMS value of the current._

**URI**: [cim:ApparentPower](http://iec.ch/TC57/CIM100#ApparentPower)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ApparentPower
    click ApparentPower href "/Models/Profiles/CoreEquipment/ConcreteClasses/ApparentPower/"
    style ApparentPower fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> ApparentPower : ACDCConverter.baseS

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ApparentPowerLimit --> ApparentPower : ApparentPowerLimit.normalValue

        ApparentPowerLimit
            click ApparentPowerLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ApparentPowerLimit/"
            style ApparentPowerLimit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerElectronicsConnection --> ApparentPower : PowerElectronicsConnection.ratedS

        PowerElectronicsConnection
            click PowerElectronicsConnection href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerElectronicsConnection/"
            style PowerElectronicsConnection fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerTransformerEnd --> ApparentPower : PowerTransformerEnd.ratedS

        PowerTransformerEnd
            click PowerTransformerEnd href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerTransformerEnd/"
            style PowerTransformerEnd fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> ApparentPower : RotatingMachine.ratedS

        RotatingMachine
            click RotatingMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/RotatingMachine/"
            style RotatingMachine fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ApparentPower --> UnitMultiplier : ApparentPower.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ApparentPower --> UnitSymbol : ApparentPower.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ApparentPower : ApparentPower.value
        ApparentPower : ApparentPower.multiplier
        ApparentPower : ApparentPower.unit
```

## Inheritance
* **ApparentPower**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:ApparentPower.value](http://iec.ch/TC57/CIM100#ApparentPower.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:ApparentPower.multiplier](http://iec.ch/TC57/CIM100#ApparentPower.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:ApparentPower.unit](http://iec.ch/TC57/CIM100#ApparentPower.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
