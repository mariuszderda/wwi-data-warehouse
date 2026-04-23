CREATE USER IF NOT EXISTS 'etl_user'@'%' identified by 'etl_password';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, INDEX  ON wwi_staging.* TO 'etl_user'@'%';
FLUSH PRIVILEGES;