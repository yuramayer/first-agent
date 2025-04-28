from dotenv import load_dotenv
import os
from agent_setup import create_agent


load_dotenv(override=True)

OPENAI_KEY = str(os.getenv('OPENAI_API_KEY')) 


agent = create_agent()


csv_text = """name,city
Alice,Paris
Bob,London
Alice,Paris
Charlie,Paris
Bob,Berlin
"""

print(agent.run(f"Загрузи эту таблицу:\n{csv_text}"))
#print(agent.run("Найди самые частые значения в колонке 'name'"))
