# Section 1 - clean sensor readings

def clean_readings(data):
    result = []

    # empty list or None
    if not data:
        return result

    for x in data:
        if x is None:
            continue

        try:
            val = float(x)
        except (ValueError, TypeError):
            continue   # cant convert so skip

        if val < 0:
            continue   # negative = error flag

        if val > 500.0:
            val = 500.0

        result.append(val)

    return result


# tests
print(clean_readings(["10", 20.5, None, "abc", -5, 800]))   # [10.0, 20.5, 500.0]
print(clean_readings([]))                                    # []
print(clean_readings([None, "x", -1]))                       # []
