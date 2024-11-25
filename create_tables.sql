
CREATE TABLE FactOrders (
    OrderID SERIAL PRIMARY KEY,
    OrderDate DATE NOT NULL,
    CustomerID INT NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL
);


CREATE TABLE FactClientesAtendidos (
    ClientID SERIAL PRIMARY KEY,
    AtencionFecha DATE NOT NULL,
    AtencionTipo VARCHAR(50) NOT NULL
);


CREATE TABLE FactOrderDetails (
    OrderDetailID SERIAL PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    TotalPrice DECIMAL(10, 2) GENERATED ALWAYS AS (Quantity * UnitPrice) STORED,
    FOREIGN KEY (OrderID) REFERENCES FactOrders(OrderID)
);
