import urllib.parse
import requests
import json
import pandas as pd

main_api = "https://data.medicaid.gov/resource/tau9-gfwr.json"

json_data = requests.get(main_api).json()
print(json_data[0])
stringified = json.dumps(json_data)
f = open("data.json", "w+")
f.write(stringified)
f.close()

per_unit = {}
total = 0

for c in json_data:
  if c["otc"] == "N" and c["classification_for_rate_setting"] == "G":

      nadac = c["nadac_per_unit"]
      per_unit[c["ndc_description"]] = nadac
      total += float(nadac)

top_nadac = sorted(per_unit.items(), key=lambda x: x[1], reverse = True)

#maximum
max_nadac = top_nadac[0][1]

#minimum
min_nadac = top_nadac[-1][1]

#average
average_nadac = total / len(per_unit)

#median
median_nadac = (float(top_nadac[193][1]) + float(top_nadac[194][1])) / 2


print("max: ", max_nadac)
print("min: ", min_nadac)
print("average: ", average_nadac)
print("median: ", median_nadac)

df = pd.DataFrame(json_data)
df['nadac_per_unit'] = df['nadac_per_unit'].astype(float)
mean = df["nadac_per_unit"].mean()
max = df["nadac_per_unit"].max(axis = 0)
describe = df['nadac_per_unit'].describe()
#print(df, "dataframe")
print(mean, "mean")
print(max, "max")
print(describe, "describe")



