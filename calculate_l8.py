import os
import numpy as np
import rasterio
import geopandas as gpd
from rasterio.mask import mask

class Calculate_NDVI_LST_L8:
    def __init__(self,band4_l8,band5_l8,band10_l8,shape_l8,ndvi_l8,lst_l8):
        
        super().__init__()
        
        self.calculate_ndvi_landsat_8_9(band4_l8,band5_l8,ndvi_l8)
        
        self.calculate_lst_landsat_8_9(band10_l8,lst_l8)
        
        self.clip_rasters_with_shp(ndvi_l8,lst_l8,shape_l8,ndvi_l8,lst_l8)
        
        
    def calculate_ndvi_landsat_8_9(self,red_band_path, nir_band_path, output_path):
        with rasterio.open(red_band_path) as red_src:
            red_band = red_src.read(1).astype(float)
            profile = red_src.profile  

        with rasterio.open(nir_band_path) as nir_src:
            nir_band = nir_src.read(1).astype(float)
        

        with np.errstate(divide='ignore', invalid='ignore'):
            ndvi = (nir_band - red_band) / (nir_band + red_band)
            ndvi[(nir_band + red_band) == 0] = np.nan

        
        profile.update(dtype=rasterio.float32, count=1, driver='GTiff')
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(ndvi, 1)

        print(f"Landsat 8/9 NDVI xeritesi '{output_path}' kimi yazildi.")
        return output_path


    def calculate_lst_landsat_8_9(self,thermal_band_path, output_path):
        radiance_mult=0.0003342
        radiance_add=0.1
        k1=774.89
        k2=1321.08
        with rasterio.open(thermal_band_path) as thermal_src:
            thermal_band = thermal_src.read(1).astype(float)
            profile = thermal_src.profile  
        
    
        radiance = radiance_mult * thermal_band + radiance_add
        lst = k2 / np.log((k1 / radiance) + 1) - 273.15
        lst[np.isinf(lst)] = np.nan

    
        profile.update(dtype=rasterio.float32, count=1, driver='GTiff')
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(lst, 1)

        print(f"Landsat 8/9 seth tempratur xeritesi '{output_path}' kimi yazildi.")
        return output_path


    # Raster datasini bir poliqonla kesmek
    def clip_rasters_with_shp(self,NDVI_path, LST_path, shp_path, NDVI_output_folder, LST_output_folder):
       # Shapefile yukleyir ve geometriyalari alir
        shp = gpd.read_file(shp_path)
        geoms = [feature["geometry"] for feature in shp.iterfeatures()]

        # Raster fayillarini kesip yeni fayillar kimi yazmaq
        for raster_path, output_folder in zip([NDVI_path, LST_path], [NDVI_output_folder, LST_output_folder]):
            with rasterio.open(raster_path) as src:
                out_image, out_transform = mask(src, geoms, crop=True)
                out_meta = src.meta.copy()
                out_meta.update({
                    "driver": "GTiff",
                    "height": out_image.shape[1],
                    "width": out_image.shape[2],
                    "transform": out_transform
                })

                # Orijinal fayl adini alir ve sonuna "_" elave ederek yeni ad yaradir
                base_name = os.path.basename(raster_path)
                name, ext = os.path.splitext(base_name)
                output_path_ = os.path.dirname(output_folder)
                
                # Folder yolundan istifade ederek tam fayl yolunu yaradir
                output_path = os.path.join(output_path_, f"{name}_.tif")

                # Folderin movcdulugunu yoxlayir
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                with rasterio.open(output_path, 'w', **out_meta) as dest:
                    dest.write(out_image[0], 1)

                print(f"Kesilmis raster fayli '{output_path}' kimi yadda saxlanilir.")




