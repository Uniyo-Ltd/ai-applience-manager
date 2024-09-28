# AI Application Manager

## Setup Instructions

### Prerequisites
- Python 3.8+
- Git installed

### Installation
1. Clone the repository:
git clone https://github.com/yourusername/ai-applience-manager.git cd ai-applience-manager


2. Create and activate a virtual environment:
python -m venv env source env/bin/activate # On Windows, use env\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


## Run Instructions

1. Start the Django server:
python manage.py runserver

2. Access the application at x host

## Assumptions and Decisions

- Used Django and React, PostgreSQL, Typescript due to projects tech stack requirements
- Implemented basic functioalites for user access control
- Utilized PostgreSQL database for simplicity and quick development
- Prioritized functionality over advanced arch, best practices, SOLID extensibility, testing features etc

## Known Limitations

- Limited unit tests due to time constraints
- No comprehensive integration tests implemented
- Some edge cases may not be covered thoroughly

## Future Improvements


- Add C4 documentation etc
- Implement more robust testing suite
- Optimize database tables, scheme, relations, queries templates etc for improved performance
- implement Arch to prevent tech debt as team and complexity grows
- Enhance security measures and visuals 
