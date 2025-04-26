"""Simple agent with only one func"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from config import OPENAI_KEY
from tools import simple_calculator

llm = ChatOpenAI(temperature=0)



tools = [
    Tool(
        name="Calculator",
        func=simple_calculator,
        description="Используй для простых математических вычислений.\
            Вводи выражение как строку, напирмер '2 + 2' или '3 * (5 + 7)"
    ),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.run('Сколько будет тридцать-3 + семь * пятнадцат тыщ?')
print('Ответ агента: ', response)
