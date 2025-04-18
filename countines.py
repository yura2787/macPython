from time import sleep
import asyncio

# def hello():
#     print('Hello world')
#     sleep(1)
#     print('Hello again')
#
#
# hello()


async def hello():
    print("Hello world")
    await asyncio.sleep(1)
    print("Hello again")


async def foo():
    print("From foo")
    await asyncio.sleep(1)
    print("From foo again")


# asyncio.run(hello())


async def main():
    await asyncio.gather(foo(), hello())


asyncio.run(main())
