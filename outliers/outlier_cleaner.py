#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        
        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    # Calculate the residual errors
    errors = [(net_worths[i] - predictions[i]) for i in range(len(predictions))]

    # Combine ages, net_worths, and errors into a list of tuples
    data_with_errors = list(zip(ages, net_worths, errors))

    # Sort the data by error in ascending order
    data_with_errors.sort(key=lambda x: x[2])

    # Retain the top 90% of data points (remove the 10% with the largest errors)
    limit = int(len(data_with_errors) * 0.9)
    cleaned_data = data_with_errors[:limit]



    
    return cleaned_data

