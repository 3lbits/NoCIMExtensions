# ConductingEquipment

_The parts of the AC power system that are designed to carry current or that are conductively connected through terminals._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConductingEquipment](http://iec.ch/TC57/CIM100#ConductingEquipment)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class ConductingEquipment
    click ConductingEquipment href "/Models/Profiles/StateVariables/AbstractClasses/ConductingEquipment/"
    style ConductingEquipment fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- ACDCConverter : inherits

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/AbstractClasses/ACDCConverter/"
            style ACDCConverter fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- Switch : inherits

        Switch
            click Switch href "/Models/Profiles/StateVariables/ConcreteClasses/Switch/"
            style Switch fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment --> SvStatus : ConductingEquipment.SvStatus

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvStatus --> ConductingEquipment : SvStatus.ConductingEquipment

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        ConductingEquipment : ConductingEquipment.SvStatus
```

## Inheritance
* **ConductingEquipment**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SvStatus | [cim:ConductingEquipment.SvStatus](http://iec.ch/TC57/CIM100#ConductingEquipment.SvStatus) | No cardinality available SvStatus | The status state variable associated with this conducting equipment. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
