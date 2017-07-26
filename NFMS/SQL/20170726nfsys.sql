-- MySQL dump 10.13  Distrib 5.7.17, for Win32 (AMD64)
--
-- Host: localhost    Database: nfsys
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actioninfo`
--

DROP TABLE IF EXISTS `actioninfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `actioninfo` (
  `ID` int(11) NOT NULL,
  `ParentID` int(11) DEFAULT NULL,
  `ActionInfoName` varchar(45) DEFAULT NULL,
  `SubTime` date DEFAULT NULL,
  `DelFlag` tinyint(1) DEFAULT '0',
  `ModifiedOnTime` date DEFAULT NULL,
  `Remark` varchar(256) DEFAULT NULL,
  `Url` varchar(256) DEFAULT NULL,
  `AreaName` varchar(45) DEFAULT NULL,
  `ActionMethodName` varchar(45) DEFAULT NULL,
  `ControllerName` varchar(45) DEFAULT NULL,
  `JsFunctionName` varchar(45) DEFAULT NULL,
  `Sort` int(11) DEFAULT NULL,
  `ActionTypeEnum` int(11) DEFAULT NULL,
  `IconWidth` int(11) DEFAULT NULL,
  `IconHeight` int(11) DEFAULT NULL,
  `IconCls` varchar(45) DEFAULT NULL,
  `IconClassName` varchar(45) DEFAULT NULL,
  `isShow` tinyint(4) DEFAULT NULL,
  `MethodTypeEnum` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actioninfo`
--

LOCK TABLES `actioninfo` WRITE;
/*!40000 ALTER TABLE `actioninfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `actioninfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-26 10:08:32
