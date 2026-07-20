create table student
(
    student_id serial primary key,
	name varchar(100),
	course varchar(50),
	marks int
)
insert into student values(1,'Anand','MSC Data Analytics',85),(2,'Varun','MSC Physics',75),(3,'Vineeth','MTech Engineering',90);
select * from student;