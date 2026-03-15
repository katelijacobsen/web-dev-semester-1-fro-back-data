-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Mar 15, 2026 at 07:39 PM
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
  `recipe_fk` char(32) NOT NULL,
  `ingridient_names` varchar(50) NOT NULL,
  `ingridient_amounts` varchar(10) NOT NULL,
  `ingridient_units` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ingridients`
--

INSERT INTO `ingridients` (`ingridient_id`, `recipe_fk`, `ingridient_names`, `ingridient_amounts`, `ingridient_units`) VALUES
('021d659a0f9745968b8d918bc9c7b3b8', '03cbad3980e64bf6923fcd20bf2605cb', 'DD', '222', 'g'),
('0a6a048fb3d6404bb01a6bfcc3c4383b', '5ed583affc8f412f82ca266a0f0c08cb', 'DD', '222', 'g'),
('1', '', '', '', ''),
('134803ea57f54a1aa415f8f1bad5c14f', '5e021f48e9ae4f6eb67ed9f7041a1ee2', 'DD', '222', 'g'),
('1da31c63268b4227b2c8ff3ea515c588', '9a135cc0fb4b4cf29644d6ab2077a4be', 'DD', '222', 'g'),
('1e0163943e304cfd8401daa5df0a8b65', '690a0954fed74f5988dffe487d13c8cb', 'CC', '111', 'L'),
('1e15fa30465b4c91ae489421377e6337', 'a64cf46c0cb34210a27744e7e2ee7698', 'CC', '111', 'L'),
('1fc7e124f5c64179a0cebf7123b4ede0', 'bc71b34e67b1492994a39d262e7399c7', 'DD', '222', 'g'),
('2', '', '', '', ''),
('212d7ad711e8486dbedfaab587a1f79c', '03cbad3980e64bf6923fcd20bf2605cb', 'CC', '111', 'L'),
('212d8bb898d34894ab638cefb3ad7bdc', '12ca42a69c334fae817bae027c3286fb', 'DD', '222', 'g'),
('2a0b3640419440da919953a63b499bd7', 'e37a01921b5b424a97adc03cd720c70a', 'CC', '111', 'L'),
('2a5d3184b8c744b5863f62fd91ac4b42', '031d2b16e72044e9b998dc8f41ef3a21', 'CC', '111', 'L'),
('2ab3d96a3e0346e4b9c1d368182ce086', '6389e0182fe14449a82ded0bb695f015', 'CC', '111', 'L'),
('330f5b2b5766483f8149758be35aa6e2', '4c3ae7de4533480eba020e8d3e1dade9', 'CC', '111', 'L'),
('37687efd113c44829a5e50e973885be8', 'eaf3abc030ef4501afd7922f20c48c17', '', '222', 'g'),
('37ef725d2b9540c987b48211e1711298', '4c3ae7de4533480eba020e8d3e1dade9', 'DD', '222', 'g'),
('3aaf1eea691641d8bae45cd78026f376', 'e71d8cfea6074e15a6afd56847fc3f36', 'CC', '111', 'L'),
('3cc30c5372a1478f9a0eff0ba84cef5e', '89c3c23908814e0a9409aa3dcba90c5e', 'DD', '222', 'g'),
('40565a2b33504ea1aab1f18220b34576', 'e71d8cfea6074e15a6afd56847fc3f36', 'DD', '222', 'g'),
('44f9ebc097f9464fa36f8c1f94264faa', 'ee7a0b3dd2af4603a27758afa4f7701a', 'DD', '222', 'g'),
('44ff3472bab24ebcb381f0f5503fd597', '912d1260b6fa4525820c19e5dfe64ed0', 'CC', '111', 'L'),
('457a2d63ac3547b4a1114ab6af723321', 'b43f2ad34fb146a0894594d3748bab4c', 'CC', '111', 'L'),
('48c3375e14fb41f2b100a6092ad77cf7', 'a82afb5213b14221a35aa628688dc459', 'CC', '111', 'L'),
('4c2b6ccbce474518bd212a4334de211c', '12ca42a69c334fae817bae027c3286fb', 'CC', '111', 'L'),
('54c03709b6974ad88ea08da179fe0939', '690a0954fed74f5988dffe487d13c8cb', 'DD', '222', 'g'),
('5b8af210799c40f1aea1058e73fc3afe', '83ab6c184cfe4e8c88e858bd74062e3b', 'CC', '111', 'L'),
('5d7632c3fec648e68ed8cf8d1e9fb114', '692324440b19407a8771da6ed0d209d9', 'DD', '222', 'g'),
('5f7435f15a914551a4e04648c3cb9f22', 'ee7a0b3dd2af4603a27758afa4f7701a', 'CC', '111', 'L'),
('605cf301f35146e5ae0fab9bf654c7d9', '096f4354068e4c168d6d2b9bf7ae968c', 'CC', '111', 'L'),
('6544991464e14678a7af24f90352bd5f', 'eaf3abc030ef4501afd7922f20c48c17', '', '111', 'L'),
('6e5e0e88c9084b04be0d2d0de4a653ba', '692324440b19407a8771da6ed0d209d9', 'CC', '111', 'L'),
('7b6c2103e27e4a638527f4a3d633f2f3', '4429c1500b68443ba5e75e56d3115ac0', 'CC', '111', 'L'),
('8273585e9c82416cbeab1bd3ed3fac20', 'bc71b34e67b1492994a39d262e7399c7', 'CC', '111', 'L'),
('8a33946794be47fb9933cd304edcd6c7', '5e021f48e9ae4f6eb67ed9f7041a1ee2', 'CC', '111', 'L'),
('90a7e12f75ee49b8b660111e37478fa4', 'f6b3d89a11b64ba59531e659853fb6e6', 'DD', '222', 'g'),
('9f190236907340639bb19d8b934703a5', '89c3c23908814e0a9409aa3dcba90c5e', 'CC', '111', 'L'),
('a49501fd47c34438a705dfb16f9faf7e', 'b43f2ad34fb146a0894594d3748bab4c', 'DD', '222', 'g'),
('a788aaa2586147a0b2d4e40ea6a6474a', '9dd8be7b998f47a6b42f4bba0a2f9555', '', '111', 'L'),
('af4f41e572224895ab99ab5318201fad', '912d1260b6fa4525820c19e5dfe64ed0', 'DD', '222', 'g'),
('b532e3d3eae441748e4f2e7418ef8e11', 'ec8c73a2a4e74169b763a0fffcc8c106', 'DD', '222', 'g'),
('b76bb0a57006482fb0c637827a17ab64', '096f4354068e4c168d6d2b9bf7ae968c', 'DD', '222', 'g'),
('bb62250f65644d80870c199e9ba7605f', 'a82afb5213b14221a35aa628688dc459', 'DD', '222', 'g'),
('c097a7778fa94138991c282184996ec7', '5ed583affc8f412f82ca266a0f0c08cb', 'CC', '111', 'L'),
('c1adc21cff434ca6a3803168a5cdc8f2', 'a64cf46c0cb34210a27744e7e2ee7698', 'DD', '222', 'g'),
('cb0deb2a306d4836b93f7f9d509dd78b', 'e37a01921b5b424a97adc03cd720c70a', 'DD', '222', 'g'),
('cbe97cecfd7f412d834bbaf2d64c8cc0', '6389e0182fe14449a82ded0bb695f015', 'DD', '222', 'g'),
('e0b9b0791aaa45119dce8b34899fa721', '4429c1500b68443ba5e75e56d3115ac0', 'DD', '222', 'g'),
('e2e22246382844548df4af8ded63cbfb', 'ec8c73a2a4e74169b763a0fffcc8c106', 'CC', '111', 'L'),
('ea10d42734694d8f822e2d861526b997', '9a135cc0fb4b4cf29644d6ab2077a4be', 'CC', '111', 'L'),
('eac393e3c479496e840b74f3a8c971ea', '031d2b16e72044e9b998dc8f41ef3a21', 'DD', '222', 'g'),
('f8c67b28662b49caaba6b724c6f27f43', '83ab6c184cfe4e8c88e858bd74062e3b', 'DD', '222', 'g'),
('fc3fb9c204c440ec8ea9522baa12f8a4', 'f6b3d89a11b64ba59531e659853fb6e6', 'CC', '111', 'L');

-- --------------------------------------------------------

--
-- Table structure for table `instructions`
--

CREATE TABLE `instructions` (
  `instruction_id` char(32) NOT NULL,
  `recipe_fk` char(32) NOT NULL,
  `instruction` varchar(500) NOT NULL,
  `instruction_step_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `instructions`
