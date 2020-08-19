import asyncio


async def delayedPrint(delay, text):
    i = 0
    while(i < 5):
        await asyncio.sleep(delay)
        print(text)
        i += 1


async def main():
    await delayedPrint(2, "First")
    await delayedPrint(2, "Second")

asyncio.run(main())
