DROP DATABASE IF EXISTS collision_insight;
CREATE DATABASE collision_insight;

DROP USER IF EXISTS collision_insight;
CREATE USER collision_insight WITH PASSWORD 'collision_insight';

GRANT ALL PRIVILEGES ON SCHEMA collision_insight TO collision_insight;
GRANT ALL PRIVILEGES ON DATABASE collision_insight TO collision_insight;

ALTER USER collision_insight SET search_path = collision_insight;




