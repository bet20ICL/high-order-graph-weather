import time
import glob
import numpy as np
import xarray as xr
import torch
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim

from high_order_graph_weather.models.losses import NormalizedMSELoss
from high_order_graph_weather import GraphConvolutionForecaster, GraphWeatherForecaster
import scripts.constants as constsants

# data_path = f"{constants.DATASET_PATH}/global/2022_01.nc"
# class ToyERA5Dataset(Dataset):
#     def __init__(self, data_path) -> None:
#         super().__init__()
#         data = xr.open_dataset(data_path)
#         self.lat_lons = np.array(np.meshgrid(data.latitude.values, data.longitude.values)).T.reshape(-1, 2)
#         self.dataset 
        
#     def __len__(self):
#         return self.dataset.shape[0] - 1
        
# dataset = ToyERA5Dataset(data_path)

lat_lons = []
for lat in range(-90, 90, 1):
    for lon in range(0, 360, 1):
        lat_lons.append((lat, lon))
model = GraphConvolutionForecaster(lat_lons)

features = torch.randn((2, len(lat_lons), 78))

out = model(features)
criterion = NormalizedMSELoss(lat_lons=lat_lons, feature_variance=torch.randn((78,)))
loss = criterion(out, features)
loss.backward()

print("Done!")

# model = GraphWeatherForecaster(lat_lons)
# criterion = NormalizedMSELoss(lat_lons=lat_lons, feature_variance=torch.randn((78,)))
# optimizer = optim.AdamW(model.parameters(), lr=0.001)
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# for epoch in range(100):  # loop over the dataset multiple times
#     running_loss = 0.0
#     print(f"Start Epoch: {epoch}")
#     for i, data in enumerate(dataset):
#         start = time.time()
#         # get the inputs; data is a list of [inputs, labels]
#         inputs, labels = data[0].to(device), data[1].to(device)
#         # zero the parameter gradients
#         optimizer.zero_grad()

#         # forward + backward + optimize
#         outputs = model(inputs)

#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

#         # print statistics
#         running_loss += loss.item()
#         end = time.time()
#         print(
#             f"[{epoch + 1}, {i + 1:5d}] loss: {running_loss / (i + 1):.3f} Time: {end - start} sec"
#         )

# print("Finished Training")
# torch.save(model.state_dict(), '/local/scratch-2/asv34/graph_weather/dataset/models/jan2022_rescaled_100epochs.pt')