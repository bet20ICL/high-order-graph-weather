"""Load downloaded ERA5 data"""
import xarray as xr
import zarr
import numcodecs
import sys

dataset_path = "dataset/2022_01_03.nc"
data = xr.open_dataset(dataset_path, engine="netcdf4")

