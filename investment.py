import streamlit as st
import os

st.set_page_config(
    page_title="Investment AI Assistant",
    page_icon="📊",
    layout="centered"
)

DISCLAIMER = "⚠️ Educational purposes only. This is NOT financial advice."


def is_investment_advice(query: str) -> bool:
    blocked = [
        "which stock should i buy",
        "best stock",
        "buy or sell",
        "intraday",
        "tomorrow market",
        "guaranteed returns",
        "should i invest",
        "give me stock tips",
    ]
    q = query.lower()
    return any(b in q for b in blocked)



INVESTMENT_COACH_PROMPT = """
You are an Investment Coach (Teacher Persona).

Rules:
- You ONLY explain investing concepts.
- You NEVER give stock recommendations.
- You NEVER say buy, sell, or hold.

If the user asks for advice:
- Politely refuse
- Explain this is educational only
- Redirect to how investors generally evaluate investments

Tone: Calm, educational, beginner-friendly.
"""

MARKET_COMMENTARY_PROMPT = """
You are a Market Commentary Assistant (News Persona).

Rules:
- Summarize and explain market news neutrally
- Explain why markets moved (macro, earnings, rates)
- NO predictions
- NO recommendations

Tone: Neutral, factual, journalist-style.
"""


MARKET_NEWS = [
    {
        "headline": "Indian markets decline amid global uncertainty",
        "detail": "Markets fell due to weak global cues and concerns around interest rate hikes by central banks."
    },
    {
        "headline": "IT stocks under pressure",
        "detail": "IT stocks declined after cautious revenue outlooks from global technology companies."
    }
]


from groq import Groq

# Initialize Groq client (expects GROQ_API_KEY in environment)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_groq(system_prompt: str, user_input: str) -> str:
    """Call Groq LLM with system + user prompt"""
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ],
        temperature=0.4,
    )
    return chat_completion.choices[0].message.content


def investment_coach_response(user_input: str) -> str:
    if is_investment_advice(user_input):
        return (
            "I can’t help with specific investment advice or stock recommendations. "
            "However, I can explain how investors generally approach decision-making, "
            "such as understanding risk, diversification, and long-term goals.\n\n"
            + DISCLAIMER
        )

    response = call_groq(INVESTMENT_COACH_PROMPT, user_input)
    return response + "\n\n" + DISCLAIMER


def market_commentary_response(user_input: str) -> str:
    news_context = "\n".join(
        [f"{n['headline']}: {n['detail']}" for n in MARKET_NEWS]
    )

    combined_prompt = (
        f"Recent market news:\n{news_context}\n\n"
        f"User question: {user_input}"
    )

    response = call_groq(MARKET_COMMENTARY_PROMPT, combined_prompt)
    return response + "\n\n" + DISCLAIMER

# ================================
# Streamlit UI
# ================================

st.title("📊 Investment AI Assistant")
st.caption("Learn investing concepts and understand markets — safely")

mode = st.selectbox(
    "Select mode",
    [
        "Investment Coach (Learn Concepts)",
        "Market Commentary (Market News)"
    ]
)

if "chat" not in st.session_state:
    st.session_state.chat = []

# Show chat history
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_query = st.chat_input("Ask your question...")

if user_query:
    st.session_state.chat.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        if mode.startswith("Investment"):
            answer = investment_coach_response(user_query)
        else:
            answer = market_commentary_response(user_query)

        st.markdown(answer)

    st.session_state.chat.append({"role": "assistant", "content": answer})
