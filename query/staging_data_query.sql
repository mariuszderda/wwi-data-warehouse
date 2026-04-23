use wwi_staging;

/* create index on dim_date */
create index dim_date_date_key_index on dim_date (date_key);

SELECT COUNT(*) FROM dim_date;