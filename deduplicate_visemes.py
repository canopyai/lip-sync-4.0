def deduplicate_visemes(data):
    indices_to_modify = []

    # Check for equality between elements 0 through 32 inclusive
    for i in range(len(data) - 1):
        if (data[i]['targets'][:33] != data[i + 1]['targets'][:33]) and data[i + 1]["word"]!="DUP":
            indices_to_modify.append(i)

    # Apply modifications at the identified indices
    for i in indices_to_modify:
        # Only scale elements 0 through 32
        scaled_targets = [x * 0.8 for x in data[i]['targets'][:33]] + data[i]['targets'][33:]
        scaled_targets[0] += 0.2  # Add 0.2 to the first element of the scaled portion
        data[i]['targets'] = scaled_targets

    return data

