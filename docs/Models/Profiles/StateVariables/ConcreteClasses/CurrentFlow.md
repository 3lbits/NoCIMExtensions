# CurrentFlow

_Electrical current with sign convention: positive flow is out of the conducting equipment into the connectivity node. Can be both AC and DC._

**URI**: [cim:CurrentFlow](http://iec.ch/TC57/CIM100#CurrentFlow)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class CurrentFlow
    click CurrentFlow href "/Models/Profiles/StateVariables/ConcreteClasses/CurrentFlow/"
    style CurrentFlow fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> CurrentFlow : ACDCConverter.idc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurrentFlow --> UnitMultiplier : CurrentFlow.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/StateVariables/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        CurrentFlow --> UnitSymbol : CurrentFlow.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/StateVariables/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        CurrentFlow : CurrentFlow.value
        CurrentFlow : CurrentFlow.multiplier
        CurrentFlow : CurrentFlow.unit
```

## Inheritance
* **CurrentFlow**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| value | [cim:CurrentFlow.value](http://iec.ch/TC57/CIM100#CurrentFlow.value) | No cardinality available float | No description available | direct |
| multiplier | [cim:CurrentFlow.multiplier](http://iec.ch/TC57/CIM100#CurrentFlow.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:CurrentFlow.unit](http://iec.ch/TC57/CIM100#CurrentFlow.unit) | No cardinality available UnitSymbol | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
