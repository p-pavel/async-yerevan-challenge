import asyncio
from config import load_yaml_to_env
import aiohttp
import os

async def make_a_call(session, url):
    """
    Call to url
    """
    try:
        async with session.get(url) as response:
            return await response.json()
        
    except aiohttp.ClientError as error: 
        print(f'Client error {url},{error}')
    except asyncio.TimeoutError:
        print(f'Request timeour {url}')
    except Exception as error:
        print(f'An error occured {url}, {error}')


async def main(urls):
    """
    Takes a list of urls

    Adds calls to the list of tasks. 
    Executes the tasks
    """
    tasks = []
    async with aiohttp.ClientSession() as session: 
        for url in urls:
            tasks.append(make_a_call(session,url))
        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    load_yaml_to_env('config.yaml')

    url1=os.environ["endpoint1"]
    url2=os.environ["endpoint2"]
    url3=os.environ["endpoint3"]
    urls = [url1,url2, url3]
    print(urls)
    result = asyncio.run(main(urls))
    print(result)