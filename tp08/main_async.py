import asyncio

async def add(a,b):
    await asyncio.sleep(3)
    return a+b


async def main():
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # r = await add(5,6)
    # print(r)

    print("avant")
    all_r = [add(5,6),add(5,16),add(75,6),add(58,60)]

    print("après")
    r = await asyncio.gather(*all_r)
    print(r)
if __name__=='__main__':
    asyncio.run(main())
