CREATE TABLE "departamento" (
    "nome" varchar(100) NOT NULL,
    "codigo" serial unique,
    "codgerente" int,
    CONSTRAINT "departamentoPK" PRIMARY KEY ("codigo"),
    CONSTRAINT "departamentoFK" FOREIGN KEY ("codgerente")
	REFERENCES "funcionario" ("codigo")
		ON UPDATE CASCADE
		ON DELETE NO ACTION
);