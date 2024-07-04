Flowchart:-

Create a csv file for required state consisting of district name, coordinates.

Inventory folder:
Consists of IMD, US-NOAA codes.

Inventory>IMD:

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th training
5th testing

IMD extraction code:
Run files IMD_rain, IMD_tmax, IMD_tmin for imd data extraction. Give year range acccordingly as per requirement. In my case I have IMD for 1960-2023 of 43 districts of rajasthan.

IMD conversion code:
The drought indices are calculated month-wise but IMD data are in daily basis. So run files IMD_rain, IMD_temp to convert into monthly basis. Then run file IMD_combine to combine all parameter into a single csv file.

IMD drought indices code:
3 types of drought indices are considered SPI, SPEI, RDI. Run the files IMD_SPI, IMD_SPEI, IMD_RDI. For SPI, SPEI considered 6 months interval and 12 months interval of RDI. NOTE: 1, 3, 6, 12, 24 months interval taken for SPI, SPEI but for RDI year wise interval taken.

IMD training code:

IMD testing code:

Follow the same procedure for NOAA.

Potential future>CMIP:

Order of code execution:
1st extraction
2nd conversion
3rd drought indices
4th testing

Extracting CMIP6 data:
Download data from zenodo link and extract the data. The data for india is about 120GB+. We have used the BCC-CSM2-MR data from the total data. To use the extractor you need location name to name the final file lat and lon coordinates for crosscheck and the column number coordinating to the coordinates in each file for each SSP scenario.Then add these to a coordinates.csv and run the file.
