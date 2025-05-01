# llm-knowledge-harvester
A personalized AI agent system that curates, summarizes, and ranks articles based on your interests.


🚀 Project Vision
This project is a modular, agent-based system that:
- Finds new articles and papers from selected sources
- Summarizes them concisely
- Scores their relevance based on your preferences
- Filters out low-quality or off-topic content
- Builds and sends you a personalized reading list or newsletter
- Learns from your feedback over time
- Agents are powered by LLMs, coordinated in a multi-agent pipeline, and built using structured Pydantic models.


##  🧩 Roadmap & Milestones
### ✅ 1. Article Fetch & Summarize: 
Basic tool that pulls articles from RSS/Arxiv and summarizes them using an LLM.

### ✅ 2. Relevance Scoring Agent
Add a relevance scoring step that ranks articles by a user’s interests.

### ✅ 3. Multi-Agent Pipeline
Split the processing into distinct agents:
- Summarizer
- Scorer
- Quality Critic

### ✅ 4. Personalized Filtering
Introduce a UserProfile that defines topics, tone, and reading preferences to steer agents' behavior.

### ✅ 5. Feedback Loop
Let users rate articles and adapt recommendations based on past feedback.

### ✅ 6. Auto-Generated Newsletter
Assemble top articles weekly into a polished Markdown/HTML newsletter.

### ✅ 7. Conversational Reader Agent
Enable question-answering over your personal reading archive with a chatbot interface.