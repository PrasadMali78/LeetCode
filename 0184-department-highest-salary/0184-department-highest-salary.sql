select d.name Department,e.name Employee,e.salary Salary
from employee e inner join department d
on e.departmentid =  d.id 
where(e.departmentid,e.salary) in (select departmentid,max(salary) 
                                  from employee
                                  group by departmentid);