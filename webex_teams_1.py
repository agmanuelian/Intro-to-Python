import requests
import json
from datetime import datetime

token = "ZDQ0NTQ0MzQtNWJmYi00YjdhLWFhMDItODBkZWI0NjNlMWYxYmUzMzEzN2QtNzVj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNWI3YzE4NTAtYTc5MC0xMWVhLWIwMjAtMmYwMjVhNDY4OTdm"
roomId_Accenture = "Y2lzY29zcGFyazovL3VzL1JPT00vMTI3NDJiNjAtMGUzOS0xMWViLTlkNjYtMTk4N2E2NTY1NmRh"
time = datetime.now()

url = f'https://webexapis.com/v1/messages'

headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "roomId": roomId,
    "text": f"""
    Mensaje de prueba publicado desde una API, dejando todo listo para la sesión de mañana.
    .:|:.:|:. Cisco Systems .:|:.:|:.
    {time}
    """
 }

requests.post(url=url, headers=headers, data=json.dumps(body))

