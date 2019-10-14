import websockets
import aysncio


async def hello():
	url = "www.localhost:8001"
	async with websockets.connect(url) as websockets