-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: airlineht
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'nguyentrong','202cb962ac59075b964b07152d234b70'),(2,'phanhuy','202cb962ac59075b964b07152d234b70'),(3,'thienphuc','202cb962ac59075b964b07152d234b70');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES (1,'Noi Bai','Ha Noi'),(2,'Tan Son Nhat','TP HCM'),(3,'Cam Ranh','Khanh Hoa'),(4,'Long Khanh','Dong Nai'),(5,'Da Nang','Da Nang'),(6,'Phan Thiet','Binh Thuan'),(7,'Vinh','Vinh'),(8,'Cat Bi','Hai Phong');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Tin','Tran','1234',NULL,'9092209922'),(2,'Tín','Trần','123456','abc1@fox','0943940261'),(3,'Phuc','Thien','123','abc2@fox','0943940261'),(4,'Phúc','Trần','123','abc3@fox','0373893333'),(5,'Phước','Lê','123','abc5@fox','0373893333'),(6,'Bửu','Đặng','261613','abc8@fox','0943940261'),(7,'Huy','Tran','1111','abc11@fox','0775398511'),(8,'Huy','BU','12333','abc6@fox','0775398511'),(9,'Thao','Truong','002020','abc12@fox','0979273737'),(10,'Huy','Nguyen','111111','abc17@fox','0775398511'),(11,'Trong','Nguyen','12333','abc22@fox','0979273737'),(12,'Yen','Vo','12333','abc6666@fox','0979273737'),(13,'Thao','Truong','4321','abc52@fox','0775398511'),(14,'Trong','Tran','2232','abc14@fox','0775398511'),(15,'a','a','a','1851050056huy@ou.edu.vn','0775398511');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `flight schedule`
--

LOCK TABLES `flight schedule` WRITE;
/*!40000 ALTER TABLE `flight schedule` DISABLE KEYS */;
INSERT INTO `flight schedule` VALUES (1,1,6,NULL,'2020-12-06','00:00:00',30,1),(2,1,6,NULL,'2020-12-07','01:00:00',40,2),(3,2,1,NULL,'2020-12-06','02:00:00',30,3),(4,1,4,NULL,'2020-12-07','01:00:00',30,4);
/*!40000 ALTER TABLE `flight schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `plane`
--

LOCK TABLES `plane` WRITE;
/*!40000 ALTER TABLE `plane` DISABLE KEYS */;
INSERT INTO `plane` VALUES (1),(2),(3),(4),(5),(6),(7);
/*!40000 ALTER TABLE `plane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
INSERT INTO `seat` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,2,1),(10,2,2),(11,2,3),(12,2,4),(13,2,5),(14,2,6),(15,2,7),(16,2,8),(17,3,1),(18,3,2),(19,3,3),(20,3,4),(21,3,5),(22,3,6),(23,3,7),(24,3,8),(25,4,1),(26,4,2),(27,4,3),(28,4,4),(29,4,5),(30,4,6),(31,4,7),(32,4,8);
/*!40000 ALTER TABLE `seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `seat location`
--

LOCK TABLES `seat location` WRITE;
/*!40000 ALTER TABLE `seat location` DISABLE KEYS */;
INSERT INTO `seat location` VALUES (1,'A1',1),(2,'A2',1),(3,'A3',1),(4,'A4',1),(5,'B1',2),(6,'B2',2),(7,'B3',2),(8,'B4',2);
/*!40000 ALTER TABLE `seat location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Trọng','Nguyễn','ndt050800@gmail.com','0943940261',NULL,1,NULL,'ADMIN'),(2,'Huy','Trần','tph@gmail.com','037733337',NULL,1,'2020-12-06','STAFF'),(3,'Phuc','Thien','tph@gmail.com','0917909999',NULL,1,'2020-12-14','STAFF');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,1,1,1,2,'2020-12-14 07:44:00',NULL,0),(2,2,1,1,2,'2020-12-14 07:44:00',NULL,0),(3,3,1,2,2,'2020-12-14 07:44:00',NULL,0),(4,4,1,NULL,NULL,NULL,NULL,1),(5,5,1,NULL,NULL,NULL,NULL,1),(6,6,1,NULL,NULL,NULL,NULL,1),(7,7,1,NULL,NULL,NULL,NULL,1),(8,8,1,4,2,'2020-12-14 07:44:00',NULL,0),(9,9,2,5,1,'2020-12-16 09:19:59',NULL,0),(10,10,2,NULL,NULL,NULL,NULL,0),(11,11,2,NULL,NULL,NULL,NULL,0),(12,12,2,12,1,'2020-12-16 11:36:37',NULL,0),(13,13,2,NULL,NULL,NULL,NULL,1),(14,14,2,NULL,NULL,NULL,NULL,1),(15,15,2,NULL,NULL,NULL,NULL,1),(16,16,2,NULL,NULL,NULL,NULL,1),(17,17,3,6,2,'2020-12-16 09:23:58',NULL,0),(18,18,3,8,1,'2020-12-16 10:23:07',NULL,0),(19,19,3,NULL,NULL,NULL,NULL,1),(20,20,3,NULL,NULL,NULL,NULL,1),(21,21,3,NULL,NULL,NULL,NULL,1),(22,22,3,NULL,NULL,NULL,NULL,1),(23,23,3,NULL,NULL,NULL,NULL,1),(24,24,3,14,2,'2021-03-18 17:26:10',NULL,0),(25,25,4,NULL,NULL,NULL,NULL,1),(26,26,4,7,1,NULL,NULL,0),(27,27,4,13,1,NULL,NULL,0),(28,28,4,NULL,NULL,NULL,NULL,1),(29,29,4,NULL,NULL,NULL,NULL,1),(30,30,4,NULL,NULL,NULL,NULL,1),(31,31,4,NULL,NULL,NULL,NULL,1),(32,32,4,NULL,NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `type_seat`
--

LOCK TABLES `type_seat` WRITE;
/*!40000 ALTER TABLE `type_seat` DISABLE KEYS */;
INSERT INTO `type_seat` VALUES (1,'Class 1',10),(2,'Class 2',5);
/*!40000 ALTER TABLE `type_seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'airlineht'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-18 17:36:14
