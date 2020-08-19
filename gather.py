import asyncio

async def delayedPrint(delay, text):
    i = 0
    while(i<5):
        await asyncio.sleep(delay)
        print(text)
        i+=1

async def main():
    await asyncio.gather(delayedPrint(2, "First"),delayedPrint(2, "Second"))

asyncio.run(main())
