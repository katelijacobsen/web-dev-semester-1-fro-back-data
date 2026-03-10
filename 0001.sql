-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Mar 10, 2026 at 09:17 PM
-- Server version: 10.6.20-MariaDB-ubu2004
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodhead`
--

-- --------------------------------------------------------

--
-- Table structure for table `Ingridients`
--

CREATE TABLE `Ingridients` (
  `ingridient_id` char(32) NOT NULL,
  `ingridient_name` varchar(50) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `measure_id` char(32) NOT NULL,
  `recipe_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Measures`
--

CREATE TABLE `Measures` (
  `measure_id` char(32) NOT NULL,
  `measure_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `recipies`
--

CREATE TABLE `recipies` (
  `recipe_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  `recipe_title` varchar(50) NOT NULL,
  `recipe_img` varchar(255) NOT NULL,
  `recipe_instructions` varchar(50) NOT NULL,
  `recipe_created_at` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` char(32) NOT NULL,
  `user_username` varchar(20) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(20) NOT NULL,
  `country` varchar(30) NOT NULL,
  `user_phone` char(8) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_created_at` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_username`, `user_first_name`, `user_last_name`, `country`, `user_phone`, `user_password`, `user_email`, `user_created_at`) VALUES
('f447a89e987c4e91b389fc4f750ebd85', 'Kat', 'Katja', 'Mähleke', 'Denmark', '12346578', 'scrypt:32768:8:1$PXMvuV0GqdRGwdOA$52aeeabee065a7c22c59e4c3709e8316507ac1f74a0c50acbd90ca1794d73a438f3f5082a18dd2244ebc15b7c750e516d9a12faffecdfa58b85dbbc24e6f8267', 'katjamaehleke98@gmail.com', 1773147767);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Ingridients`
--
ALTER TABLE `Ingridients`
  ADD PRIMARY KEY (`ingridient_id`),
  ADD KEY `recipe_id` (`recipe_id`),
  ADD KEY `measure_id` (`measure_id`);

--
-- Indexes for table `Measures`
--
ALTER TABLE `Measures`
  ADD PRIMARY KEY (`measure_id`);

--
-- Indexes for table `recipies`
--
ALTER TABLE `recipies`
  ADD PRIMARY KEY (`recipe_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD UNIQUE KEY `user_username` (`user_username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Ingridients`
--
ALTER TABLE `Ingridients`
  ADD CONSTRAINT `Ingridients_ibfk_1` FOREIGN KEY (`recipe_id`) REFERENCES `recipies` (`recipe_id`),
  ADD CONSTRAINT `Ingridients_ibfk_2` FOREIGN KEY (`measure_id`) REFERENCES `Measures` (`measure_id`);

--
-- Constraints for table `Measures`
--
ALTER TABLE `Measures`
  ADD CONSTRAINT `Measures_ibfk_1` FOREIGN KEY (`measure_id`) REFERENCES `Ingridients` (`ingridient_id`);

--
-- Constraints for table `recipies`
--
ALTER TABLE `recipies`
  ADD CONSTRAINT `recipies_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
