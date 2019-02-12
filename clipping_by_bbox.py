from osgeo import gdal
import sys

# Reading source raster(tif) file
image = gdal.Open('./output/vizag.tif')
if image is None:
    print 'Unable to open the source file'
    sys.exit()

# Clipping source file using bounding box (bbox)
# the format of bbox os [x min,y max,x max,y min] or [top left corner, bottom right corner]
image = gdal.Translate('./output/bbox_clipping.tif', image, projWin = [724465, 1968215, 749990, 1945090])
