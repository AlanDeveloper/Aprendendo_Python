CREATE TABLE "departamento" (
    "nome" varchar(100) NOT NULL,
    "codigo" serial,
    "codgerente" int,
    CONSTRAINT "departamentoPK" PRIMARY KEY ("codigo"),
    CONSTRAINT "departamentoFK" FOREIGN KEY ("codgerente")
	REFERENCES "funcionario" ("codigo")
		ON UPDATE CASCADE
		ON DELETE NO ACTION
);

INSERT INTO "departamento" ("nome") VALUES ('Alan e sia');
INSERT INTO "departamento" ("nome") VALUES ('Mauricio inc');

UPDATE "departamento" SET "codgerente" = 2 WHERE "codigo" = 1;
UPDATE "departamento" SET "codgerente" = 1 WHERE "codigo" = 2;