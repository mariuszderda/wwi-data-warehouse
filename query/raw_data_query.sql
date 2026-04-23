-- select minimum and maximum date for dim dimensions
SELECT MIN(InvoiceDate)
     , MAX(InvoiceDate)
FROM invoices;

SELECT COLUMN_NAME
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'customers';

SELECT c.CustomerID
     , c.CustomerCategoryID
     , cc.CustomerCategoryName
     , c.BuyingGroupID
     , b.BuyingGroupName
     , c.PrimaryContactPersonID
     , c.DeliveryMethodID
     , c.DeliveryCityID
     , c.PostalCityID
     , c.AccountOpenedDate
     , c.StandardDiscountPercentage
FROM customers AS c
         JOIN customercategories AS cc ON c.CustomerCategoryID = cc.CustomerCategoryID
         LEFT JOIN buyinggroups AS b ON b.BuyingGroupID = c.BuyingGroupID;

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


SELECT CustomerID
     , CustomerCategoryID
     , BuyingGroupID
     , PrimaryContactPersonID
     , DeliveryMethodID
     , DeliveryCityID
     , PostalCityID
     , AccountOpenedDate
     , StandardDiscountPercentage
FROM customers;

SELECT CustomerCategoryID
     , CustomerCategoryName
FROM customercategories;

SELECT BuyingGroupID,
       BuyingGroupName
FROM buyinggroups;