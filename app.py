import customtkinter as ctk
from tools import TOOLS
from langchain.agents import initialize_agent, AgentType
from model_setup import load_llm
from memory import get_memory, should_use_memory
from langchain.prompts import PromptTemplate

llm = load_llm()

# GUI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("600x500")
app.title("Windows Control Bot")

chat_display = ctk.CTkTextbox(app, width=580, height=380, font=("Arial", 14))
chat_display.pack(pady=10)

user_input = ctk.CTkEntry(app, width=580, font=("Arial", 14))
user_input.pack(pady=10)

# Custom prompt to enforce ReAct format
REACT_PROMPT = """
You are a helpful assistant that controls Windows system settings like volume and brightness. Answer the user's query by reasoning through the steps and using the provided tools when necessary. If the query is vague (e.g., "decrease volume"), assume a default change of 10% (increase or decrease based on context).

Format your response as follows:
Thought: [Your reasoning about what to do]
Action: [The tool to use and its input, e.g., set_volume(10)]
Observation: [The result of the action]

If no tool is needed, provide the final answer directly:
Final Answer: [Your response]

Tools available: set_volume(value), set_brightness(value)
Query: {input}
"""

def handle_input():
    query = user_input.get()
    user_input.delete(0, ctk.END)
    chat_display.insert(ctk.END, f"You: {query}\n")

    try:
        memory = get_memory()
        if should_use_memory():
            memory.save_context({"input": query}, {"output": ""})

        # Initialize agent with memory and custom prompt
        agent = initialize_agent(
            tools=TOOLS,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Revert for robust tool handling
            verbose=True,
            handle_parsing_errors=True,
            memory=memory,
            agent_kwargs={"prompt": PromptTemplate.from_template(REACT_PROMPT)}
        )

        # Pass query as a dictionary with 'input' key
        result = agent.run({"input": query})
        chat_display.insert(ctk.END, f"Bot: {result}\n\n")
        memory.save_context({"input": query}, {"output": result})

    except Exception as e:
        chat_display.insert(ctk.END, f"Bot Error: {e}\n\n")

    chat_display.see(ctk.END)

send_btn = ctk.CTkButton(app, text="Send", command=handle_input)
send_btn.pack(pady=10)

app.mainloop()