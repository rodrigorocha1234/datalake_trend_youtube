USE hive;

select
    1;

SHOW SCHEMAS
FROM
    hive;

CREATE SCHEMA IF NOT EXISTS hive.datalake
WITH
    (location = 's3a://datalakeyoutube/');

drop schema hive.datalake;

select
    *
from
    hive.datalake.videos_bronze a;

drop table hive.datalake.videos_bronze;

SELECT
    *
FROM
    hive.datalake.videos_bronze
    ---- Deu certo 
CREATE TABLE hive.datalake.videos_bronze (
    kind VARCHAR,
    etag VARCHAR,
    id VARCHAR,
    snippet ROW(
        publishedAt VARCHAR,
        channelId VARCHAR,
        title VARCHAR,
        description VARCHAR,
        thumbnails ROW(
            "default" ROW(url VARCHAR, width INTEGER, height INTEGER),
            medium ROW(url VARCHAR, width INTEGER, height INTEGER),
            high ROW(url VARCHAR, width INTEGER, height INTEGER),
            standard ROW(url VARCHAR, width INTEGER, height INTEGER),
            maxres ROW(url VARCHAR, width INTEGER, height INTEGER)
        ),
        channelTitle VARCHAR,
        tags ARRAY(VARCHAR),
        categoryId VARCHAR,
        liveBroadcastContent VARCHAR,
        defaultLanguage VARCHAR,
        localized ROW(title VARCHAR, description VARCHAR),
        defaultAudioLanguage VARCHAR
    ),
    contentDetails ROW(
        duration VARCHAR,
        dimension VARCHAR,
        definition VARCHAR,
        caption VARCHAR,
        licensedContent BOOLEAN,
        projection VARCHAR
    ),
    "status" ROW(
        uploadStatus VARCHAR,
        privacyStatus VARCHAR,
        license VARCHAR,
        embeddable BOOLEAN,
        publicStatsViewable BOOLEAN,
        madeForKids BOOLEAN
    ),
    statistics ROW(
        viewCount VARCHAR,
        likeCount VARCHAR,
        favoriteCount VARCHAR,
        commentCount VARCHAR
    ),
    topicDetails ROW(topicCategories ARRAY(VARCHAR)),
    localizations MAP(VARCHAR, ROW(title VARCHAR, description VARCHAR)),
    ano int,
    mes int,
    dia int
)
WITH
    (
        external_location = 's3a://datalakeyoutube/youtube_trend_bronze/',
        format = 'JSON',
        partitioned_by = ARRAY['ano', 'mes', 'dia']
    );

CALL hive.system.sync_partition_metadata (
    schema_name => 'datalake',
    table_name => 'videos_bronze',
    mode => 'ADD'
);