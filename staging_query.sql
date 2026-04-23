CREATE USER IF NOT EXISTS etl_user@wwi_staging identified by 'etl_password';
GRANT CREATE, INSERT, UPDATE, DELETE on wwi_staging.* TO 'etl_user'@wwi_staging;
GRANT SELECT ON wwi_staging.* TO 'etl_user'@wwi_staging;
FLUSH PRIVILEGES;