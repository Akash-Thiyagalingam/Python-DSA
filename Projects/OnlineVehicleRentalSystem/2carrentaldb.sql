-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 10, 2023 at 12:50 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2carrentaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` int(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `VehicleNo` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL,
  `SDate` date NOT NULL,
  `EDate` date NOT NULL,
  `IdProof` varchar(500) NOT NULL,
  `License` varchar(500) NOT NULL,
  `Dname` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `VehicleNo`, `Amount`, `Date`, `Image`, `SDate`, `EDate`, `IdProof`, `License`, `Dname`, `Status`) VALUES
(1, 'san', 'TN45AL5535', '40000.0', '2023-05-01', '4835.png', '2023-05-01', '2023-05-09', 'admin.png', 'Planet9_Wallpaper_5000x2813.jpg', 'sangeeth', 'paid'),
(4, 'san', 'TN45AL5535', '5000.0', '2023-05-02', '4835.png', '2023-05-10', '2023-05-11', '32.png', '76.jpg', 'sangeeth', 'waiting');

-- --------------------------------------------------------

--
-- Table structure for table `ownertb`
--

CREATE TABLE `ownertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FirstName` varchar(250) NOT NULL,
  `LastName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `ownertb`
--

INSERT INTO `ownertb` (`id`, `FirstName`, `LastName`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(3, 'sangeeth', 'Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'sangeeth', 'sangeeth'),
(4, 'Sangeeth', 'Kumar', 'sangeeth5535@gmail.com', '7904902206', 'No 16 samnath plaza, melapudur  trichy', 'Sangeeth123', 'Sangeeth123'),
(5, 'sangeeth', 'Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san56', 'san56');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(10) NOT NULL auto_increment,
  `VehicleNo` varchar(250) NOT NULL,
  `VehicleType` varchar(250) NOT NULL,
  `YearOfRegistration` varchar(250) NOT NULL,
  `Gearbox` varchar(250) NOT NULL,
  `PowerPS` varchar(250) NOT NULL,
  `FuelType` varchar(250) NOT NULL,
  `Brand` varchar(250) NOT NULL,
  `Amount` varchar(20) NOT NULL,
  `RcBook` varchar(500) NOT NULL,
  `UploadImage` varchar(500) NOT NULL,
  `Dname` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `lat` varchar(500) NOT NULL,
  `lon` varchar(500) NOT NULL,
  `City` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `VehicleNo`, `VehicleType`, `YearOfRegistration`, `Gearbox`, `PowerPS`, `FuelType`, `Brand`, `Amount`, `RcBook`, `UploadImage`, `Dname`, `Address`, `lat`, `lon`, `City`) VALUES
(4, 'TN45AL5535', 'limousine', '2014', 'automatic', '1200', 'petrol', 'bmw', '5000', 'codepy11.txt', '4835.png', 'sangeeth', 'no 6 trichy', '10.7905', '78.7047', 'Trichy'),
(5, 'TN45AL5535', 'limousine', '2014', 'automatic', '2500', 'diesel', 'audi', '8000', '32.png', '6966.png', 'sangeeth', 'no 6 trichy', '10.3624', '77.9695', 'Dindigul');

-- --------------------------------------------------------

--
-- Table structure for table `querytb`
--

CREATE TABLE `querytb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `OwnerName` varchar(250) NOT NULL,
  `Queryinfo` varchar(500) NOT NULL,
  `Answer` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `querytb`
--

INSERT INTO `querytb` (`id`, `UserName`, `OwnerName`, `Queryinfo`, `Answer`, `Status`) VALUES
(1, 'san', 'sangeeth', 'time asf', ' 10 am', 'Answer');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FirstName` varchar(250) NOT NULL,
  `LastName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `FirstName`, `LastName`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'daisy', 'daisy', '9486365535', 'daisy@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'daisy', 'daisy'),
(2, 'san', 'Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san'),
(3, 'Sangeeth', 'Kumar', 'sangeeth5535@gmail.com', '7904902206', 'No 16 samnath plaza, melapudur  trichy\r\nNo 16 samnath plaza, melapudur, trichy', 'Sangeeth123', 'Sangeeth123');
