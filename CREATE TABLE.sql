CREATE TABLE `FORMA_PG` (
  `ID_FORMA_PG` int NOT NULL AUTO_INCREMENT,
  `DESC_FORMA_PG` varchar(200) NOT NULL,
  `ID_PEDIDO` char(9) NOT NULL,
  PRIMARY KEY (`ID_FORMA_PG`),
) ;
CREATE TABLE `USUARIO` (
  `ID_USUARIO` int NOT NULL AUTO_INCREMENT,
  `LOGIN_USUARIO` varchar(200) NOT NULL,
  `SENHA_USUARIO` char(11) NOT NULL, 
  `ID_TIPO_ACESSO_USUARIO` char(1) NOT NULL,  
  `NOME_USUARIO` varchar(200) NOT NULL,
  `CPF_USUARIO` char(11) NOT NULL, 
  `ENDERECO_USUARIO` varchar(200) NOT NULL,
  `TELEFONE_USUARIO` char(11) NOT NULL,    
  `EMAIL_USUARIO` varchar(200) NOT NULL, 
  `SEXO_USUARIO` char(1) NOT NULL,  
  `DT_NASCIMENTO_USUARIO` date NOT NULL, 
  `ATIVO` char(1) NOT NULL, 
  PRIMARY KEY (`ID_CLIENTE`),
  KEY `ID_TIPO_ACESSO_USUARIO_idx` (`ID_TIPO_ACESSO_USUARIO`),
  CONSTRAINT `ID_TIPO_ACESSO_USUARIO` FOREIGN KEY (`ID_TIPO_ACESSO_USUARIO`) REFERENCES `TIPO_ACESSO` (`ID_TIPO_ACESSO_USUARIO`),
) ;
CREATE TABLE `TIPO_ACESSO` (
  `ID_TIPO_ACESSO` int NOT NULL AUTO_INCREMENT,
  `DESC_TIPO_ACESSO` varchar(200) NOT NULL,
  PRIMARY KEY (`ID_TIPO_ACESSO`),
) ;
CREATE TABLE `REC_SENHA` (
  `ID_REC_SENHA` int NOT NULL AUTO_INCREMENT,
  `ID_USUARIO` char(11) NOT NULL,  
    PRIMARY KEY (`ID_REC_SENHA`),
) ;
CREATE TABLE `PEDIDO` (
  `ID_PEDIDO` int NOT NULL AUTO_INCREMENT,
  `ID_USUARIO_PEDIDO` char(11) NOT NULL,
  `TOTAL_PEDIDO` varchar(200) NOT NULL,
  `OBS_PEDIDO` varchar(200) NOT NULL, 
  `DATA_PEDIDO` date NOT NULL,    
  PRIMARY KEY (`ID_PEDIDO`),
  KEY `ID_USUARIO_PEDIDO_idx` (`ID_USUARIO_PEDIDO`),
  CONSTRAINT `ID_USUARIO_PEDIDO` FOREIGN KEY (`ID_USUARIO_PEDIDO`) REFERENCES `USUARIO` (`ID_USUARIO_PEDIDO`),
) ;
CREATE TABLE `PEDIDO_CANCELAMENTO` (
  `ID_PEDIDO_CANCELAMENTO` int NOT NULL AUTO_INCREMENT,
  `ID_PEDIDO` int NOT NULL AUTO_INCREMENT,
  `TP_CANCELAMENTO` char(11) NOT NULL,  
  `DESC_PEDIDO_CANCELAMENTO` varchar(200) NOT NULL,
  `DATA_CANCELAMENTO` date NOT NULL,
  PRIMARY KEY (`ID_PEDIDO_CANCELAMENTO`),
  KEY `ID_PEDIDO_idx` (`ID_PEDIDO`),
  CONSTRAINT `ID_PEDIDO` FOREIGN KEY (`ID_PEDIDO`) REFERENCES `PEDIDO` (`ID_PEDIDO`),








) ;
CREATE TABLE `CLIENTE` (
  `ID_CLIENTE` int NOT NULL AUTO_INCREMENT,
  `NOME_CLIENTE` varchar(200) NOT NULL,
  `CPF_CLIENTE` char(11) NOT NULL, 
  `ENDERECO_CLIENTE` varchar(200) NOT NULL,
  `TELEFONE_CLIENTE` char(11) NOT NULL,    
  `EMAIL_CLIENTE` varchar(200) NOT NULL, 
  `SEXO_CLIENTE` char(1) NOT NULL,  
  `DT_NASCIMENTO` date NOT NULL, 
  PRIMARY KEY (`ID_CLIENTE`),