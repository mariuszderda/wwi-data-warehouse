from sqlalchemy import text
import pandas as pd

from config import get_staging_engine, get_source_engine, get_dwh_engine

# create engine
source_engine = get_source_engine()
staging_engine = get_staging_engine()
dwh_engine = get_dwh_engine()

# source query
source_customer_query = """
                        SELECT CustomerID
                             , CustomerCategoryID
                             , BuyingGroupID
                             , PrimaryContactPersonID
                             , DeliveryMethodID
                             , DeliveryCityID
                             , PostalCityID
                             , AccountOpenedDate
                             , StandardDiscountPercentage
                             , ValidFrom
                             , ValidTo
                        FROM customers;
                        """

source_category_query = """
                        SELECT CustomerCategoryID
                             , CustomerCategoryName
                        FROM customercategories;
                        """

source_buyinggroups_query = """
                            SELECT BuyingGroupID,
                                   BuyingGroupName
                            FROM buyinggroups;
                            """

# save to staging
source_customer_df = pd.read_sql(source_customer_query, source_engine)
source_customer_df.to_sql('customers', con=staging_engine, index=False, if_exists='replace')

source_category_df = pd.read_sql(source_category_query, source_engine)
source_category_df.to_sql('customercategories', con=staging_engine, index=False, if_exists='replace')

source_buyinggroups_df = pd.read_sql(source_buyinggroups_query, source_engine)
source_buyinggroups_df.to_sql('buyinggroups', con=staging_engine, index=False, if_exists='replace')

staging_query = """
                SELECT c.CustomerID
                     , c.CustomerCategoryID
                     , cc.CustomerCategoryName
                     , coalesce(c.BuyingGroupID, -1)                              as BuyingGroupID
                     , coalesce(b.BuyingGroupName, "Unknown")                     as BuyingGroupName
                     , c.PrimaryContactPersonID
                     , c.DeliveryMethodID
                     , c.DeliveryCityID
                     , c.PostalCityID
                     , c.AccountOpenedDate
                     , c.StandardDiscountPercentage
                     , c.ValidFrom
                     , REPLACE(c.ValidTo, DATE('0000-00-00'), DATE('9999-12-31')) as ValidTo
                     , CASE
                           WHEN c.ValidTo = DATE('0000-00-00') THEN 1
                           ELSE 0
                    END                                                           as isCurrent
                FROM customers AS c
                         JOIN customercategories AS cc ON c.CustomerCategoryID = cc.CustomerCategoryID
                         LEFT JOIN buyinggroups AS b ON b.BuyingGroupID = c.BuyingGroupID;
                """

staging_df = pd.read_sql(staging_query, staging_engine)
staging_df.to_sql('dim_customer', con=dwh_engine, if_exists='replace', index=False)

with dwh_engine.connect() as conn:
    res = conn.execute(text("create index if not exists dim_customer_customer_key_index on dim_customer (CustomerID);"))
    print("Index on customer key - created.")
    conn.commit()