import json
import matplotlib.pyplot as plt

# Load data
with open("output.json", "r") as f:
    data = json.load(f)

# Extract device IDs and average temperatures
devices = list(data.keys())
avg_temps = [data[d]["avg_temperature"] for d in devices]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(devices, avg_temps, color="steelblue", edgecolor="black")

ax.set_xlabel("Device ID")
ax.set_ylabel("Average Temperature (°C)")
ax.set_title("Average Temperature per Device")
ax.bar_label(bars, fmt="%.2f", padding=3)

plt.tight_layout()
plt.savefig("avg_temperature_per_device.png", dpi=150)
plt.show()