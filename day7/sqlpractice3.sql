use student;
create table Sales_data(
		Product varchar(50),
        Price int ,
        Date DATE,
        City char(49)
        );
 insert into Sales_data
  VALUES
  ('Chairs',8000,'2026-02-25','Jhalawar'),
  ('Table',5000,'2026-02-26','Kota');
SELECT product, SUM(price)
FROM sales_data
GROUP BY product
ORDER BY SUM(price) DESC;
        
        