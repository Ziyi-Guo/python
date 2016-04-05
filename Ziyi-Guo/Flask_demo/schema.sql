drop table if exists Message;
create table Message (
	id integer primary key autoincrement,
	name text not null,
	comment text not null,
	time text not null);