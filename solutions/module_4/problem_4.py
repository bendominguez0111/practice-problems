def percentile(list_obj, percentile):
    """
    perecentile must be a float between 0 and 1.0
    """
    sorted_list_obj = sorted(list_obj, reverse=True)

    n = int(round(percentile * len(sorted_list_obj) + 0.5))

    return sorted_list_obj[n - 1]