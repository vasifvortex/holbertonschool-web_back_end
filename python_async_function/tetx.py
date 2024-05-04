import asyncio

async def delay_function(delay):
    await asyncio.sleep(delay)
    return delay

async def main():
    delays = [1, 2, 3, 4, 5]

    # Sequential execution
    results_sequential = []
    for delay in delays:
        result = await delay_function(delay)
        results_sequential.append(result)
    print(results_sequential)

    # Concurrent execution using asyncio.as_completed
    results_concurrent = []
    tasks = [delay_function(delay) for delay in delays]
    for task in asyncio.as_completed(tasks):
        result = await task
        results_concurrent.append(result)
    print(results_concurrent)

asyncio.run(main())