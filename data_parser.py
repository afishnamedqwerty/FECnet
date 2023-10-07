def parse_data(raw_data):
    parsed_data = []
    
    for entry in raw_data:
        # Create a dictionary for each entry
        entry_data = {
            'office': entry['office'],
            'candidate': entry['candidate'],
            'total_receipts': entry['total_receipts'],
            'donors': entry['donors'],
            'committee': entry['committee']
        }
        
        parsed_data.append(entry_data)
        
    return parsed_data
