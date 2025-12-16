from fastapi import FastAPI
from db import get_db_connection

app = FastAPI()

@app.get("/revenue-summary")
def revenue_summary():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT billing_status,
               SUM(billing_numbers) AS revenue
        FROM cops_billing_details
        GROUP BY billing_status;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    total = sum(row["revenue"] for row in rows)

    return {
        "status_wise_revenue": rows,
        "grand_total_revenue": total
    }
