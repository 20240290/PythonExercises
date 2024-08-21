# Joseph Patambag
# August 19, 2024

#Module import

# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

def make_car(manufacturer: str, model: str, **car_props):
    """
    Method to show information of a specific car.

    Parameters
    ----------
    manufacturer: string
        Car manufacturer.
    model: string
        Car model.
    car_props: variable
        Variable parameter which will add more information of the car.

    Returns
    -------
    user_info: dictionary
        Car information.

    """
    #car variable that holds the manufacturer and model
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    #iterate car props and add it in the car dictionary
    for key,value in car_props.items():
        car[key] = value
    return car  