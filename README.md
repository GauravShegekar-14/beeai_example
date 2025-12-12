📦 Requirements

Python 3.10+
Ollama installed → https://ollama.com/download
Model pulled: ollama pull granite3.3:8b


🛠️ Setup Instructions
✅ Step 1 — Create a new project folder
mkdir beeai-python-demo
cd beeai-python-demo

✅ Step 2 — Create & activate a virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

✅ Step 3 — Install BeeAI Framework
pip install beeai-framework

✅ Step 4 — Create the Python agent file

Create:
price_agent.py

✅ Step 5 
add given code in  price_agent.py

✅ Step 6 — Run the agent
python price_agent.py


In terminal You will see:
Enter your question:


Try asking:

🔥 examples PROMPTS TO TEST ThinkTool

ThinkTool is usually meant for deep reasoning, chain-of-thought, planning, and multi-step logic.

✅ Basic Reasoning

1)“Think step-by-step and explain how you would plan a 3-day India trip under ₹15,000.”
2)“Think through the logic and tell me if it’s cheaper to build my own backend or use Firebase.”
3)“Think carefully: If I increase my marketplace commission from 10% to 18%, how will it affect vendor earnings?”
4)“Think step-by-step: How can I scale my pizza delivery app to 1 lakh users with minimum cost?”
5)“Think like an architect and design a TypeScript backend folder structure for a marketplace like Urban Company.”
6)“Think in depth and explain why TypeScript reduces bugs in large backend systems.”
7)“Think logically and compare Redis vs MongoDB for caching real-time data.”


🌤️ Example PROMPTS TO TEST OpenMeteoTool (Weather Tool)

This tool responds when you ask for weather, temperature, forecast, wind, humidity, air quality, etc.

✅ Simple Weather Check

1)“Give me current weather in Ahmedabad.”
2)“Check temperature and humidity in Mumbai right now.”
3)“What’s the 7-day weather forecast for Delhi?”
4)“What is the rainfall prediction for Bangalore tomorrow?”
5)“Compare the next 3 days’ temperature of Surat and Vadodara.”
6)“Tell me if there is a chance of storm or heavy wind in Chennai in the next 48 hours.”
7)“Get the hourly temperature trend for Jaipur for the next 24 hours.”
8)“Show me sunrise and sunset timing for Kolkata today.”
9)“Check air quality index (AQI) for Pune right now.”
10)“Give me weather alerts for Uttarakhand mountains in the next 2 days.”

