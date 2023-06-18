import asyncio
from listing_2_6_delay_functions import delay


async def hello_every_seconds():
    for i in range(2):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting...")


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_seconds()
    await first_delay
    await second_delay


asyncio.run(main())
