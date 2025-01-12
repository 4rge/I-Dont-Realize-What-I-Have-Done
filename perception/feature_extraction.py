def extract_features(data):
    # Simple feature extraction
    features = {}
    if data['sound'] == 'loud':
        features['attention'] = 'high'
    else:
        features['attention'] = 'low'
    
    features['object'] = data['image']
    return features
