from utils.http_method import HttpMethods

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"
key_place_id = "&place_id="


class GoogleMapsApi:

    @staticmethod  # does not depend on any classes or variables
    def create_new_place():
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_api = "/maps/api/place/add/json"
        post_url = base_url + post_api + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)

        return result_post

    @staticmethod
    def get_place(place_id):
        get_api = "/maps/api/place/get/json"
        get_url = base_url + get_api + key + key_place_id + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)

        return result_get

    @staticmethod
    def put_place(place_id):
        put_api = "/maps/api/place/update/json"
        updated_address = "100 SUPER STREET, WEB"

        put_url = base_url + put_api + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": updated_address,
            "key": "qaclick123",
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)

        return result_put

    @staticmethod
    def delete_place(place_id):
        delete_api = "/maps/api/place/delete/json"

        delete_url = base_url + delete_api + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }

        result_delete = HttpMethods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)

        return result_delete
