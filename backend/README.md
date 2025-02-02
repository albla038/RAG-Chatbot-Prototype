Filstruktur:

backend/
├── app/
│   ├── __init__.py
│   ├── main.py         # Entry point
│   ├── routes.py       # Routes/API endpoints
│   ├── models.py       # Pydantic models
│   ├── services.py     # Business logic for users
│   ├── config.py       # Configuration settings
│   ├── database.py     # DB connection setup
├── tests/              # Unit tests
├── requirements.txt    # Dependencies
├── README.md           # Documentation


OpenAI free API:
Med antagandet att en input är 100 tokens och en output är 300 tokens och att vi använder GPT-4o Mini som kostar

  Input: $0.15 / 1M tokens
  Output: $0.60 per

blir det totalt ca. $0.000255 per fråga.

Det blir alltså $5 / $0.000255 = 19'600 frågor och är giltigt i 3 månader.