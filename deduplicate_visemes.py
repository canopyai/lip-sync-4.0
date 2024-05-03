def deduplicate_visemes(data):
    # List to hold indices where modifications should be applied
    indices_to_modify = []

    # Identify all indices that need modification
    for i in range(len(data) - 1):
        if data[i]['targets'] == data[i + 1]['targets']:
            indices_to_modify.append(i)

            print(data[i]['targets'])
            print(data[i + 1]['targets'])
            print("***")
            

    # Apply modifications at the identified indices
    for i in indices_to_modify:
        data[i]['targets'] = [x * 0.8 for x in data[i]['targets']]
        data[i]['targets'][0] += 0.2  # Add 0.2 to the first element

    return data


    
