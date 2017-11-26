#!env/bin/python
"""Car Restful Web Service"""
from flask import Flask, jsonify, request, abort, make_response
app = Flask(__name__)

# Initial list of cars
cars = [
    {
        'id': 1,
        'color': "red",
        'make': "ford",
        'model': "silverado",
        'year': "2017"
    }, {
        'id': 2,
        'color': "blue",
        'make': "chevy",
        'model': "camero",
        'year': "2014"
    }
]
# Car Value-Specific validation functions
validate_car_value = {
    "color": lambda value: str(value),
    "make": lambda value: str(value),
    "model": lambda value: str(value),
    "year": lambda value: str(value)
}
# Holds the next Car ID
car_id_counter = cars[-1]['id'] + 1
# List of Car Keys whose values can be updated by a PUT request
mutable_car_keys = ["color", "make", "model", "year"]


def filter_cars(car_id):
    """Filter the list of cars given an ID"""
    car = [c for c in cars if c['id'] == car_id]
    if not car:
        abort(404)
    return car


def get_car_from_request(r):
    """Retrieve and validate the car from the API request"""
    car_json = r.json
    if not car_json:
        abort(400)
    print car_json
    return {
        k: validate_car_value[k](car_json[k])
        for k in car_json.keys()
        if k in mutable_car_keys
    }


def update_car(car_id, car_data):
    """
    Updates a car in the 'database'
    Arguments: Car ID, validated car value dict
    """
    car = filter_cars(car_id)[0]
    for key in car_data.keys():
        car[key] = car_data[key]


@app.route('/')
def index():
    """Documentation of the Cars API"""
    return (
        "Welcome to the Cars API.\n" +
        "Use the '/cars' endpoint to get started.\n"
    )


@app.route('/cars', methods=['GET'])
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_cars(car_id=None):
    """GET a list of all cars or specify an id to get a specific car"""
    if car_id is not None:
        car = filter_cars(car_id)
        return jsonify({'data': car})
    return jsonify({'data': cars})


@app.route('/cars', methods=['POST'])
def create_car():
    """POST endpoint that creates new cars. All Car attributes are required."""
    global car_id_counter

    car_data = get_car_from_request(request)
    # Make sure all we have all of the car keys
    if set(mutable_car_keys) != set(car_data.keys()):
        abort(400)
    # set the Car ID
    car_data['id'] = car_id_counter
    # add the new Car to the 'database'
    cars.append(car_data)
    # make sure to increment the ID counter for the next car
    car_id_counter += 1

    return make_response(jsonify({"data": car_data}), 201)


@app.route('/cars/<int:car_id>', methods=['PUT'])
def put_cars(car_id):
    """
    Update a specific Car.
    URL Parameter:  Car ID - int
    Request Body:   Car Data - json
    """
    car_data = get_car_from_request(request)
    update_car(car_id, car_data)
    return jsonify({'error': False})


@app.errorhandler(404)
def not_found(error):
    """Error handler for 404 responses"""
    return make_response(jsonify({'error': 'Car Not Found'}), error.code)


@app.errorhandler(400)
def bad_request(error):
    """Error handler for 400 responses"""
    return make_response(jsonify({'error': 'Bad Car Request.'}), error.code)

if __name__ == "__main__":
    app.run(debug=True)
