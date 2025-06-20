from fastapi import FastAPI, HTTPException, Depends, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
from typing import Any, Optional

app = FastAPI()
security = HTTPBearer()

@app.post("/api/v2/postAlert")
async def postAlert(
        data:dict, 
        credentials: HTTPAuthorizationCredentials = Depends(security),
        user_agent: Optional[str] = Header(None, alias="User-Agent"),
        netskope_datatype: Optional[str] = Header(None, alias="X-Netskope-DataType"),
        netskope_subtype: Optional[str] = Header(None, alias="X-Netskope-Subtype"),
        
        ):
    try:
        token = credentials.credentials
        if token != settings.bearer_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    
        print(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="An error occured")
    
