create Procedure emp_dynamic
@dept_id varchar(10)='d007'
WITH ENCRYPTION
as
begin
select * from new_table where new_table.dept_no=@dept_id;
END

EXEC emp_dynamic
sp_helptext emp_dynamic
