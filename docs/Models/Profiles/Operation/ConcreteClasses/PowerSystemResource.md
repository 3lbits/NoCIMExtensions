# PowerSystemResource

_A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated._

**URI**: [cim:PowerSystemResource](http://iec.ch/TC57/CIM100#PowerSystemResource)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PowerSystemResource
    click PowerSystemResource href "/Models/Profiles/Operation/ConcreteClasses/PowerSystemResource/"
    style PowerSystemResource fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource --> Control : PowerSystemResource.Controls

        Control
            click Control href "/Models/Profiles/Operation/ConcreteClasses/Control/"
            style Control fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        PowerSystemResource --> Measurement : PowerSystemResource.Measurements

        Measurement
            click Measurement href "/Models/Profiles/Operation/ConcreteClasses/Measurement/"
            style Measurement fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Control --> PowerSystemResource : Control.PowerSystemResource

        Control
            click Control href "/Models/Profiles/Operation/ConcreteClasses/Control/"
            style Control fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Measurement --> PowerSystemResource : Measurement.PowerSystemResource

        Measurement
            click Measurement href "/Models/Profiles/Operation/ConcreteClasses/Measurement/"
            style Measurement fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        PowerSystemResource : PowerSystemResource.Controls
        PowerSystemResource : PowerSystemResource.Measurements
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Operation/ConcreteClasses/IdentifiedObject/)
    * **PowerSystemResource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Controls | [cim:PowerSystemResource.Controls](http://iec.ch/TC57/CIM100#PowerSystemResource.Controls) | No cardinality available Control | The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator. | direct |
| Measurements | [cim:PowerSystemResource.Measurements](http://iec.ch/TC57/CIM100#PowerSystemResource.Measurements) | No cardinality available Measurement | The measurements associated with this power system resource. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile](http://iec.ch/TC57/ns/CIM/Operation-EUPackage_OperationProfile)
