# Length

_Unit of length. It shall be a positive value or zero._

**URI**: [cim:Length](http://iec.ch/TC57/CIM100#Length)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Length
    click Length href "/Models/Profiles/CoreEquipment/ConcreteClasses/Length/"
    style Length fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        Clamp --> Length : Clamp.lengthFromTerminal1

        Clamp
            click Clamp href "/Models/Profiles/CoreEquipment/ConcreteClasses/Clamp/"
            style Clamp fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Conductor --> Length : Conductor.length

        Conductor
            click Conductor href "/Models/Profiles/CoreEquipment/ConcreteClasses/Conductor/"
            style Conductor fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Cut --> Length : Cut.lengthFromTerminal1

        Cut
            click Cut href "/Models/Profiles/CoreEquipment/ConcreteClasses/Cut/"
            style Cut fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCLineSegment --> Length : DCLineSegment.length

        DCLineSegment
            click DCLineSegment href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLineSegment/"
            style DCLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroGeneratingUnit --> Length : HydroGeneratingUnit.dropHeight

        HydroGeneratingUnit
            click HydroGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroGeneratingUnit/"
            style HydroGeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Length --> UnitSymbol : Length.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/CoreEquipment/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Length --> UnitMultiplier : Length.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/CoreEquipment/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Length : Length.value
        Length : Length.unit
        Length : Length.multiplier
```

## Inheritance
* **Length**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:Length.value](http://iec.ch/TC57/CIM100#Length.value) | No cardinality available float | No description available | direct |
| unit | [cim:Length.unit](http://iec.ch/TC57/CIM100#Length.unit) | No cardinality available UnitSymbol | No description available | direct |
| multiplier | [cim:Length.multiplier](http://iec.ch/TC57/CIM100#Length.multiplier) | No cardinality available UnitMultiplier | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
