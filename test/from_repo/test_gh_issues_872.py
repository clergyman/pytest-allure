import pytest
import requests
import allure

from concurrent.futures import ThreadPoolExecutor
import asyncio


def session_on_node(node_id, session):
    with allure.step(f"Session#{session} on node {node_id}"):
        assert 1==2


def parallel_task_for_specific_node(node_id):
    with allure.step(f"Parallel task for node {node_id}"):
        with ThreadPoolExecutor() as executor:
            for session in range(5):
                executor.submit(session_on_node, node_id, session)

            executor.shutdown(wait=True)


def test_multithreaded():
    with allure.step("Entrance"):
        with ThreadPoolExecutor() as executor:
            for node_id in range(3):
                executor.submit(parallel_task_for_specific_node, node_id)

            executor.shutdown(wait=True)


def test_multithreaded_single_function():
    with allure.step("Entrance"):  # Top-level Allure step
        def run_for_node(node_id):
            with allure.step(f"Parallel task for node {node_id}"):
                with ThreadPoolExecutor() as session_executor:
                    for session in range(5):
                        def session_step(session=session):
                            with allure.step(f"Session#{session} on node {node_id}"):
                                pass
                        session_executor.submit(session_step)
                    session_executor.shutdown(wait=True)

        with ThreadPoolExecutor() as node_executor:
            for node_id in range(3):
                node_executor.submit(run_for_node, node_id)
            node_executor.shutdown(wait=True)


def test_multithreaded_asyncio():
    async def session_on_node_async(node_id, session):
        with allure.step(f"Session#{session} on node {node_id}"):
            await asyncio.sleep(0)  # Simulate async work

    async def parallel_task_for_node_async(node_id):
        with allure.step(f"Parallel task for node {node_id}"):
            await asyncio.gather(*[
                session_on_node_async(node_id, session)
                for session in range(5)
            ])

    async def main():
        with allure.step("Entrance"):
            await asyncio.gather(*[
                parallel_task_for_node_async(node_id)
                for node_id in range(3)
            ])

    asyncio.run(main())

@allure.step("Session#{session} on node {node_id}")
def session_step_decorated(node_id, session):
    pass

@allure.step("Parallel task for node {node_id}")
def run_for_node_decorated(node_id):
    with ThreadPoolExecutor() as session_executor:
        for session in range(5):
            session_executor.submit(session_step_decorated, node_id, session)
        session_executor.shutdown(wait=True)

@allure.step("Entrance")
def test_multithreaded_single_function_decorated():
    with ThreadPoolExecutor() as node_executor:
        for node_id in range(3):
            node_executor.submit(run_for_node_decorated, node_id)
        node_executor.shutdown(wait=True)