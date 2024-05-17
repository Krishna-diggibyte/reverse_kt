Static
create Procedure emp_d005
As
Begin
select * from new_table where new_table.dept_no='d005';
END

EXEC emp_d005
