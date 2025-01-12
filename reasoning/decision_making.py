def make_decision(features):
    if features['attention'] == 'high':
        return f"Focus on the {features['object']}."
    return "No significant focus needed."
