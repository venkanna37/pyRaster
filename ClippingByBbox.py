import gdal

image = gdal.Open('./output/vizag.tif')
image = gdal.Translate('./output/bbox_clipping.tif', image, projWin = [724465, 1968215, 749990, 1945090])
