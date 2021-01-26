from dataclasses import dataclass
import requests



@dataclass()
class Airtable:
    base_id:str
    api_key:str
    table_name:str

    def create_records(self, data={}):
        if len(data.keys()) == 0:
            return False
        endpoint = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "records": [
                {
                    "fields": data
            }
            ]
        }
        r = requests.post(endpoint, json=data, headers=headers)
        print(endpoint, r.json())
        return r.status_code == 200 or r.status_code == 201