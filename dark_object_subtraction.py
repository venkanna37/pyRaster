from osgeo import gdal
import sys
import numpy as np

# Reading raster(tif) file
image = gdal.Open('./output/bbox_clipping.tif')
if image is None:
    print 'Unable to open the source file'
    sys.exit()

# First of all, gather some information from the original file
[cols, rows] = np.array(image.GetRasterBand(1).ReadAsArray()).shape
trans = image.GetGeoTransform()
proj = image.GetProjection()
outfile = "./output/dark_object_subtraction.tif"
outdriver = gdal.GetDriverByName("GTiff")

# Create the file, using the information from the original file
outdata = outdriver.Create(str(outfile), rows, cols, 4, gdal.GDT_Float32)


# Dark object subtraction from each band (minimum pixel value)
bands = []
for band in range(image.RasterCount):
    band += 1
    stats = image.GetRasterBand(band).GetStatistics(True, True)
    minimum = stats[0]
    bandarray = np.array(image.GetRasterBand(band).ReadAsArray())

    # Write the array to the file
    outdata.GetRasterBand(band).WriteArray(bandarray)

    # Georeference the image
    outdata.SetGeoTransform(trans)

    # Write projection information
    outdata.SetProjection(proj)
