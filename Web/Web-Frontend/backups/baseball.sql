-- phpMyAdmin SQL Dump
-- version 4.6.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 15, 2017 at 03:33 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.0.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `baseball`
--

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

CREATE TABLE `games` (
  `gid` int(11) NOT NULL,
  `gamenum` int(11) NOT NULL,
  `home` varchar(255) NOT NULL,
  `away` varchar(255) NOT NULL,
  `hscore` int(11) NOT NULL,
  `ascore` int(11) NOT NULL,
  `loc` varchar(255) NOT NULL,
  `innings` int(11) NOT NULL,
  `year` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `games`
--

INSERT INTO `games` (`gid`, `gamenum`, `home`, `away`, `hscore`, `ascore`, `loc`, `innings`, `year`) VALUES
(348, 1, 'Colorado Rockies', 'Milwaukee Brewers', 9, 0, 'Coors Field', 9, 2017),
(349, 2, 'Detroit Tigers', 'Minnesota Twins', 1, 0, 'Comerica Park', 9, 2017),
(350, 3, 'Colorado Rockies', 'Arizona Diamondbacks', 9, 0, 'Coors Field', 9, 2017),
(351, 4, 'Washington Nationals', 'Miami Marlins', 7, 0, 'Nationals Park', 9, 2017),
(352, 5, 'St. Louis Cardinals', 'Washington Nationals', 6, 0, 'Busch Stadium III', 9, 2017),
(353, 1, 'San Diego Padres', 'Arizona Diamondbacks', 11, 0, 'Petco Park', 9, 2018),
(354, 2, 'Cleveland Indians', 'Atlanta Braves', 3, 1, 'Progressive Field', 11, 2018),
(355, 3, 'Pittsburgh Pirates', 'Chicago White Sox', 5, 0, 'PNC Park', 9, 2018),
(356, 4, 'Washington Nationals', 'Detroit Tigers', 1, 4, 'Nationals Park', 9, 2018),
(357, 5, 'Los Angeles Angels of Anaheim', 'Tampa Bay Rays', 5, 0, 'Angel Stadium of Anaheim', 9, 2018),
(358, 6, 'Los Angeles Angels of Anaheim', 'Philadelphia Phillies', 3, 0, 'Angel Stadium of Anaheim', 9, 2018),
(359, 7, 'Toronto Blue Jays', 'Arizona Diamondbacks', 6, 0, 'Rogers Centre', 9, 2018),
(360, 8, 'Minnesota Twins', 'Arizona Diamondbacks', 5, 0, 'Target Field', 9, 2018),
(361, 9, 'Atlanta Braves', 'San Diego Padres', 4, 3, 'Turner Field', 9, 2018),
(362, 10, 'Cleveland Indians', 'Chicago Cubs', 1, 0, 'Progressive Field', 9, 2018),
(363, 11, 'Minnesota Twins', 'New York Yankees', 3, 0, 'Target Field', 9, 2018),
(364, 12, 'San Francisco Giants', 'Kansas City Royals', 7, 2, 'AT&T Park', 9, 2018),
(365, 13, 'Chicago White Sox', 'St. Louis Cardinals', 6, 1, 'U.S. Cellular Field', 9, 2018),
(366, 14, 'Cincinnati Reds', 'Texas Rangers', 7, 0, 'Great American Ball Park', 9, 2018),
(367, 15, 'New York Mets', 'Chicago White Sox', 3, 0, 'Citi Field', 12, 2018),
(368, 16, 'San Francisco Giants', 'Tampa Bay Rays', 9, 1, 'AT&T Park', 9, 2018),
(369, 17, 'Detroit Tigers', 'Cincinnati Reds', 7, 1, 'Comerica Park', 9, 2018);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `games`
--
ALTER TABLE `games`
  ADD PRIMARY KEY (`gid`),
  ADD UNIQUE KEY `gid` (`gid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `games`
--
ALTER TABLE `games`
  MODIFY `gid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=370;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
