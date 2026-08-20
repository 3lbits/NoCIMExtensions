# Temperature

_Value of temperature in degrees Celsius._

**URI**: [cim:Temperature](http://iec.ch/TC57/CIM100#Temperature)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Temperature
    click Temperature href "/Models/Profiles/ShortCircuit/ConcreteClasses/Temperature/"
    style Temperature fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACLineSegment --> Temperature : ACLineSegment.shortCircuitEndTemperature

        ACLineSegment
            click ACLineSegment href "/Models/Profiles/ShortCircuit/ConcreteClasses/ACLineSegment/"
            style ACLineSegment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Temperature --> UnitMultiplier : Temperature.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/ShortCircuit/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Temperature --> UnitSymbol : Temperature.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/ShortCircuit/Enumerations/UnitSymbol/"
            style UnitSymbol fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Temperature : Temperature.multiplier
        Temperature : Temperature.unit
        Temperature : Temperature.value
```

## Inheritance
* **Temperature**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| multiplier | [cim:Temperature.multiplier](http://iec.ch/TC57/CIM100#Temperature.multiplier) | No cardinality available UnitMultiplier | No description available | direct |
| unit | [cim:Temperature.unit](http://iec.ch/TC57/CIM100#Temperature.unit) | No cardinality available UnitSymbol | No description available | direct |
| value | [cim:Temperature.value](http://iec.ch/TC57/CIM100#Temperature.value) | No cardinality available float | No description available | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
