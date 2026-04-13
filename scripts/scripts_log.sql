-- Create a new database called 'YOUTUBE_DATALAKE_LOG'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT [name]
        FROM sys.databases
        WHERE [name] = N'YOUTUBE_DATALAKE_LOG'
)
CREATE DATABASE YOUTUBE_DATALAKE_LOG
GO



DROP TABLE log_aplicacao;

CREATE TABLE [log_aplicacao] (
    [timestamp] DATETIME2 NOT NULL,
    [level_log] VARCHAR(50) NOT NULL CHECK ([level_log] IN ('DEBUG', 'INFO', 'ERROR', 'WARNING', 'CRITICAL')),
    
    [message] NVARCHAR(MAX) NOT NULL,
    [logger_name] VARCHAR(100) NOT NULL,
    [filename] VARCHAR(255) NOT NULL,
    [func_name] VARCHAR(100) NOT NULL,
    [line_no] INT NOT NULL,
    
    [url] VARCHAR(500) NULL,
    [mensagem_de_excecao_tecnica] NVARCHAR(MAX) NULL,
    [requisicao] NVARCHAR(MAX) NULL,
    [status_code] INT NULL
);

select *
FROM log_aplicacao;

TRUNCATE TABLE log_aplicacao;


INSERT INTO logs
VALUES ('2026-04-11 20:48:52', 'INFO', 'Teste', 'main_pipeline', 'main_pipeline.py', '<module>', 21, None, None, None, None);



INSERT INTO logs

VALUE