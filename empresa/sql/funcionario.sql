CREATE TABLE "funcionario" (
    "nome" varchar(100) NOT NULL,
    "codigo" serial unique,
    CONSTRAINT "funcionarioPK" PRIMARY KEY ("codigo")
);


ALTER TABLE "funcionario" ADD COLUMN "coddepartamento" int

ALTER TABLE  "funcionario" ADD CONSTRAINT "funcionarioFK" FOREIGN KEY  ("coddepartamento")
	REFERENCES "departamento" ("codigo")
		ON UPDATE CASCADE
		ON DELETE NO ACTION



INSERT INTO "departamento" ("nome", "codgerente") VALUES ('Alan', 2);
INSERT INTO "funcionario" ("nome", "coddepartamento") VALUES ('Alanzinho', 1);
INSERT INTO "funcionario" ("nome", "coddepartamento") VALUES ('Alanzao', 1);