# Testing Remote PostgreSQL Connection

This Python script tests the connection to a remote PostgreSQL database using the `psycopg2` library. It loads the database credentials from an environment file and establishes a connection to the database. If the connection is successful, it executes a sample query to verify the connection and prints the PostgreSQL version.

## Prerequisites

- Python 3.6 or above
- `psycopg2` library (`pip install psycopg2`)
- `python-dotenv` library (`pip install python-dotenv`)

## Getting Started

1. Clone the repository or download the script file (`test_postgres_connection.py`).

2. Create a file named `.env` in the same directory as the script file.

3. Open the `.env` file and add the following lines, replacing the placeholder values with your actual database credentials:

   ```plaintext
   HOST=your_host
   PORT=your_port
   DATABASE=your_database
   USER=your_username
   PASSWORD=your_password
   ```

4. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the script using the following command:

```bash
python test_postgres_connection.py
```
