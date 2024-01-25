def division_aggregation(location_key: str) -> str:
    """
    Categorize the location_key into a regional division based on US Census Bureau
    """
    state = location_key.split("_")[1]
    if state in ["CT", "ME", "MA", "NH", "RI", "VT"]:
        return "New England"
    elif state in ["NJ", "NY", "PA"]:
        return "Mid-Atlantic"
    elif state in ["IL", "IN", "MI", "OH", "WI"]:
        return "East North Central"
    elif state in ["IA", "KS", "MN", "MO", "NE", "ND", "SD"]:
        return "West North Central"
    elif state in ["DE", "FL", "GA", "MD", "NC", "SC", "VA", "DC", "WV"]:
        return "South Atlantic"
    elif state in ["AL", "KY", "MS", "TN"]:
        return "East South Central"
    elif state in ["AR", "LA", "OK", "TX"]:
        return "West South Central"
    elif state in ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY"]:
        return "Mountain"
    elif state in ["AK", "CA", "HI", "OR", "WA"]:
        return "Pacific"
    else:
        return "Other"
