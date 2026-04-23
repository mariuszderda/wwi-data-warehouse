use wwi_staging;

GRANT index ON wwi_staging.* TO 'etl_user'@'%';
FLUSH PRIVILEGES;

create index dim_date_date_key_index on dim_date (date_key);