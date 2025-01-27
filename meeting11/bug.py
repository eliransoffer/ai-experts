import json
from pprint import pprint

import requests


def get_diffs(avalara_data: list, spreadsheet_data: list):
    avalara_doc_codes = set(map(lambda item: item["DocCode"], avalara_data))
    spreadsheet_doc_codes = set(map(lambda item: item["DocCode"], spreadsheet_data))

    items_missing_in_avalara = spreadsheet_doc_codes - avalara_doc_codes
    items_missing_in_spreadsheet = avalara_doc_codes - spreadsheet_doc_codes
    docs_in_avalara_and_spreadsheet = avalara_doc_codes.intersection(spreadsheet_doc_codes)
    same_doc_code_diff_field = []

    avalara_doc_code_to_item = {item["DocCode"]: item for item in avalara_data}
    spreadsheet_doc_code_to_item = {item["DocCode"]: item for item in spreadsheet_data}

    # check whether there are items with same doccode but different fields
    for doc_code in docs_in_avalara_and_spreadsheet:
        avalara_item = avalara_doc_code_to_item[doc_code]
        spreadsheet_item = spreadsheet_doc_code_to_item[doc_code]
        if (avalara_item["TaxCode"] != spreadsheet_item["TaxCode"] or
                avalara_item["ItemCode"] != spreadsheet_item["ItemCode"] or
                avalara_item["Amount"] != spreadsheet_item["Amount"]):
            same_doc_code_diff_field.append(doc_code)
    return items_missing_in_avalara, items_missing_in_spreadsheet, same_doc_code_diff_field


if __name__ == "__main__":
    spreadsheet_data = requests.get("https://storage.googleapis.com/ai-experts/bug/spreadsheet_data.json").json()
    avalara_data = requests.get("https://storage.googleapis.com/ai-experts/bug/avalara_data.json").json()
    print(get_diffs(avalara_data, spreadsheet_data))