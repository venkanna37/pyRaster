from osgeo import gdal

#stacking 4 bands

blue = gdal.Open('./data/landsat5/LT05_L1TP_141048_20060216_20161123_01_T1_B1.TIF')
green = gdal.Open('./data/landsat5/LT05_L1TP_141048_20060216_20161123_01_T1_B2.TIF')
red = gdal.Open('./data/landsat5/LT05_L1TP_141048_20060216_20161123_01_T1_B3.TIF')
nir = gdal.Open('./data/landsat5/LT05_L1TP_141048_20060216_20161123_01_T1_B4.TIF')

outvrt = './output/stacked.vrt'
outtif = './output/stacked.tif'
bands = [blue,green,red,nir]
outds = gdal.BuildVRT(outvrt, bands, separate = True)
outds = gdal.Translate(outtif, outds)
