
CREATE SCHEMA hive.bronze
WITH (
    location = 's3a://bronze/'
);

drop schema hive.bronze;


create schema if not exists hive.bronze with (location = 's3a://bronze/');
