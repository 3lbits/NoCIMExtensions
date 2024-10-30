# Asset Catalogue Vocabulary

**URI**: http://iec.ch/TC57/2007/profile#

**Name**: AssetCatalogue

## Classes

| Class | Description |
| --- | --- |
| [AssetInfo](AssetInfo.md) | Set of attributes of an asset, representing typical datasheet information of a physical device that can be instantiated and shared in different data exchange contexts:- as attributes of an asset instance (installed or in stock)- as attributes of an asset model (product by a manufacturer)- as attributes of a type asset (generic type of an asset as used in designs/extension planning). |
| [AssetSpecification](AssetSpecification.md) | Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc. |
| [BindingLayer](BindingLayer.md) | Layer applied with the sole purpose of binding different layers/cores of cable together. |
| [CableInfo](CableInfo.md) | Cable data. |
| [CableLayer](CableLayer.md) | No description available |
| [ConcentricWireLayer](ConcentricWireLayer.md) | Concentric wire layer base class. |
| [ConductingAssetInfo](ConductingAssetInfo.md) | Generic information for conducting asset |
| [ConductorInfo](ConductorInfo.md) | Common class for rigid and flexible conductors.[IEC 826-14-06]: Conductive part intended to carry a specified electric current |
| [ConductorScreenLayer](ConductorScreenLayer.md) | A screen covering the conductor. Also called Conductor Shield. |
| [CorrugatedRoundWire](CorrugatedRoundWire.md) | No description available |
| [FlatStraps](FlatStraps.md) | No description available |
| [GappedTape](GappedTape.md) | Tape shield cable data. |
| [IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing identification and naming attributes. |
| [InnerSheathLayer](InnerSheathLayer.md) | <b>Non-metallic</b> covering which surrounds the assembly of the cores (and fillers, if any) of a multiconductor cable and over which the protective covering is applied.For example, a bedding layer for an armour or reinforcement. |
| [InsulationLayer](InsulationLayer.md) | No description available |
| [InsulationScreenLayer](InsulationScreenLayer.md) | A screen covering the insulation. Also called Insulation Shield. |
| [LappedTape](LappedTape.md) | Tape shield cable data. |
| [LongitudinallyCorrugatedTape](LongitudinallyCorrugatedTape.md) | Tape shield cable data. |
| [Manufacturer](Manufacturer.md) | Organisation that manufactures asset products. |
| [MetallicSheathLayer](MetallicSheathLayer.md) | Any metallic sheath (or metal screen), including foils, braids, armours, concentric neutrals and tape shields. |
| [MultiCoreCableInfo](MultiCoreCableInfo.md) | No description available |
| [NonMetallicSheathLayer](NonMetallicSheathLayer.md) | Uniform and continuous tubular non-metallic sheath. This class allows for the representation of any sheaths not properly defined with it's children classes.For example, separation sheaths (inner sheath applied between two metallic coverings of different materials).Note: The term sheath is only used for metallic coverings in North America, whereas the term jacket is used for non-metallic coverings. |
| [OrganisationRole](OrganisationRole.md) | Identifies a way in which an organisation may participate in the utility enterprise (e.g., customer, manufacturer, etc). |
| [OverSheathLayer](OverSheathLayer.md) | <b>Non-metallic</b> covering applied over a covering, generally metallic, ensuring the protection of the cable from the outside, such as jackets and servings. |
| [PerLengthConductorParameter](PerLengthConductorParameter.md) | Common type for per-length electrical catalogues describing line parameters. |
| [PerLengthImpedance](PerLengthImpedance.md) | Common type for per-length impedance electrical catalogues. |
| [PerLengthPhaseImpedance](PerLengthPhaseImpedance.md) | Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form. |
| [PerLengthSequenceImpedance](PerLengthSequenceImpedance.md) | Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm. |
| [PhaseImpedanceData](PhaseImpedanceData.md) | Impedance and conductance matrix element values.The diagonal elements are described by the elements having the same toPhase and fromPhase value and the off diagonal elements have different toPhase and fromPhase values.  The matrix can also be stored in symmetric lower triangular format using the row and column attributes, which map to ACLineSegmentPhase.sequenceNumber. |
| [ProductAssetModel](ProductAssetModel.md) | Asset model by a specific manufacturer. |
| [ResistancePerLengthTemperaturePoint](ResistancePerLengthTemperaturePoint.md) | No description available |
| [RoundWire](RoundWire.md) | No description available |
| [ScreenLayer](ScreenLayer.md) | Electrical screen of non-metallic and/or metallic material. A semi conducting (as in somewhat conducting) material is typically used. |
| [SkidWireLayer](SkidWireLayer.md) | Layer with wires or assembly of wires, usually D-shaped, applied with a long length of lay over the cores of a pipe-type cable, to provide mechanical protection and to facilitate sliding while the cores are being pulled into the pipe.  Reference: IEC 60050-461 |
| [SplitConcentric](SplitConcentric.md) | Single concentric layer with two conductors separated by each other by insulating material. Reference: IEC 60050-461 |
| [SwellableWaterTapes](SwellableWaterTapes.md) | Swellable water tapes (SWTPs) to provide longitudinal and radial water blocking. It can be made of a semi-conducting or a non-conductive material (NCWST).Typically applied between the insulation screen and the shield layers and/or over the shield layer and/or over the shield layer.Note that the Shield and Armor layers may also have a water blocking purpose. In such cases MettalicSheath should be used instead. |
| [TapeLayer](TapeLayer.md) | Tape layer base class. |
| [TubularTape](TubularTape.md) | Tape shield cable data. |
| [WireBraidInfo](WireBraidInfo.md) | Metallic Wires or Braid sheath. |
| [WireInfo](WireInfo.md) | Wire data that can be specified per line segment phase, or for the line segment as a whole in case its phases all have the same wire characteristics. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CableShieldMaterialKind](CableShieldMaterialKind.md) | Kind of cable shield material. |
| [WireInsulationKind](WireInsulationKind.md) | Kind of wire insulation. |
| [WireMaterialKind](WireMaterialKind.md) | Kind of wire material. |
