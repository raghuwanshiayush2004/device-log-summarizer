# Device Log Summarizer

Small Python project for the Software Engineering Intern assessment.

## Files

- `section1.py` - function to clean sensor readings (with 3 test cases)
- `main.py` - reads `device_telemetry.csv`, groups by device, saves `output.json` and prints a table
- `chart_ai.py` - bar chart of average temperature per device (written with AI help, see PROMPT_LOG.md)
- `device_telemetry.csv` - input data
- `output.json` - sample output
- `avg_temperature_per_device.png` - sample chart
- `PROMPT_LOG.md` - how I used AI for the chart

## How to run

Install matplotlib first:

    pip install matplotlib

Then run:

    python section1.py
    python main.py
    python chart_ai.py

## What each part does

**Section 1:** `clean_readings()` converts values to float, drops None, invalid text and negative values, and caps anything above 500 to 500. Empty or fully invalid lists return an empty list.

**Section 2:** `main.py` groups rows by `device_id` and calculates total records, average temperature and ERROR count. Devices with average temperature above 80 are removed. Bad rows are skipped, and a missing file shows an error message instead of crashing.

**Section 3:** `chart_ai.py` reads `output.json` and saves a bar chart.
