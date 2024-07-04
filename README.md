Flowchart:-

Create a CSV file for the required state consisting of the district name and coordinates.

Inventory data:
IMD, US-NOAA.

IMD:

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th training
5th testing

IMD extraction code:
Run files IMD_rain, IMD_tmax, and IMD_tmin for IMD data extraction. Give year range accordingly as per requirement. I have IMD for 1901-2023 of 43 districts of Rajasthan.

IMD conversion code:
The drought indices are calculated month-wise, but IMD data are daily. So run files IMD_rain and IMD_temp to convert monthly. Then, run the file IMD_combine to combine all parameters into a single CSV file.

IMD drought indices code:
3 types of drought indices are considered: SPI, SPEI, and RDI. Run the files IMD_SPI, IMD_SPEI, IMD_RDI. For SPI, SPEI considered 6 months interval and 12 months interval of RDI.

IMD training code:

IMD testing code:

Follow the same procedure for NOAA.

Potential future data:
CMIP.

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th testing

Extracting CMIP6 data:
