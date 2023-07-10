#Забелин Андрей, 6-я когорта - Диплом, Инженер по тестированию +
import data
import configuration
import requests
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body, headers=data.order_headers)
def new_order_track():
    order_response = create_order(data.order_body)
    order_track = order_response.json()["track"]
    return order_track
def get_order(order_track):
    order_number = configuration.ORDER_TRACK + "?t=" + str(order_track)
    return requests.get(configuration.URL_SERVICE + order_number, headers=data.order_headers)

def test_get_order():
    track = new_order_track()
    order_response = get_order(track)
    assert order_response.status_code == 200
    assert order_response.json()
