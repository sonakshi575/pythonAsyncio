import asyncio


async def delayedPrint(delay, text):
    i = 0
    while(i < 5):
        await asyncio.sleep(delay)
        print(text)
        i += 1


async def main():
    task1 = asyncio.create_task(delayedPrint(2, "First"))
    task2 = asyncio.create_task(delayedPrint(2, "Second"))

    await task1
    await task2

asyncio.run(main())
