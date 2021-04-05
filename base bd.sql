
CREATE DATABASE IF NOT EXISTS `petshop` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `petshop`;



CREATE TABLE IF NOT EXISTS `tb_produto` (
  `id_produto` int(11) NOT NULL AUTO_INCREMENT,
  `nome_produto` varchar(200) NOT NULL,
  `tipo_produto` varchar(200) NOT NULL,
  `foto_produto` char(11) NOT NULL,
  `preco_compra_produto` char(9) NOT NULL,
  `preco_venda_produto` char(11) NOT NULL,
  `quantidade_produto` varchar(200) NOT NULL,
  PRIMARY KEY (`id_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `tb_usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `email_usuario` varchar(300) NOT NULL,
  `senha_usuario` varchar(20) NOT NULL,
  `nome_usuario` varchar(50) NOT NULL,
  'cod_segurança' int(11) not null,
  'status' boolean not null DEFAULT 0;
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Exportação de dados foi desmarcado.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
