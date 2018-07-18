def total_feature_contributions(feature):
    contributions = feature.contributions.all()
    total = 0 
    for obj in contributions:
        total += obj.contribution
    return total