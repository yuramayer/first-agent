from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
import os
from table_manager import TableManager


def create_agent():

    table_manager = TableManager()

    tools = [
        Tool(
            name="LoadTable",
            func=table_manager.load_table_from_text,
            description="Загружает таблицу из CSV-текста. \
                Передавай весь текст таблицы."
        ),
        Tool(
            name="FindMostFrequent",
            func=table_manager.find_most_frequent,
            description="Находит самые частые элементы в указанной колонке. \
                Укажи имя колонки."
        )
    ]

    llm = ChatOpenAI(temperature=0)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    return agent
