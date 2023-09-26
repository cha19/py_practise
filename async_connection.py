from flask import Flask
from time import sleep
import asyncio

app=Flask(__name__)

@app.route('/')
async def home():
    result=await end()
    return "this is a home page"


@app.route('/end')
async def end():
    await asyncio.sleep(5)
    
    return "end page"
if __name__=='__main__':
    app.run(debug=True)    

# async def get_chat_id(name):
#     await asyncio.sleep(3)
#     return "chat-%s" % name

# async def main():
#     result = await get_chat_id("django")