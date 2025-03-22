# ERA5 and CFSR Extratropical Cyclone (ETC) Inventory

This project utilizes two primary datasets to study extratropical cyclones (ETCs) in the Great Lakes Basin region. These datasets are derived from the ERA5 reanalysis and NOAA's Climate Forecast System Reanalysis (CFSR). Both datasets have identical columns/variables.

## ERA5 Dataset
The following is a brief description of the data included in `era5_etc.csv`. An ETC detection algorithm (i.e., the Crawford algorithm) identified 6136 ETCs between January 1950 and December 2019 in ERA5 mean sea level pressure data. Each ETC takes up one row in `era5_etc.csv`. The columns in `era5_etc.csv` are variables associated with each ETC:

### Features
| Feature                          | Description                                                                                   | Units                     | Data Type    |
| -------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------- | ------------ |
| `track_id`                         | Unique storm identifier within a given month                                                  | N/A                       | integer      |
| `year`, `month`, `day`, `hour`           | ETC cyclolysis time                                                                           | N/A                       | integer      |
| `year_genesis`, `month_genesis`, `day_genesis`, `hour_genesis` | ETC cyclogenesis time                                                                   | N/A                       | integer      |
| `lat_gen`, `lon_gen`                 | Cyclogenesis latitude and longitude                                                           | degrees North, degrees East | float      |
| `gen_region`                       | Geographic region of the ETC formation: 1=Alberta, 2=Atlantic, 3=Colorado, 4=Great Lakes, 5=Gulf of Mexico | N/A | integer      |
| `year_of_GLR_0`, `month_of_GLR_0`, `day_of_GLR_0`, `hour_of_GLR_0` | Time when the ETC first enters the Great Lakes Region (GLR)                         | N/A                       | integer      |
| `min_p_cent`                      | Minimum central MSLP during the ETC’s lifespan                                                | hPa                       | float        |
| `max_p_grad`                       | Maximum pressure gradient during the ETC’s lifespan                                           | hPa                       | float        |
| `max_radius`                       | Maximum ETC radius during the ETC’s lifespan                                                  | km                        | float        |
| `max_uv`                           | Maximum ETC propagation speed during the ETC’s lifespan                                       | km/hr                     | float        |
| `sup_ttl_precip`, `mi_ttl_precip`, `hur_ttl_precip`, `erie_ttl_precip`, `ont_ttl_precip` | Sum of over-lake precipitation for each lake while the ETC is in the region | m precipitation   | float        |
| `sup_ttl_evap`, `mi_ttl_evap`, `hur_ttl_evap`, `erie_ttl_evap`, `ont_ttl_evap` | Over-lake evaporation for each lake                                           | m evaporation     | float        |
| `sup_ttl_run`, `mi_ttl_run`, `hur_ttl_run`, `erie_ttl_run`, `ont_ttl_run` | Runoff for each lake basin                                                         | m runoff          | float        |
| `sup_ttl_P_minus_E`, `mi_ttl_P_minus_E`, `hur_ttl_P_minus_E`, `erie_ttl_P_minus_E`, `ont_ttl_P_minus_E` | Over-lake P-E (precipitation minus evaporation) for each lake | m P-E per m²               | float        |
| `total_hours_in_GLR`               | Total time the ETC spends in the GLR                                                           | hours                     | integer      |
| `genesis_date_time`, `lysis_date_time`, `glr0_date_time` | Datetime format conversions of year, month, day, and hour information for cyclogenesis, cyclolysis, and GLR entrance | %y-%m-%d %h:%m:%s          | Python Object |
| `fraction_of_time_in_GLR`          | Fraction of the ETC's lifespan spent in the GLR                                                | unitless                  | float        |
| `maturity_glr0_minus_genesis_ratio` | Ratio of time to reach GLR after forming to the total lifespan of the ETC                   | unitless                  | float        |
| `north_south_gen_lat`              | ETC bins determined by whether the storm forms north (1) or south (-1) of 43°N                | unitless                  | integer      |
| `east_west_gen_lon`                | ETC bins determined by whether the storm forms east (1) or west (-1) of 96°W                  | unitless                  | integer      |
| `[teleconnection_name]_bin`        | Teleconnection phase and strength: -2 (Strong Negative), -1 (Weak Negative), 1 (Weak Positive), 2 (Strong Positive) | unitless                  | integer      |
| `[teleconnection_name]_value`      | Teleconnection index corresponding to ETC timing                                              | unitless                  | float        |


## CFSR Dataset
NOAA's Climate Forecast System (CFSR) dataset covers the period from 1979 to 2019, and contains the same columns and variables as the ERA5 dataset. It is the file `cfsr_etc.csv.` Although we expect the two datasets to give similar information about ETCs and their impacts, they are not identical. They come from two different estiamtes of the atmospheric state. The CFSR dataset will be primarily utilized for cross-validation of the clustering results obtained from the ERA5 dataset.

### Features
The features in the CFSR dataset are practically identical to those listed for the ERA5 dataset. Please refer to the ERA5 feature descriptions above for details.

### Teleconnections and their Acronyms
| Teleconnection Acronym | Teleconnection Name                    |
| --------------------- | -------------------------------------- |
| AMO                   | Atlantic Multidecadal Oscillation       |
| AO                    | Arctic Oscillation                      |
| EA/WR                 | East Atlantic/West Russia pattern       |
| ENSO                  | El Niño-Southern Oscillation            |
| EP/NP                 | East Pacific/North Pacific pattern      |
| IPO                   | Interdecadal Pacific Oscillation        |
| NAO                   | North Atlantic Oscillation              |
| PDO                   | Pacific Decadal Oscillation             |
| PNA                   | Pacific North American pattern          |
| POL                   | Polar/Eurasia pattern                   |
| TNH                   | Tropical/Northern Hemisphere pattern    |
| WP                    | West Pacific pattern                    |

### Great Lakes and Their Abbreviations
| Lake Name     | Abbreviation |
| --------------| ------------ |
| Lake Superior | sup          |
| Lake Michigan | mi           |
| Lake Huron    | hur          |
| Lake Erie     | erie         |
| Lake Ontario  | ont          |

### 💧 A Note About Volumetric Impacts (m³)

The precipitation and evaporation values in this dataset are given in **meters (m)** — not as raw precipitation totals, but as **equivalent depth** over the lake's surface. These values represent the **volume of water added or removed by a storm, divided by the lake's surface area**. In other words, they are **volume-per-area** quantities, expressed as a depth.

To recover the actual **volumetric impact** of a storm on a lake, we multiply these depth values by the lake's surface area (in m²), yielding a volume in cubic meters:

Depth (m) × Lake Area (m²) = Volume (m³)

This conversion is essential if we want to compare impacts across lakes of different sizes or compute total basin-wide effects. Without it, the same depth over Lake Superior and Lake Ontario would misleadingly imply equal impacts.






