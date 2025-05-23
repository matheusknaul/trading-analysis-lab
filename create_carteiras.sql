USE bolsa;

CREATE TABLE carteiras(
	id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    nome VARCHAR (255) NOT NULL,
    tipo VARCHAR (50) NOT NULL,
    qtd_teorica DOUBLE,
    part_percentage  double,
    UNIQUE(ticker)
);