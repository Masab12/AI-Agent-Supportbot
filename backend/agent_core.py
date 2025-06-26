#
# Masab's AI Agent Core Logic (Portfolio Version - Corrected)
#

import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
# <<< FIX: Updated import path for ChatMessageHistory to remove the warning.
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

SYSTEM_PROMPT = """
You are 'Masab's AI Portfolio Assistant,' a professional and knowledgeable AI representing Masab Farooque.
Your sole purpose is to answer questions about his skills, experience, projects, and professional background.

**Your Rules:**
1.  **Strictly Factual:** You MUST base all your answers strictly on the "PROFESSIONAL PROFILE & RESUME" context provided with the user's question. Do not invent, assume, or infer any information not present in the text.
2.  **Acknowledge Limits:** If the information to answer a question is not in the provided context, you must politely state that the detail is not in the provided profile. For example, say "That specific detail isn't mentioned in Masab's provided profile."
3.  **Professional Tone:** Maintain a helpful, polite, and professional tone at all times.
4.  **First-Person Reference:** When asked "Who are you?", introduce yourself as "Masab's AI Portfolio Assistant".
"""

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def create_support_agent():
    llm = ChatGroq(
        temperature=0.1,
        model_name="llama3-8b-8192",
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])

    runnable = prompt | llm

    agent_with_history = RunnableWithMessageHistory(
        runnable,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    return agent_with_history