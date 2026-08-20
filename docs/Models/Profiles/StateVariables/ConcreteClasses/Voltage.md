# Voltage

_Electrical voltage, can be both AC and DC._

**URI**: [cim:Voltage](http://iec.ch/TC57/CIM100#Voltage)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class Voltage
    click Voltage href "/Models/Profiles/StateVariables/ConcreteClasses/Voltage/"
    style Voltage fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ACDCConverter --> Voltage : ACDCConverter.uc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ACDCConverter --> Voltage : ACDCConverter.udc

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvVoltage --> Voltage : SvVoltage.v

        SvVoltage
            click SvVoltage href "/Models/Profiles/StateVariables/ConcreteClasses/SvVoltage/"
            style SvVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VsConverter --> Voltage : VsConverter.uv

        VsConverter
            click VsConverter href "/Models/Profiles/StateVariables/ConcreteClasses/VsConverter/"
            style VsConverter fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Voltage --> UnitMultiplier : Voltage.multiplier

        UnitMultiplier
            click UnitMultiplier href "/Models/Profiles/StateVariables/Enumerations/UnitMultiplier/"
            style UnitMultiplier fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Voltage --> UnitSymbol : Voltage.unit

        UnitSymbol
            click UnitSymbol href "/Models/Profiles/StateVariables/Enumerations/UnitSymbol/"
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
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
