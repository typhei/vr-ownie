import os
import psycopg2
import urlparse


def main():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port)

    cur = conn.cursor()
    db_data = list(cur.execute("SELECT url FROM pages;"))
    print db_data


if __name__ == "__main__":
    main()
