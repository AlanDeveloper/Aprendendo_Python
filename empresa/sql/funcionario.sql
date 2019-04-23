CREATE TABLE "funcionario" (
    "nome" varchar(100) NOT NULL,
    "codigo" serial,
    "coddepartamento" int,
    CONSTRAINT "funcionarioPK" PRIMARY KEY ("codigo")
);

ALTER TABLE  "funcionario" ADD CONSTRAINT "funcionarioFK" FOREIGN KEY  ("coddepartamento")
	REFERENCES "departamento" ("codigo")
		ON UPDATE CASCADE
		ON DELETE NO ACTION



INSERT INTO "funcionario" ("nome", "coddepartamento") VALUES ('Alan', 2);
INSERT INTO "funcionario" ("nome", "coddepartamento") VALUES ('Mauricio', 1);


SELECT "f"."nome", "f"."codigo", "d"."nome" FROM "funcionario" AS "f" INNER JOIN "departamento" AS "d" ON "f"."codigo" = "d"."codgerente";