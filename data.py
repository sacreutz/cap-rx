import urllib.parse
import requests
import json
import pandas as pd

main_api = "https://data.medicaid.gov/resource/tau9-gfwr.json"

json_data = requests.get(main_api).json()
stringified = json.dumps(json_data)
f = open("data.json", "w+")
f.write(stringified)
f.close()

#min, max, average, and median:
df = pd.DataFrame(json_data)
df['nadac_per_unit'] = df['nadac_per_unit'].astype(float)
mean = df["nadac_per_unit"].mean()
max = df["nadac_per_unit"].max(axis = 0)
min = df["nadac_per_unit"].min(axis = 0)
median = df["nadac_per_unit"].median()
describe = df['nadac_per_unit'].describe()
print(mean, "mean")
print(max, "max")
print(min, "min")
print(median, "median")
print(describe, "describe")



