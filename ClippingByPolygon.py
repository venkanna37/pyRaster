from osgeo import gdal, ogr

# reading raster file
image = gdal.Open("./output/vizag.tif")

# reading vector file
driver = ogr.GetDriverByName('ESRI Shapefile')
polygon = driver.Open(r'./data/shapefiles/study_area.shp')

# clipping raster with shapefile
clip_image = gdal.Translate('./output/polygon_clipping.tif',image, projWin = polygon )
