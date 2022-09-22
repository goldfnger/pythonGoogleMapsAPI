from requests import Response
from utils.api import GoogleMapsApi
from utils.status_code import Verification
import allure


# allure usage
# command in pycharm terminal to run test and create report for it:
# python3 -m pytest --alluredir=test_results/ tests/test_google_maps_api.py
# command in terminal to generate report and display it in browser:
# cd <to project root directory> then allure serve test_results/


@allure.epic("Test create new place")
class TestCreatePlace:
    @allure.description("Test create, update, delete new place")
    def test_create_place(self):
        print("Creating a new place")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Verification.check_status_code(result_post, 200)
        Verification.check_json_field(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # to get all fields from the response. later could be used for check_json_field()
        # token = json.loads(result_post.text)
        # print(list(token))
        Verification.check_json_values(result_post, "status", 'OK')

        print("Verifying creation of new place")
        result_get: Response = GoogleMapsApi.get_place(place_id)
        Verification.check_status_code(result_get, 200)
        Verification.check_json_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Verification.check_json_values(result_get, "address", "29, side layout, cohen 09")

        print("Updating existing place with a new address")
        result_put: Response = GoogleMapsApi.put_place(place_id)
        Verification.check_status_code(result_put, 200)
        Verification.check_json_field(result_put, ['msg'])
        Verification.check_json_values(result_put, "msg", "Address successfully updated")

        print("Verifying updated address")
        result_get: Response = GoogleMapsApi.get_place(place_id)
        Verification.check_status_code(result_get, 200)
        Verification.check_json_values(result_get, "address", "100 SUPER STREET, WEB")

        print("Deleting created place")
        result_delete: Response = GoogleMapsApi.delete_place(place_id)
        Verification.check_status_code(result_delete, 200)
        Verification.check_json_field(result_delete, ['status'])
        Verification.check_json_values(result_delete, "status", "OK")

        print("Verifying deletion")
        result_get: Response = GoogleMapsApi.get_place(place_id)
        Verification.check_status_code(result_get, 404)
        Verification.check_json_field(result_get, ['msg'])
        Verification.check_json_values(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")
        Verification.check_json_values_by_search(result_get, "msg", "failed")

        print("Testing is done. Location creating, updating, deleting are succeed.")
