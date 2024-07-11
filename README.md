Flowchart:-

Create a CSV file for the required state consisting of the district name and coordinates stored in the initials folder.

Inventory dataset:
IMD, US NOAA.

Datasets>Inventory>IMD>IMD preprocessed>IMD extraction, IMD conversion, IMD drought indices.
Datasets>Inventory>IMD>IMD preprocessed training testing>IMD ML & DL models.

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th training & testing

IMD extraction code:
Run files IMD_rain, IMD_tmax, and IMD_tmin for IMD data extraction. Give year range accordingly as per requirement. I have IMD for 1901-2023 of 43 districts of Rajasthan.

IMD conversion code:
The drought indices are calculated month-wise, but IMD data are daily. So run files IMD_rain and IMD_temp to convert monthly. Then, run the file IMD_combine to combine all parameters into a single CSV file.

IMD drought indices code:
3 types of drought indices are considered: SPI, SPEI, and RDI. Follow the IMD_SPI, IMD_SPEI, IMD_RDI files to calculate drought indices. For SPI, SPEI considered 6-month intervals and RDI of 12-month intervals.

IMD training & testing code:

Follow the same procedure for NOAA.
Note: For US NOAA datasets, I directly downloaded them from https://www.ncdc.noaa.gov/cdo-web/search.

Potential future dataset:
CMIP6.

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th testing

CMIP6 extraction:
For CMIP6 datasets, I directly downloaded them from https://zendo.org/record/3873998.

CMIP6 conversion code:
Follow the same procedure of inventory.

CMIP6 drought indices code:
Follow the same procedure of inventory.

CMIP6 testing code:
