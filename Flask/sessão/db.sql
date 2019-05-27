CREATE TABLE "funcionario" (
    "nome" varchar(100) NOT NULL,
    "codigo" serial,
    "login" varchar(100) NOT NULL,
    "pass" int NOT NULL,
    "admin" bit NOT NULL,
    "coddepartamento" int,
    CONSTRAINT "funcionarioPK" PRIMARY KEY ("codigo")
);


INSERT INTO "funcionario" ("nome", "coddepartamento", "login", "pass", "admin") VALUES ('Alan', 2, 'doidao', '12345', '0');

drop table funcionario
select * from funcionario