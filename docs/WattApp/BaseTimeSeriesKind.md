# BaseTimeSeriesKind

__

**URI**: http://entsoe.eu/ns/nc#BaseTimeSeriesKind

**Type**: Enumeration

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| forecast | [nc:BaseTimeSeriesKind.forecast](http://entsoe.eu/ns/nc#BaseTimeSeriesKind.forecast) | Time series is forecast data. The values represent the result of scientific predictions based on historical time stamped data. |
| hindcast | [nc:BaseTimeSeriesKind.hindcast](http://entsoe.eu/ns/nc#BaseTimeSeriesKind.hindcast) | Time series is hindcast data. The value represent probable past (historic) condition given by calculation done using actual values. For instance, determine the among of wind based on the energy produced by wind. However, hindcast is typical the result of a simulated forecasts for historical periods. |
| schedule | [nc:BaseTimeSeriesKind.schedule](http://entsoe.eu/ns/nc#BaseTimeSeriesKind.schedule) | Time series is schedule data. The values represent the result of a committed and plan forecast data that has been through a quality control and could incur penalty when not followed. |
| actual | [nc:BaseTimeSeriesKind.actual](http://entsoe.eu/ns/nc#BaseTimeSeriesKind.actual) | Time series is actual data. The values represent measured or calculated values that represent the actual behaviour.  |
## Schema Source

from schema: [https://ap-no.cim4.eu/WattApp/1.0](https://ap-no.cim4.eu/WattApp/1.0)
