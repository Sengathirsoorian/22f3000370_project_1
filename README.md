
# Project Title: 22f3000370_project_1 - Automation Agent for DataWorks Solutions


## Description

This project involves the automation of operations tasks using an API and an LLM-based automation agent. The goal is to simplify and automate various operational tasks such as file formatting, data extraction, API interactions, SQL queries, and more through a seamless interface.

### Key Features
- **API Endpoints**: 
  - `/run`: Executes operations or tasks.
  - `/read`: Retrieves status or results of the operation.
- **LLM Integration**: Leveraging a Language Model to interpret and execute tasks like business operations and API calls.
- **Data Security**: Strict constraints on data access, ensuring no access outside `/data` and preventing deletions.
- **Task Automation**: Supports a variety of automation tasks like file formatting, database queries, git operations, and more.

## Project Setup

### Prerequisites

1. Docker
2. Python 3.11
3. Required Python libraries (installed via `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/22f3000370_project_1.git
   cd 22f3000370_project_1
   ```

2. Build and run the Docker container:

   ```bash
   docker-compose up --build
   ```

3. Access the API through `localhost:<port>` (replace `<port>` with your actual port number).

### API Usage

AI Proxy only supports these endpoints and models:

- GET https://aiproxy.sanand.workers.dev/openai/v1/models
- POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings
model: text-embedding-3-small
- POST https://aiproxy.sanand.workers.dev/openai/v1/chat/completions
model: gpt-4o-mini
It returns a set of additional headers:

- cost: Cost of this request in USD
- monthlyCost: Total costs (in USD) of requests used this month. Monthly limit is $0.5 (resets at midnight UTC on the first of the next month).
- monthlyRequests: Total requests made this month.

## Skills & Technologies Used

- **Languages**: Python 3.11
- **Framework**: Flask (for the backend)
- **Docker**: For containerization and deployment
- **APIs**: RESTful API development
- **LLM Integration**: Language Model for task interpretation
- **SQL**: Database query handling
- **Security**: Data access restrictions

## Deployment

- This project is deployed using Docker. The image can also be published on Docker Hub for easy access.

## Contribution

Feel free to fork the repository, submit issues, or create pull requests.

## License

MIT License © [Sengathirsoorian](https://github.com/Sengathirsoorian)

