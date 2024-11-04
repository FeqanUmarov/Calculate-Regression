import os
import numpy as np
import rasterio
from sklearn.linear_model import LinearRegression
from tqdm import tqdm
import geopandas as gpd
from rasterio.mask import mask

class Calculate_Regression_Analysis:
    def __init__(self, ndvi_folder, lst_folder, regression_output_path):
        super().__init__()
        
        # NDVI ve LST fayillari yukleyir
        ndvi_files = self.load_raster_files_from_folder(ndvi_folder)
        lst_files = self.load_raster_files_from_folder(lst_folder)
        
        if len(ndvi_files) != len(lst_files):
            raise ValueError("NDVI ve LST fayillari uygunlasmir")
        
        # Raster fayillari yukleyir
        ndvi_stack = self.load_rasters(ndvi_files)
        lst_stack = self.load_rasters(lst_files)
        
        # Regressiya analizi
        regression_map = self.perform_regression_analysis(ndvi_stack, lst_stack)
        
        # Regressiya neticeleri
        self.save_regression_result(regression_map, ndvi_files[0], regression_output_path)
        
    def load_raster_files_from_folder(self, folder_path):
        # Verilen folder-dan raster-leri alir
        filepaths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.tif')]
        return filepaths

    def load_rasters(self, filepaths):
        # Raster fayillari yukleyir
        arrays = []
        for filepath in tqdm(filepaths, desc=f"Raster fayillari yukle"):
            with rasterio.open(filepath) as src:
                arrays.append(src.read(1).astype(float))
        return np.array(arrays)

    def perform_regression_analysis(self, ndvi_stack, lst_stack):
        # Raster fayillari uzerinde regressiya analizi edir
        rows, cols = ndvi_stack.shape[1:]
        regression_map = np.zeros((rows, cols), dtype=np.float32)

        print("Regressiya analizi baslayir...")
        for i in tqdm(range(rows), desc="Setrler oxunur"):
            for j in range(cols):
                ndvi_series = ndvi_stack[:, i, j]
                temp_series = lst_stack[:, i, j]

                valid_mask = ~np.isnan(ndvi_series) & ~np.isnan(temp_series)
                if valid_mask.sum() > 1:
                    X = temp_series[valid_mask].reshape(-1, 1)
                    y = ndvi_series[valid_mask]

                    model = LinearRegression().fit(X, y)
                    regression_map[i, j] = model.coef_[0]
                else:
                    regression_map[i, j] = np.nan

        return regression_map

    def save_regression_result(self, regression_map, reference_file, output_path):
        # Regressiya neticelerini raster kimi yadda saxlayir
        with rasterio.open(reference_file) as src:
            profile = src.profile
            profile.update(dtype=rasterio.float32, count=1, driver='GTiff')

        print("Regressiya neticeleri yadda saxlanilir...")
        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(regression_map, 1)

        print(f"Regressiya raster fayl '{output_path}' kimi yadda saxlanildi.")
