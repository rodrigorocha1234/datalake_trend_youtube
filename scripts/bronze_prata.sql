select 
    v.snippet.categoryId as id_categoria,
    v.snippet.channelId as id_canal,
    v.snippet.channelTitle as nome_canal,
    v.id as id_video,
    v.snippet.title as nome_video,
    cast(v.statistics.viewcount as int) as total_visualizacoes,
    cast(v.statistics.likecount as int) as total_likes,
    cast(v.statistics.commentcount as int) as total_comentarios,

    CAST(date_parse(v.data_hora_insercao, '%d/%m/%Y %H:%i:%s') AS timestamp) as data_atual,

    year(current_date)  AS ano,
    month(current_date) AS mes,
    day(current_date)   AS dia
from hive.datalake.videos_bronze v
where CAST(date_parse(v.data_hora_insercao, '%d/%m/%Y %H:%i:%s') AS timestamp) >= current_date - interval '1' minute ;


select *
from hive.datalake.videos_bronze v;


select * 
 from hive.datalake.videos_bronze v;


SELECT current_timestamp;


with base as (
    select 
        v.snippet.categoryId as id_categoria,
        v.snippet.channelId as id_canal,
        v.snippet.channelTitle as nome_canal,
        v.id as id_video,
        v.snippet.title as nome_video,

        cast(v.statistics.viewcount as integer) as total_visualizacoes,
        cast(v.statistics.likecount as integer) as total_likes,
        cast(v.statistics.commentcount as integer) as total_comentarios,

        CAST(date_parse(v.data_hora_insercao, '%d/%m/%Y %H:%i:%s') AS timestamp) as data_atual,
        year(current_date)  AS ano,
	    month(current_date) AS mes,
	    day(current_date)   AS dia

    from hive.datalake.videos_bronze v
)

select *
from base
where data_atual >= current_timestamp - interval '1' day;



select *
from  hive.datalake.prata ;

drop table hive.datalake.prata ;

