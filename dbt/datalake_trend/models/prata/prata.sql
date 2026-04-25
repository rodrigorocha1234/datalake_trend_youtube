{{ config(
    materialized='incremental',
    unique_key='id_video',
    properties={
        "partitioned_by": "ARRAY['ano','mes','dia', 'id_categoria', 'id_canal', 'id_video']",
        "format": "'PARQUET'"
    }
) }}

with base as (
    select


        v.snippet.channelTitle as nome_canal,

        v.snippet.title as nome_video,

        cast(v.statistics.viewcount as integer) as total_visualizacoes,
        cast(v.statistics.likecount as integer) as total_likes,
        cast(v.statistics.commentcount as integer) as total_comentarios,

        CAST(date_parse(v.data_hora_insercao, '%d/%m/%Y %H:%i:%s') AS timestamp) as data_atual,

        year(current_date)  as ano,
        month(current_date) as mes,
        day(current_date)   as dia,
        v.snippet.categoryId as id_categoria,
        v.snippet.channelId as id_canal,
        v.id as id_video

    from {{ source('bronze', 'videos_bronze') }} v
)

select *
from base

{% if is_incremental() %}
where data_atual >= current_timestamp - interval '1' minute
{% endif %}