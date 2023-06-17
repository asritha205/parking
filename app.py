import uvicorn
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import os


app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")


# @app.get("/")
# async def root():
#    return {"message": "hello world"}

@app.get("/")
def read_root():
    with open("templates/base.html", 'r') as file:
        content = file.read()
    return HTMLResponse(content=content)
from fastapi.responses import FileResponse

@app.get("/video")
async def get_video():
    return FileResponse("static/boxvedio.mp4", media_type="video/mp4")
@app.get("/image")
async def get_image():
    return FileResponse("static/backg.png")

# To run locally
if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)