from fastapi import FastAPI, HTTPException, Depends, status, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
from typing import Any, Optional, List
import pprint

app = FastAPI()
security = HTTPBearer()

@app.post("/api/v2/postAlert")
async def postAlert(
        payload: List[Any],
        credentials: HTTPAuthorizationCredentials = Depends(security),
        user_agent: Optional[str] = Header(None, alias="User-Agent"),
        netskope_datatype: Optional[str] = Header(None, alias="X-Netskope-DataType"),
        netskope_subtype: Optional[str] = Header(None, alias="X-Netskope-Subtype"),
        
        ):
    try:
        print("=" * 80)
        print("Received new data from Netskope Plugin")
        print("-" * 80)
        
        # Pretty-print the JSON payload
        print("Payload Content:")
        pprint.pprint(payload)
        
        print("=" * 80 + "\n")
        
        return {
            "status": "success",
            "message": f"Successfully received {len(payload)} records."
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="An error occured")
    
