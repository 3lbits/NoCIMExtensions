# TapChanger

_Mechanism for changing transformer winding tap positions._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:TapChanger](http://iec.ch/TC57/CIM100#TapChanger)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class TapChanger
    click TapChanger href "/Models/Profiles/StateVariables/AbstractClasses/TapChanger/"
    style TapChanger fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        TapChanger --> SvTapStep : TapChanger.SvTapStep

        SvTapStep
            click SvTapStep href "/Models/Profiles/StateVariables/ConcreteClasses/SvTapStep/"
            style SvTapStep fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        SvTapStep --> TapChanger : SvTapStep.TapChanger

        SvTapStep
            click SvTapStep href "/Models/Profiles/StateVariables/ConcreteClasses/SvTapStep/"
            style SvTapStep fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        TapChanger : TapChanger.SvTapStep
```

## Inheritance
* **TapChanger**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SvTapStep | [cim:TapChanger.SvTapStep](http://iec.ch/TC57/CIM100#TapChanger.SvTapStep) | No cardinality available SvTapStep | The tap step state associated with the tap changer. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
