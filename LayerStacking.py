from osgeo import gdal

#stacking 4 bands

blue = gdal.Open('./data/landsat5/blue.tif')
green = gdal.Open('./data/landsat5/green.tif')
red = gdal.Open('./data/landsat5/red.tif')
nir = gdal.Open('./data/landsat5/nir.tif')

outvrt = './output/vizag.vrt'
outtif = './output/vizag.tif'
bands = [blue,green,red,nir]
outds = gdal.BuildVRT(outvrt, bands, separate = True)
outds = gdal.Translate(outtif, outds)
