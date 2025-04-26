"""Agent with two functions and chat memory!"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from config import OPENAI_KEY
from tools import simple_calculator, fake_search


llm = ChatOpenAI(temperature=0)

tools = [
    Tool(
        name='Calculator',
        func=simple_calculator,
        description="Используй для простых математических вычислений.\
            Вводи выражение как строку, напирмер '2 + 2' или '3 * (5 + 7)"
    ),
    Tool(
        name='Search',
        func=fake_search,
        description="Используется для поиска информации в интернете.\
            Опиши, что найти."
    ),
]

memory = ConversationBufferMemory(memory_key='chat_history',
                                  return_messages=True)


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

print(agent.run('Сколько будет 2 в степени 3 в лгрфьме четырёх??'))
print(agent.run('Кто стал президентом США в 2024 году? на выборах'))
print(agent.run('Какой был 1ый вопрос кстати?'))
