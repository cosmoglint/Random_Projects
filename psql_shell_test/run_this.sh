psql
create database newdb;
create user myuser with password 'userpass';
grant all previlages on database newdb to myuser;
\q
psql -c "CREATE DATABASE testdb;"
psql -c "CREATE USER testuser WITH  PASSWORD 'testpass';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;"