--

INSERT INTO `instructions` (`instruction_id`, `recipe_fk`, `instruction`, `instruction_step_number`) VALUES
('453b394444d346aeb670e8ed0db9c135', '912d1260b6fa4525820c19e5dfe64ed0', 'adfdsfsd', 1),
('5349aa27a8ba46d2bb495c3e321ee57a', '912d1260b6fa4525820c19e5dfe64ed0', 'esfsfsdsdsd', 2),
('8abac9d3d2af43c9ab961d8ee2caac95', '031d2b16e72044e9b998dc8f41ef3a21', 'sadsdsd', 3),
('b9a1f0e7a3074198948e3b379f319fda', '031d2b16e72044e9b998dc8f41ef3a21', 'adfdsfsd', 1),
('bef58483045c4bb0bfcc4d028d8158d6', '031d2b16e72044e9b998dc8f41ef3a21', 'esfsfsdsdsd', 2),
('e5a066777ff6499d8b43c88a4ac109f6', '912d1260b6fa4525820c19e5dfe64ed0', 'sadsdsd', 3);

-- --------------------------------------------------------

--
-- Table structure for table `recipes`
--

CREATE TABLE `recipes` (
  `recipe_id` char(32) NOT NULL,
  `user_id` char(32) NOT NULL,
  `recipe_title` varchar(50) NOT NULL,
  `recipe_description` varchar(255) NOT NULL,
  `recipe_img_key` text NOT NULL,
  `recipe_servings` int(11) NOT NULL,
  `recipe_prep_time` int(11) NOT NULL,
  `recipe_cook_time` int(11) NOT NULL,
  `recipe_created_at` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recipes`
--

INSERT INTO `recipes` (`recipe_id`, `user_id`, `recipe_title`, `recipe_description`, `recipe_img_key`, `recipe_servings`, `recipe_prep_time`, `recipe_cook_time`, `recipe_created_at`) VALUES
('031d2b16e72044e9b998dc8f41ef3a21', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '75b641d574374a04b2f570cd88533f5a_cookie.png', 4, 60, 30, 1773414024),
('03cbad3980e64bf6923fcd20bf2605cb', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '05ace4c6b2d3453091d81a8f97cb0f5c_cookie.png', 4, 60, 30, 1773411625),
('096f4354068e4c168d6d2b9bf7ae968c', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '63345ec57e1c4f97ab3d022097fc9314_cookie.png', 4, 60, 30, 1773412357),
('12ca42a69c334fae817bae027c3286fb', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '0d93e041ba4846748f2c0b186b8f1657_cookie.png', 4, 60, 30, 1773413744),
('4429c1500b68443ba5e75e56d3115ac0', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'd6b3b99663d242b1980b7f5aa42c07ba_cookie.png', 4, 60, 30, 1773411660),
('4c3ae7de4533480eba020e8d3e1dade9', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'd37e651096d24617ae0f41118f4c3082_cookie.png', 4, 60, 30, 1773412357),
('5e021f48e9ae4f6eb67ed9f7041a1ee2', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '4c5a829d39a143fbb2a9ccc1a7af63cf_cookie.png', 4, 60, 30, 1773411838),
('5ed583affc8f412f82ca266a0f0c08cb', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '9ab1c6e72a034e8bb50dadc859ffba7d_cookie.png', 4, 60, 30, 1773410967),
('6389e0182fe14449a82ded0bb695f015', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '2ad46e2590ae43139f7b5b0376dcbeff_cookie.png', 4, 60, 30, 1773412357),
('690a0954fed74f5988dffe487d13c8cb', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '017c4ca21f9644b7ae93619b2c577799_cookie.png', 4, 60, 30, 1773412357),
('692324440b19407a8771da6ed0d209d9', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'ff0c9fccd70d498b931429b8d628b109_cookie.png', 4, 60, 30, 1773411625),
('912d1260b6fa4525820c19e5dfe64ed0', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '66a4b31b191a45f0990e0b506d66ca36_cookie.png', 4, 60, 30, 1773414011),
('9a135cc0fb4b4cf29644d6ab2077a4be', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '89853149968649a39d6926f17f382c24_cookie.png', 4, 60, 30, 1773413393),
('a64cf46c0cb34210a27744e7e2ee7698', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '4661c66910a0499aacb41c40f5429b13_cookie.png', 4, 60, 30, 1773413412),
('b43f2ad34fb146a0894594d3748bab4c', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'f3f8619501ac4325a5331842101d68b4_cookie.png', 4, 60, 30, 1773411626),
('bc71b34e67b1492994a39d262e7399c7', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'd2aa7ce7456843808fb31b95cc6bd3c1_cookie.png', 4, 60, 30, 1773412357),
('e37a01921b5b424a97adc03cd720c70a', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', 'dcb64544699b44febf89db481edd5468_cookie.png', 4, 60, 30, 1773411626),
('e71d8cfea6074e15a6afd56847fc3f36', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '16b51bbfe236462da01d1b0bbbe9c315_cookie.png', 4, 60, 30, 1773412529),
('ec8c73a2a4e74169b763a0fffcc8c106', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '59f4cf54e4d549868e732fd4bc4e4c92_cookie.png', 4, 60, 30, 1773412334),
('ee7a0b3dd2af4603a27758afa4f7701a', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '7e615c825774408d84e4298a815a89c5_cookie.png', 4, 60, 30, 1773411718),
('f6b3d89a11b64ba59531e659853fb6e6', '4713bf5f3bff4c288caeb69152db26ae', 'TEST', 'æeojfølisghlsjvnlekfmnlæjabglenfljwnglewjnflwrknglweknflkrgnwknglkaerngklsnglkaernglkwngklaergnlkrengeklrgn', '3491064d7c2b4eae9adb44bebace2d37_cookie.png', 4, 60, 30, 1773412357);

-- --------------------------------------------------------

--
-- Table structure for table `recipes_ingridients`
--

CREATE TABLE `recipes_ingridients` (
  `recipe_fk` char(32) NOT NULL,
  `ingridient_fk` char(32) NOT NULL
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
  ADD PRIMARY KEY (`ingridient_id`);

--
-- Indexes for table `instructions`
--
ALTER TABLE `instructions`
  ADD PRIMARY KEY (`instruction_id`),
  ADD KEY `recipe_fk` (`recipe_fk`);

--
-- Indexes for table `recipes`
--
ALTER TABLE `recipes`
  ADD PRIMARY KEY (`recipe_id`);

--
-- Indexes for table `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD PRIMARY KEY (`recipe_fk`,`ingridient_fk`),
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
-- Constraints for table `instructions`
--
ALTER TABLE `instructions`
  ADD CONSTRAINT `instructions_ibfk_1` FOREIGN KEY (`recipe_fk`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE;

--
-- Constraints for table `recipes_ingridients`
--
ALTER TABLE `recipes_ingridients`
  ADD CONSTRAINT `recipes_ingridients_ibfk_1` FOREIGN KEY (`ingridient_fk`) REFERENCES `ingridients` (`ingridient_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recipes_ingridients_ibfk_2` FOREIGN KEY (`recipe_fk`) REFERENCES `recipes` (`recipe_id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`user_country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
