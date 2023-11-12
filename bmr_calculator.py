def bmr_calculator(weight, size, age, activity, model = "H&B", gender = "male"):
    """Basal metabolysm rate (BMR), based on Harris and Benedict formula.

    Args:
        weight (float): weight in kg
        size (float): size in m
        age (int): age in years
        activity (float): depend on the subject activity (1.8~2 for sportive people)
        model (string): existing formula Harris and Benedict (H&B) and Black and al.(B&al)
        gender (string): male or female

    Returns:
        float: BMR express in kcal
    """

    coeff = {
        "H&B" : {
            "male": [13.707, 492.3, -6.673, 77.607],
            "female": [9.740, 172.9, -4.737, 667.051]
        },
        "B&al" : {
            "male" : [259, 0.48, 0.50, -0.13],
            "female": [230, 0.48, 0.50, -0.13]
        }
    }

    # get coefficients
    c = coeff[model][gender]
    
    # get the suitable formula
    if model == "H&B":
        bmr = activity * (c[0]*weight + c[1]*size + c[2]*age + c[3])
    elif model == "B&al":
        bmr = activity * (c[0] * weight**(c[1]) * size**(c[2]) * age**(c[3]))
    else:
        raise('Wrong method name' + model)
    return bmr
