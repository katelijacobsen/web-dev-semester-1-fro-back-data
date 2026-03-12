-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Mar 12, 2026 at 10:04 AM
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
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `country_id` char(32) NOT NULL,
  `country_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
('1', 'Denmark'),
('2', 'Germany');

-- --------------------------------------------------------

--
-- Table structure for table `ingridients`
--

CREATE TABLE `ingridients` (
  `ingridient_id` char(32) NOT NULL,
  `ingridient_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ingridients`
--

INSERT INTO `ingridients` (`ingridient_id`, `ingridient_name`) VALUES
('1', 'salt'),
('2', 'sugar');

-- --------------------------------------------------------

--
-- Table structure for table `recipes`
--

CREATE TABLE `recipes` (
  `recipe_id` char(32) NOT NULL,
  `recipe_title` varchar(50) NOT NULL,
  `recipe_servings` int(11) NOT NULL,
  `recipe_prep_time` int(11) NOT NULL,
  `recipe_cook_time` int(11) NOT NULL,
  `recipe_instructions` text NOT NULL,
  `recipe_created_at` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recipes`
--

INSERT INTO `recipes` (`recipe_id`, `recipe_title`, `recipe_servings`, `recipe_prep_time`, `recipe_cook_time`, `recipe_instructions`, `recipe_created_at`) VALUES
('1', 'Delicious cookies', 0, 0, 0, '', 0),
('2', 'Tiramisu', 0, 0, 0, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `recipes_ingridients`
--

CREATE TABLE `recipes_ingridients` (
  `recipie_fk` char(32) NOT NULL,
  `ingridient_fk` char(32) NOT NULL,
  `recipe_quantity` decimal(10,2) NOT NULL,
  `recipe_unit` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recipes_ingridients`
--

INSERT INTO `recipes_ingridients` (`recipie_fk`, `ingridient_fk`, `recipe_quantity`, `recipe_unit`) VALUES
('1', '1', 0.00, ''),
('1', '2', 0.00, ''),
('2', '1', 0.00, ''),
('2', '2', 0.00, '');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` char(32) NOT NULL,
  `user_username` varchar(20) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(20) NOT NULL,
  `user_country_id` char(32) NOT NULL,
  `user_phone` varchar(20) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_created_at` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_username`, `user_first_name`, `user_last_name`, `user_country_id`, `user_phone`, `user_password`, `user_email`, `user_created_at`) VALUES
('4713bf5f3bff4c288caeb69152db26ae', 'Kat', 'Katja', 'Mähleke', '1', '91996396', 'scrypt:32768:8:1$fpHrStCWC0JK8tQO$a57dfd6d9669d574d66aa81c77e7c1411bc95ee029ded02b518fb025a49fa0b17309768ec4d5850dc6980ef4d5d18a4c4090ddca52d2811463173e93f06d28e7', 'katjamaehleke98@gmail.com', 1773265128);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`),
  ADD UNIQUE KEY `country_name` (`country_name`);

--
-- Indexes for table `ingridients`
--
ALTER TABLE `ingridients`
  ADD PRIMARY KEY (`ingridient_id`),
  ADD UNIQUE KEY `ingridient_name` (`ingridient_name`),
  ADD UNIQUE KEY `ingridient_name_2` (`ingridient_name`);

--
-- Indexes for table `recipes`
--
ALTER TABLE `recipes`
  ADD PRIMARY KEY (`recipe_id`);

--
-- Indexes for table `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD PRIMARY KEY (`recipie_fk`,`ingridient_fk`),
  ADD KEY `ingridient_fk` (`ingridient_fk`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD UNIQUE KEY `user_username` (`user_username`),
  ADD KEY `user_country_id` (`user_country_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD CONSTRAINT `recipes_ingridients_ibfk_1` FOREIGN KEY (`ingridient_fk`) REFERENCES `ingridients` (`ingridient_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recipes_ingridients_ibfk_2` FOREIGN KEY (`recipie_fk`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
