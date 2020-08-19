import asyncio

async def sample(delay, text):
    i = 0
    while(i<5):
        await asyncio.sleep(delay)
        print(text)
        i+=1

async def main():
    await sample(2, "Hello")
    await sample(2, "World")

asyncio.run(main())