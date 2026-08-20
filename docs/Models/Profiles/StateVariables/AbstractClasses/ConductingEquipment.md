# ConductingEquipment

_The parts of the AC power system that are designed to carry current or that are conductively connected through terminals._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:ConductingEquipment](http://iec.ch/TC57/CIM100#ConductingEquipment)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class ConductingEquipment
    click ConductingEquipment href "/Models/Profiles/StateVariables/AbstractClasses/ConductingEquipment/"
    style ConductingEquipment fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- ACDCConverter : inherits

        ACDCConverter
            click ACDCConverter href "/Models/Profiles/StateVariables/AbstractClasses/ACDCConverter/"
            style ACDCConverter fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment <|-- Switch : inherits

        Switch
            click Switch href "/Models/Profiles/StateVariables/ConcreteClasses/Switch/"
            style Switch fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        ConductingEquipment --> SvStatus : ConductingEquipment.SvStatus

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        SvStatus --> ConductingEquipment : SvStatus.ConductingEquipment

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


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
