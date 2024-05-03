def deduplicate_visemes(data):
    for i in range(len(data) - 1):
        if data[i]['targets'] == data[i + 1]['targets']:
            # Update the current 'targets' list
            data[i]['targets'] = [x * 0.8 for x in data[i]['targets']]
            data[i]['targets'][0] += 0.2  # Add 0.2 to the first element
    
    return data

    
