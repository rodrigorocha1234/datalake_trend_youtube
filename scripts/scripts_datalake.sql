USE hive;


CREATE SCHEMA hive.bronze2
WITH (
    location = 's3a://bronzed/'
);

select 1

select current_timestamp;
drop table hive.bronze.youtube_videos;

CREATE TABLE hive.bronze.youtube_videos(
    kind VARCHAR,
    etag VARCHAR,
    id VARCHAR,

    snippet ROW(
        publishedAt TIMESTAMP,
        channelId VARCHAR,
        title VARCHAR,
        description VARCHAR,
        channelTitle VARCHAR,
        tags ARRAY(VARCHAR),
        categoryId VARCHAR,
        liveBroadcastContent VARCHAR,
        defaultLanguage VARCHAR,
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

    status ROW(
        uploadStatus VARCHAR,
        privacyStatus VARCHAR,
        license VARCHAR,
        embeddable BOOLEAN,
        publicStatsViewable BOOLEAN,
        madeForKids BOOLEAN
    ),

    statistics ROW(
        viewCount BIGINT,
        likeCount BIGINT,
        favoriteCount BIGINT,
        commentCount BIGINT
    ),

    topicDetails ROW(
        topicCategories ARRAY(VARCHAR)
    )
)
WITH (
    format = 'PARQUET',
    external_location = 's3a://bronze/youtube_videos/',
    partitioned_by = ARRAY['dt']
);

CREATE TABLE hive.bronze.youtube_videos (
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
        )
    ),

    dt VARCHAR
)
WITH (
    format = 'PARQUET',
    external_location = 's3a://bronze/youtube_videos/',
    partitioned_by = ARRAY['dt']
);
