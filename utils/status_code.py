import json
from requests import Response


class Verification:
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success. Status code: " + str(response.status_code))
        else:
            print("Failure. Status code: " + str(response.status_code))

    @staticmethod
    def check_json_field(response: Response, expected_result):
        token = json.loads(response.text)
        # print(token)
        assert list(token) == expected_result
        print("All json fields are exist")

    @staticmethod
    def check_json_values(response: Response, field_name, expected_result):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_result
        print(field_name + " field is correct")

    @staticmethod
    def check_json_values_by_search(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " is existing")
        else:
            print("Word " + search_word + " is missing")
