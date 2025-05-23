USE bolsa;

CREATE TABLE candles(
	id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    timeframe VARCHAR(10) NOT NULL,
    datetime DATETIME NOT NULL,
    open DOUBLE,
	high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume DOUBLE,
    UNIQUE(ticker, timeframe, datetime)
);