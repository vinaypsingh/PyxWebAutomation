import requests
import pytest


@pytest.mark.positive
def test_creating_booking_positive():
    print("Creating Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Vinay",
        "lastname": "Brown",
        "totalprice": 235,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-02",
            "checkout": "2024-03-01"
        },
        "additional needs": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertion
    assert response.status_code == 200

    # get the response body and verify the json, booking id is not none
    data = response.json()
    booking_id = data["bookingid"]
    print(data["bookingid"])
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Vinay", "incorrect firstname"


@pytest.mark.negative
def test_creating_booking_negative():
    print("Creating Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {

    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertion
    assert response.status_code == 500

    # #get the response body and verify the json, booking id is not none
    # data = response.json()
    # print(data)
    # assert data["bookingid"] is not None
    # assert data["booking"]["firstname"] == "Vinay", "incorrect firstname"
