from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI

# Directly assign your API key here
api_key = 

# Debug print to verify the API key is set
print(f"Retrieved API Key: {api_key}")

# Check if the API key is retrieved correctly
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI model with the API key
llm = OpenAI(temperature=0, openai_api_key=api_key)
delimiter = ';'
# Create the CSV agent
# agent = create_csv_agent(llm, r'C:\Users\Ayelet Lironne\Downloads\bank-additional-full.csv\bank-additional-full.csv',
#                          verbose=True,allow_dangerous_code=True)

csv_file_path=r'C:\Users\Ayelet Lironne\Downloads\bank-additional-full.csv\bank-additional-full.csv'
agent = create_csv_agent(
    llm,
    csv_file_path,
    verbose=True,
    allow_dangerous_code=True,
    pandas_kwargs={'delimiter': delimiter, 'encoding': 'latin1'}  # Adjust encoding if necessary
)
agent.run("what is the average age ?")
