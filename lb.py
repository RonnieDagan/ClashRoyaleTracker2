import requests

# Replace with your API key
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI3OTdlYTkwLTYzYzEtNDZmZC05NzhmLWM3MWQ4MmMzOTEyNiIsImlhdCI6MTcxNzA0NjQ4Miwic3ViIjoiZGV2ZWxvcGVyLzc0NTYzNDA3LWZhMTQtMmQyNS0xYTIzLTMwM2Y5YWI1NTQxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMC4xNzEuNzcuMTc5Il0sInR5cGUiOiJjbGllbnQifV19.6YTKZ4RL0kWD30DuCQxDcxjrX9ICJWK0fkNqx-ig41SVbYuISeD3uj0JxD4cUubKEX_9M76ACngYaWHb4g4Vdg'

import requests
import json
r=requests.get("https://api.clashroyale.com/v1/locations/57000006/rankings/players", headers={"Accept":"application/json", "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI3OTdlYTkwLTYzYzEtNDZmZC05NzhmLWM3MWQ4MmMzOTEyNiIsImlhdCI6MTcxNzA0NjQ4Miwic3ViIjoiZGV2ZWxvcGVyLzc0NTYzNDA3LWZhMTQtMmQyNS0xYTIzLTMwM2Y5YWI1NTQxYyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyMC4xNzEuNzcuMTc5Il0sInR5cGUiOiJjbGllbnQifV19.6YTKZ4RL0kWD30DuCQxDcxjrX9ICJWK0fkNqx-ig41SVbYuISeD3uj0JxD4cUubKEX_9M76ACngYaWHb4g4Vdg"}, params = {"limit":20})
print(json.dumps(r.json(), indent = 2))