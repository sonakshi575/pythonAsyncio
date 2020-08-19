import asyncio

async def sample(delay, text):
    i = 0
    while(i<5):
        await asyncio.sleep(delay)
        print(text)
        i+=1

async def main():
    task1=asyncio.create_task(sample(2, "Hello"))
    task2=asyncio.create_task(sample(2, "World"))

    await task1
    await task2

asyncio.run(main())