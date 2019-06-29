import urllib.parse
import requests
import json
import pandas as pd


main_api = "https://data.medicaid.gov/api/views/a4y5-998d/rows.json"

json_data = requests.get(main_api).json()
stringified = json.dumps(json_data)
f = open("data.json", "w+")
f.write(stringified)
f.close()

data = json.load(open('data.json'))

df = pd.DataFrame(data["data"])
df.columns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "ndc_description", "ndc", "nadac_per_unit", "effective_date", "pricing_unit", "pharmacy_type_indicator", "otc", "explanation_code", "classification_for_rate_setting", "null", "null2", "as_of_date"]
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



