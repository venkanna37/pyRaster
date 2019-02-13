from osgeo import gdal
import sys
import numpy as np
import math

# Reading raster(tif) file
image = gdal.Open('./output/dark_object_subtraction.tif')
if image is None:
    print 'Unble to open the source file'
    sys.exit()

# First of all, gather some information from the origin file
[cols, rows] = np.array(image.GetRasterBand(1).ReadAsArray()).shape
trans = image.GetGeoTransform()
proj = image.GetProjection()
outfile = './output/sun_angle_correction.tif'
outdriver = gdal.GetDriverByName('GTiff')

# Create the file, using information from gthe original file
outdata = outdriver.Create(str(outfile), rows, cols, 4, gdal.GDT_Float32)

# Sunangle correction of each band and stacking those all bands
sun_angle = 64.16
for band in range(image.RasterCount):
    band += 1
    bandarray = np.array(image.GetRasterBand(band).ReadAsArray())
    bandarray1 = bandarray/math.sin(64.16)

    # Write the array to the image
    outdata.GetRasterBand(band).WriteArray(bandarray1)

    # Georeferencing the image
    outdata.SetGeoTransform(trans)

    # Write projection information
    outdata.SetProjection(proj)