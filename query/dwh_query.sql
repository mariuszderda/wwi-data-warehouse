GRANT INDEX ON wwi_dwh.* TO 'etl_user'@'%';
FLUSH PRIVILEGES;

create index dim_customer_customer_key_index on dim_customer (CustomerID);