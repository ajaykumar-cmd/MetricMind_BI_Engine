from dotenv import load_dotenv
load_dotenv()

import os
print("KEY:", os.getenv("GROK_API_KEY"))

from agent import ask_metricmind
import duckdb

con = duckdb.connect("metricmind.duckdb")
result = ask_metricmind("what is total revenue in Europe", con)
print(result)