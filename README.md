# 🌟 Gemini SQL Query

This project is a Streamlit-powered web app that converts natural language questions into SQL queries using the Gemini API. It then executes those queries on an SQLite database containing student data and displays the results.

## 🚀 Features

- Convert English questions to SQL queries using the Gemini API.
- Execute SQL queries on a pre-populated `STUDENT` SQLite database.
- User-friendly interface built with Streamlit.

## 📦 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/Nanashi-bot/gemini_sql_query.git
cd gemini_sql_query
```

2. **Create a Virtual Environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

3. **Install Required Packages:**
```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables:**

Create a `.env` file in the root directory and add your Gemini API key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## ⚙️ Usage

1. **Run the Streamlit App:**
```bash
streamlit run app.py
```

2. **Ask SQL-related Questions:**

- *Example 1:* How many students are there?  
- *Example 2:* Show me all students in the Physics class.  
- *Example 3:* Who scored more than 90 marks?  

The app will convert your query into SQL and execute it on the `student.db` SQLite database.

## 🗄️ Database Structure

The SQLite database `student.db` contains a table named `STUDENT` with the following columns:

| **Column Name** | **Data Type** |
|-----------------|---------------|
| NAME            | VARCHAR(25)   |
| CLASS           | VARCHAR(25)   |
| SECTION         | VARCHAR(25)   |
| MARKS           | INTEGER       |

## 🔑 Example Queries

1. **Input:** How many students are in the database?  
**Output:** `SELECT COUNT(*) FROM STUDENT;`

2. **Input:** List all students in the Computer Science class.  
**Output:** `SELECT * FROM STUDENT WHERE CLASS="Computer Science";`

3. **Input:** Who scored more than 85 marks?  
**Output:** `SELECT * FROM STUDENT WHERE MARKS > 85;`

## 📝 License

This project is open-source and provided under the **MIT License**.  
Feel free to use, modify, and distribute the code. See the [MIT License](https://opensource.org/licenses/MIT) for more details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.
