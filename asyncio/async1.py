import asyncio
import time
from requests import async

# async def count():
#     print("One")
#     time.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")

def get_data(id, url):
    pass

def main():
    urls = [
        (1, 'https://api.github.com/users/anunayasri'),
        (2, 'https://api.github.com/users/rizwan29'),
        (3, 'https://api.github.com/users/praveenjharbade'),
    ]

    for item in urls:
        id, url = item
        get_data(id, url)

    print("Done!!")

if __name__ == "__main__":
   s = time.perf_counter()
   elapsed = time.perf_counter() - s
   print(f"{__file__} executed in {elapsed:0.2f} seconds.")