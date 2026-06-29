# VsConverter

_DC side of the voltage source converter (VSC)._

**URI**: [cim:VsConverter](http://iec.ch/TC57/CIM100#VsConverter)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class VsConverter
    click VsConverter href "/Models/Profiles/StateVariables/ConcreteClasses/VsConverter/"
    style VsConverter fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCConverter <|-- VsConverter : inherits
            click ACDCConverter href "/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/"
            style ACDCConverter fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- ACDCConverter : inherits
            click ConductingEquipment href "/Models/Profiles/StateVariables/ConcreteClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        VsConverter --> AngleDegrees : VsConverter.delta

        AngleDegrees
            click AngleDegrees href "/Models/Profiles/StateVariables/ConcreteClasses/AngleDegrees/"
            style AngleDegrees fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        VsConverter --> Voltage : VsConverter.uv

        Voltage
            click Voltage href "/Models/Profiles/StateVariables/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCConverter --> CurrentFlow : ACDCConverter.idc

        CurrentFlow
            click CurrentFlow href "/Models/Profiles/StateVariables/ConcreteClasses/CurrentFlow/"
            style CurrentFlow fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCConverter --> ActivePower : ACDCConverter.poleLossP

        ActivePower
            click ActivePower href "/Models/Profiles/StateVariables/ConcreteClasses/ActivePower/"
            style ActivePower fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCConverter --> Voltage : ACDCConverter.uc

        Voltage
            click Voltage href "/Models/Profiles/StateVariables/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ACDCConverter --> Voltage : ACDCConverter.udc

        Voltage
            click Voltage href "/Models/Profiles/StateVariables/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConductingEquipment --> SvStatus : ConductingEquipment.SvStatus

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SvStatus --> ConductingEquipment : SvStatus.ConductingEquipment

        SvStatus
            click SvStatus href "/Models/Profiles/StateVariables/ConcreteClasses/SvStatus/"
            style SvStatus fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        VsConverter : VsConverter.delta
        VsConverter : VsConverter.uv
        ACDCConverter : ACDCConverter.idc
        ACDCConverter : ACDCConverter.poleLossP
        ACDCConverter : ACDCConverter.uc
        ACDCConverter : ACDCConverter.udc
        ConductingEquipment : ConductingEquipment.SvStatus
```

## Inheritance
* [ConductingEquipment](/Models/Profiles/StateVariables/ConcreteClasses/ConductingEquipment/)
    * [ACDCConverter](/Models/Profiles/StateVariables/ConcreteClasses/ACDCConverter/)
        * **VsConverter**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| delta | [cim:VsConverter.delta](http://iec.ch/TC57/CIM100#VsConverter.delta) | No cardinality available AngleDegrees | Angle between VsConverter.uv and ACDCConverter.uc. It is converter’s state variable used in power flow. The attribute shall be a positive value or zero. | direct |
| uv | [cim:VsConverter.uv](http://iec.ch/TC57/CIM100#VsConverter.uv) | No cardinality available Voltage | Line-to-line voltage on the valve side of the converter transformer. It is converter’s state variable, result from power flow. The attribute shall be a positive value. | direct |
| idc | [cim:ACDCConverter.idc](http://iec.ch/TC57/CIM100#ACDCConverter.idc) | No cardinality available CurrentFlow | Converter DC current, also called Id. It is converter’s state variable, result from power flow. | ACDCConverter |
| poleLossP | [cim:ACDCConverter.poleLossP](http://iec.ch/TC57/CIM100#ACDCConverter.poleLossP) | No cardinality available ActivePower | The active power loss at a DC Pole 
= idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2.
For lossless operation Pdc=Pac.
For rectifier operation with losses Pdc=Pac-lossP.
For inverter operation with losses Pdc=Pac+lossP.
It is converter’s state variable used in power flow. The attribute shall be a positive value. | ACDCConverter |
| uc | [cim:ACDCConverter.uc](http://iec.ch/TC57/CIM100#ACDCConverter.uc) | No cardinality available Voltage | Line-to-line converter voltage, the voltage at the AC side of the valve. It is converter’s state variable, result from power flow. The attribute shall be a positive value. | ACDCConverter |
| udc | [cim:ACDCConverter.udc](http://iec.ch/TC57/CIM100#ACDCConverter.udc) | No cardinality available Voltage | Converter voltage at the DC side, also called Ud. It is converter’s state variable, result from power flow. The attribute shall be a positive value. | ACDCConverter |
| SvStatus | [cim:ConductingEquipment.SvStatus](http://iec.ch/TC57/CIM100#ConductingEquipment.SvStatus) | No cardinality available SvStatus | The status state variable associated with this conducting equipment. | ConductingEquipment |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
