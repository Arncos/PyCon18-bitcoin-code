import asyncio

async def f(uid):
	await asyncio.sleep(uid ** 2)
	print (uid)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
	f(2),
	f(1)
))	
loop.close()