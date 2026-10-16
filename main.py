# Section 2 - device telemetry summary
import csv
import json

filename = "device_telemetry.csv"
data = {}      # device_id -> list of (status, temp)
bad_rows = 0

try:
    f = open(filename, newline="")
except FileNotFoundError:
    print("File not found:", filename)
    exit()

reader = csv.DictReader(f)
for row in reader:
    try:
        dev = row["device_id"]
        status = row["status"]
        temp = float(row["temperature"])
    except (ValueError, KeyError, TypeError):
        bad_rows += 1
        continue

    if dev not in data:
        data[dev] = []
    data[dev].append((status, temp))
f.close()

if len(data) == 0:
    print("No valid data in file")
    exit()

result = {}
for dev in data:
    records = data[dev]
    total = len(records)

    temp_sum = 0
    errors = 0
    for status, temp in records:
        temp_sum += temp
        if status == "ERROR":
            errors += 1

    avg = round(temp_sum / total, 2)

    # skip devices with avg temp above 80
    if avg > 80.0:
        continue

    result[dev] = {
        "total_records": total,
        "avg_temperature": avg,
        "error_count": errors
    }

with open("output.json", "w") as out:
    json.dump(result, out, indent=4)

# print table
print("Device   Records   AvgTemp   Errors")
print("-" * 36)
for dev in result:
    r = result[dev]
    print(f"{dev:<9}{r['total_records']:<10}{r['avg_temperature']:<10}{r['error_count']}")

print("\nBad rows skipped:", bad_rows)
