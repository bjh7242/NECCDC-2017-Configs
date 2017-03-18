-- phpMyAdmin SQL Dump
-- version 4.6.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 17, 2017 at 08:28 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 7.0.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `f-sports`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `pid` int(11) NOT NULL,
  `post` text NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`pid`, `post`, `title`) VALUES
(1, 'Congratulations to the 2015 Champion... The Magical Monkies. The magicians had a great run but couldn\'t muster enough in week 20. It was just for a trophy anyway. Since these two teams were first place anyway.', 'The Champ is Here!!!!');

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `uid` int(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scores`
--

INSERT INTO `scores` (`uid`, `score`) VALUES
(1, 15),
(4, 0),
(6, 0),
(7, 0),
(8, 0),
(9, 0);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session` varchar(255) NOT NULL DEFAULT 'session',
  `uid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session`, `uid`) VALUES
('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3', 1),
('ea3243132d653b39025a944e70f3ecdf70ee3994', 8),
('d03f9d34194393019e6d12d7c942827ebd694443', 9);

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `uid` int(11) NOT NULL,
  `player1` varchar(30) DEFAULT NULL,
  `player2` varchar(30) DEFAULT NULL,
  `player3` varchar(30) DEFAULT NULL,
  `player4` varchar(30) DEFAULT NULL,
  `player5` varchar(30) DEFAULT NULL,
  `player6` varchar(30) DEFAULT NULL,
  `player7` varchar(30) DEFAULT NULL,
  `player8` varchar(30) DEFAULT NULL,
  `player9` varchar(30) DEFAULT NULL,
  `player10` varchar(30) DEFAULT NULL,
  `player11` varchar(30) DEFAULT NULL,
  `player12` varchar(30) DEFAULT NULL,
  `player13` varchar(30) DEFAULT NULL,
  `player14` varchar(30) DEFAULT NULL,
  `player15` varchar(30) DEFAULT NULL,
  `player16` varchar(30) DEFAULT NULL,
  `player17` varchar(30) DEFAULT NULL,
  `player18` varchar(30) DEFAULT NULL,
  `player19` varchar(30) DEFAULT NULL,
  `player20` varchar(30) DEFAULT NULL,
  `player21` varchar(30) DEFAULT NULL,
  `player22` varchar(30) DEFAULT NULL,
  `player23` varchar(30) DEFAULT NULL,
  `player24` varchar(30) DEFAULT NULL,
  `player25` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`uid`, `player1`, `player2`, `player3`, `player4`, `player5`, `player6`, `player7`, `player8`, `player9`, `player10`, `player11`, `player12`, `player13`, `player14`, `player15`, `player16`, `player17`, `player18`, `player19`, `player20`, `player21`, `player22`, `player23`, `player24`, `player25`) VALUES
(1, 'zumayjo01', 'zychto01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `uid` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `username`, `password`, `email`) VALUES
(1, 'test', 'test', 'none@none.com'),
(5, 'test4', 'test', 'test@test.com'),
(6, 'test5', 'te', 'test@test.com'),
(7, 'test6', 'test', 'test@test.com'),
(8, 'test7', 'test', 'test@test.com'),
(9, 'test8', 'test', 'test@test.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `uid` (`uid`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `uid` (`uid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
