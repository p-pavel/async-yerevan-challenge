# async-yerevan-challenge

По итогам попыток посраться в чатике в Ереване. 

Предлагаю намутить решение задачки на любимом языке. 

Цель -- показать, как это делается (изначальный запрос: да что вы такого удобного нашли в goroutines).

Придумываем задачки, форкаем, создаем подкатолог, фигачим код. Show me the code! :)


Async demo in different languages and paradigms

ChatGPT proposed the following task: 

I need a demo task that exercise asynchronousity in different programming languages. I don't need the solution, just a task.

I have Go, Python, and Scala in mind. Can you come with some task that is suitable to demonstrate async programming in the those languages?


—— 


Certainly! Let's consider a task that involves fetching data from multiple external APIs concurrently. This task can demonstrate asynchronous programming in Go, Python, and Scala. Here's the task:
Task: Asynchronous API Data Fetching


You are tasked with creating a program that fetches data from three different external APIs concurrently. The goal is to minimize the total time taken to retrieve the data by fetching it asynchronously.

### Go:
  
 - Use Goroutines and Channels to fetch data from three different APIs concurrently.
 - You may use the net/http package for making HTTP requests.
   
### Python:
  
 - Use the asyncio library to fetch data asynchronously from three different APIs.
 - You can use the aiohttp library for making asynchronous HTTP requests.
   
### Scala:

- Use the Future and Async features in Scala to fetch data concurrently from three different APIs.
- You may use the dispatch library for making asynchronous HTTP requests.

## Requirements:

- Create a function in each language that takes a list of API endpoints and returns the fetched data.
- The program should be able to handle different types of data (e.g., JSON, XML) returned by the APIs.
- Ensure error handling for failed API requests.
- Measure and print the total time taken to fetch data from all APIs concurrently.


This task will allow you to explore and demonstrate the asynchronous capabilities of each language. Make sure to handle errors gracefully and provide clear output on the success or failure of each API request.
