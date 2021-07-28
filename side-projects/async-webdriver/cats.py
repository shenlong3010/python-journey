import asyncio
import sys

from arsenic import get_session, keys, browsers, services

if sys.platform.startswith('win'):
    DRIVER = './chromedriver.exe'
else:
    DRIVER = './chromedriver'


async def hello_world():
    service = services.Chromedriver(binary=DRIVER)
    browser = browsers.Chrome()
    async with get_session(service, browser) as session:
        await session.get('https://images.google.com/')
        search_box = await session.wait_for_element(5, 'input[name=q]')
        await search_box.send_keys('Cats')
        await search_box.send_keys(keys.ENTER)
        await asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())


if __name__ == '__main__':
    main()