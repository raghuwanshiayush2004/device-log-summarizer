# PROMPT_LOG

## Initial prompt
Write a Python script that loads output.json (dict of device_id -> total_records, avg_temperature, error_count) and makes a matplotlib bar chart of average temperature per device.

## One bug / mistake in the first attempt
The y-axis label said only "Average Temperature" with no unit, and the x-axis labels (DEV_A, DEV_B, ...) were rotated 45 degrees even though there are only a few devices and they fit horizontally.

## Follow-up prompt I used to fix it
Add the unit (°C) to the y-axis label and keep the x-axis labels horizontal since there are only a few devices.
