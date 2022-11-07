from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/workspaces/P3_Fangting/intro-ai-339107-6293cf5281e8.json')

project_id = 'intro-ai-339107'
client = bigquery.Client(credentials=credentials, project=project_id)

def query_year_sales():
    QUERY = ("""
        select release_year, round(sum(sales), 2) as total_sales
        from `game_sales.game_sales`
        group by release_year
        order by release_year desc;
    """)
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    print("query 1:")
    print("total sales of video game in each year")
    print("year, total sales")
    for row in rows:
        print(row.release_year, row.total_sales)

def query_genre_sales():
    QUERY = ("""
        select genre, round(sum(sales), 2) as total_sales
        from `game_sales.game_sales`
        group by genre
        order by total_sales desc;
    """)
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    print("\nquery 2:")
    print("total sales of video game of different genres")
    print("genre, total sales")
    for row in rows:
        print(row.genre, row.total_sales)

def query_region_sales():
    QUERY = ("""
        select region, round(sum(sales), 2) as total_sales
        from `game_sales.game_sales`
        group by region
        order by total_sales desc;
    """)
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    print("\nquery 3:")
    print("total sales of video game in different regions")
    print("region, total sales")
    for row in rows:
        print(row.region, row.total_sales)

query_year_sales()
query_genre_sales()
query_region_sales()