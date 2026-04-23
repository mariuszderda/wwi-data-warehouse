CREATE USER IF NOT EXISTS 'etl_user'@'%' identified by 'etl_password';
GRANT SELECT ON wwi.* TO 'etl_user'@'%';
FLUSH PRIVILEGES;