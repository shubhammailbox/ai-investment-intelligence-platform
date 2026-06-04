# AI Investment Intelligence Platform

## Overview

The **AI Investment Intelligence Platform** is a data-driven system designed to help long-term investors make informed investment decisions by analyzing financial data, corporate earnings commentary, and market narratives.

Unlike traditional stock screeners or trading tools, this platform focuses on **investment intelligence**, helping investors understand broader market signals, corporate sentiment, and macro narratives that influence long-term investment outcomes.

The platform leverages **AI, data engineering pipelines, and modern cloud infrastructure** to transform raw financial data into actionable insights for investors.

---

## Problem Statement

Retail investors face several challenges when making investment decisions:

* Information overload from earnings reports, research notes, and financial news
* Noise from social media influencers and biased investment advice
* Lack of structured tools to analyze corporate commentary and macro narratives

The AI Investment Intelligence Platform addresses these problems by using **AI-powered analysis to extract meaningful signals from financial data sources**.

---

## Core Modules

### 1. Earnings Call Intelligence Engine

Analyzes corporate earnings call transcripts and extracts insights related to:

* Management confidence
* Growth opportunities
* Strategic priorities
* Risk factors

Example Output:

* Company: Infosys
* Confidence Score: High
* Key Themes: AI services expansion, cloud transformation demand
* Risk Signals: Currency volatility

---

### 2. Market Narrative Tracker

Identifies dominant **market narratives** by analyzing financial news, earnings transcripts, and research commentary.

Example Narratives:

* AI technology boom
* Interest rate cycle
* Energy transition
* Global economic slowdown

This module helps investors understand **which themes are driving market sentiment**.

---

### 3. Investment Timing Indicator

Helps investors evaluate whether current market conditions are favorable for long-term investment.

The system analyzes:

* Market valuations
* Historical drawdowns
* Macro indicators
* Sentiment indicators

Example Output:

* Market Valuation: Fair
* Long-term investment outlook: Favorable

---

## High-Level Architecture

Financial Knowledge Base
        ↓
OpenAI Embeddings
        ↓
FAISS Vector Store
        ↓
RAG Pipeline
        ↓
LangSmith Tracing
        ↓
RAGAS Evaluation
        ↓
LangGraph Workflow
        ↓
Conditional Routing


## Low level Architecture

User Query
     │
     ▼
LangGraph Router
     │
 ┌───┴────┐
 ▼        ▼
ETF     RAG
Path    Path
         │
         ▼
    FAISS Vector Store
         │
         ▼
    OpenAI LLM
         │
         ▼
     Response

Observability:
LangSmith

Evaluation:
RAGAS

## Current Features 

✓ Financial Knowledge Base
✓ Semantic Search using FAISS
✓ Retrieval Augmented Generation (RAG)
✓ LangSmith Observability
✓ RAGAS Evaluation
✓ LangGraph Workflows
✓ Conditional Routing
✓ ETF Query Routing

## Technology Stack

Python
OpenAI
LangChain
LangGraph
FAISS
RAGAS
LangSmith
AWS (Upcoming)
Bedrock (Upcoming)

## Current Agent Workflow

Current LangGraph Workflow

START
  ↓
Router Node
  ↓
 ┌──────────────┬──────────────┐
 ▼              ▼
ETF Path      RAG Path
 ↓              ↓
END         Retrieve Docs
                 ↓
           Generate Answer
                 ↓
                END


## Project Goals

* Build an AI-powered platform for investment intelligence
* Apply modern data engineering techniques on financial datasets
* Extract signals from earnings transcripts and financial narratives
* Provide investors with objective decision-support insights


## Repository Structure

ai_models/
├── agents/
│   └── langgraph/
│       ├── state.py
│       ├── nodes.py
│       ├── financial_graph.py
│       └── run_graph.py
│
├── rag/
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── rag_pipeline.py
│   ├── test_rag.py
│   └── evaluation/
│       └── evaluate_rag.py
│
analytics/
│   ├── earnings_pipeline.py
data/
│   ├── investors_principles_structured.json
data_ingestion/
│   ├── earnings_calls_pipeline.py


## AI Engineering Capabilities Demonstrated

✓ Retrieval Augmented Generation (RAG)
✓ Vector Databases (FAISS)
✓ Embeddings
✓ LangGraph Workflow Orchestration
✓ Conditional Routing
✓ Observability (LangSmith)
✓ Evaluation Frameworks (RAGAS)
✓ Modular AI System Design
✓ Environment-Based Configuration


## Road Map & Future Vision

Completed
---------
✓ RAG Pipeline
✓ LangSmith
✓ RAGAS
✓ LangGraph
✓ Conditional Routing

Upcoming
---------
□ Tool Calling
□ Yahoo Finance Integration
□ Multi-Agent Architecture
□ FastAPI
□ Docker
□ AWS ECS/Fargate
□ AWS Bedrock
□ Production Deployment

The long-term vision is to build a **comprehensive AI-powered investment research platform** that helps investors analyze corporate commentary, market narratives, and macro signals to make more informed long-term investment decisions.

---

## Installation

```bash
git clone <repo>
cd ai-investment-intelligence-platform

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
```


## Author

Shubham Mishra
Principal Engineer – AI, Cloud & Data Platforms
FinTech | Data Systems | AI-driven Financial Intelligence
