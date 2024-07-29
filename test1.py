import json
import aiofiles as aiof
import aiohttp
import uvicorn
from aiohttp import ClientConnectorError
from fastapi import FastAPI


app = FastAPI()


@app.get("/query")
async def query(url: str):
    # http://127.0.0.1:8000/docs#/default/query_query_get
    print("new query:  {}".format(url))
    response = ""
    async with aiohttp.ClientSession() as client:
        try:
            async with client.get(url) as resp:
                response = await resp.json()
                async with aiof.open("export.json", "w") as out:
                    await out.write(json.dumps(response))
                    await out.flush()
        except ClientConnectorError as ex:
            print("exception: {}".format(ex))
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
