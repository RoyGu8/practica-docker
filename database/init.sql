CREATE TABLE departamentos (
    id_departamento SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE cargos (
    id_cargo SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefono VARCHAR(30),
    fecha_ingreso DATE NOT NULL,
    id_departamento INTEGER NOT NULL,
    id_cargo INTEGER NOT NULL,

    FOREIGN KEY (id_departamento)
        REFERENCES departamentos(id_departamento),

    FOREIGN KEY (id_cargo)
        REFERENCES cargos(id_cargo)
);

INSERT INTO departamentos (nombre, descripcion) VALUES
('Recursos Humanos', 'Gestion del personal'),
('Operaciones', 'Operaciones mineras'),
('Tecnologia', 'Sistemas y tecnologia'),
('Finanzas', 'Gestion financiera'),
('Seguridad', 'Seguridad industrial');

INSERT INTO cargos (nombre, descripcion) VALUES
('Gerente de RRHH', 'Gestion del talento humano'),
('Ingeniero de Minas', 'Supervision de operaciones mineras'),
('Desarrollador de Software', 'Desarrollo de sistemas'),
('Analista Financiero', 'Analisis financiero'),
('Supervisor de Seguridad', 'Supervision de seguridad');

INSERT INTO empleados
(nombre, apellido, email, telefono, fecha_ingreso, id_departamento, id_cargo)
VALUES
('Carlos', 'Mendoza', 'carlos@intipunku.com', '70000001', '2022-01-15', 1, 1),
('Ana', 'Quispe', 'ana@intipunku.com', '70000002', '2023-03-10', 3, 3),
('Luis', 'Vargas', 'luis@intipunku.com', '70000003', '2021-07-20', 2, 2),
('Maria', 'Flores', 'maria@intipunku.com', '70000004', '2024-02-05', 4, 4),
('Pedro', 'Condori', 'pedro@intipunku.com', '70000005', '2022-11-18', 5, 5),
('Sofia', 'Rojas', 'sofia@intipunku.com', '70000006', '2023-06-12', 1, 2),
('Jorge', 'Mamani', 'jorge@intipunku.com', '70000007', '2020-09-25', 2, 2),
('Valeria', 'Choque', 'valeria@intipunku.com', '70000008', '2024-01-08', 3, 3),
('Diego', 'Paredes', 'diego@intipunku.com', '70000009', '2021-04-16', 4, 4),
('Lucia', 'Torrez', 'lucia@intipunku.com', '70000010', '2023-10-30', 5, 5);