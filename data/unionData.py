import os

path = './RawData'

os.remove('data.scv')
endFile = open('data.scv','w+')
endFile.write("time	psfc	msl	wSpeed.50	wDir.50	wSpeed.850hpa	wDir.850hpa	temperature.10	temperature.50	dispHeight	precIceWater	precLiqWater	precWaterVapor	specHumidity.10\n")

for year in os.listdir(path):
    for month in os.listdir(f"{path}/{year}"):
        data_file = open(f"{path}/{year}/{month}")
        endFile.writelines(data_file.readlines()[13::])
        data_file.close()
endFile.close()
