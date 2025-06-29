from fastapi import FastAPI, HTTPException, Depends, status, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
from typing import Any, Optional
import json
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBearer()

@app.post("/api/v2/postAlert")
async def postAlert(
        request: Request,
        credentials: HTTPAuthorizationCredentials = Depends(security),
        user_agent: Optional[str] = Header(None, alias="User-Agent"),
        netskope_datatype: Optional[str] = Header(None, alias="X-Netskope-DataType"),
        netskope_subtype: Optional[str] = Header(None, alias="X-Netskope-Subtype"),
        
        ):
    try:
        token = credentials.credentials
        if token != settings.bearer_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    
        raw_body = await request.body()         # Get raw body as bytes
        decoded_body = raw_body.decode("utf-8")
        
        # print("Raw Body (bytes):", raw_body)
        # print("Raw Body (string):", raw_body.decode("utf-8"))
        try:
            json_body = json.loads(decoded_body)
            # print("📥 Received JSON (Pretty Printed):")
            # print(json.dumps(json_body, indent=4))
            
            # Count logic here
            if isinstance(json_body, dict) and "data" in json_body:
                data_items = json_body["data"]
                
                if isinstance (data_items, list):
                     print(f"✅ 'data' contains {len(data_items)} objects.")
                     print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    print("⚠️ 'data' is not a list.")
            else:
                print("⚠️ JSON is not a dict or missing 'data' key.")
            # elif isinstance(json_body, dict):
            #     print(f"✅ JSON is a dict with {len(json_body)} top-level keys.")
            # else:
            #     print("⚠️ JSON is a primitive type, not an object or array.")
                
        except json.JSONDecodeError:
            print("❌ Received non-JSON body:")
            print(decoded_body)

        return {"status": "received"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="An error occured")


