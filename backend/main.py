from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend React dev server (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Allowed commands
ALLOWED_COMMANDS = {
    "list_dir": "dir",#"ls -la",
    "show_date": "date",
    "disk_usage": "df -h",
    "uptime": "uptime"
}

class CommandRequest(BaseModel):
    command: str

@app.post("/run")
async def run_command(req: CommandRequest):
    cmd_key = req.command
    if cmd_key not in ALLOWED_COMMANDS:
        raise HTTPException(status_code=400, detail="Invalid command")
    
    try:  
        result = subprocess.run(
            ALLOWED_COMMANDS[cmd_key],
            shell=True, capture_output=True, text=True
        )
        return {
            "success": result.returncode == 0,
            "output": result.stdout if result.returncode == 0 else result.stderr
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))