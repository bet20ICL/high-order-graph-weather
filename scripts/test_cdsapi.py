import cdsapi
from pathlib import Path

cds = cdsapi.Client()

dataset_dir = "/work/ec249/ec249/bet20/dataset"

year = 2022
month = 12
time = "00:00"
day = 1

year_str = str(year)
month_str = str(month).zfill(2)
day_str = str(day).zfill(2)



cds.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            'geopotential', 'specific_humidity','temperature',
            'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity',
        ],
        'pressure_level': [
            '50', '150', '250', '400', '600', '850', '1000'
        ],
        'year': str(year),
        'month': str(month).zfill(2),
        'day': str(day).zfill(2),
        'time': time,
        #'area': area,
        'format': 'netcdf',
    },
    f'{dataset_dir}/{year_str}_{month_str}_{day_str}_{time.replace(":", "_")}.nc'
)