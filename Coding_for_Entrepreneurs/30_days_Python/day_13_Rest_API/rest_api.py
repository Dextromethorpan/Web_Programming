#REST API
#We are gonna use "themoviedb.org"
import requests




api_key="" # hay que crear la cuenta


movie_id=501
api_version=4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path=f"/movie/{movie_id}"

endpoint=f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}

r=requests.get(endpoint)
print(r.status_code)
print(r.text)


