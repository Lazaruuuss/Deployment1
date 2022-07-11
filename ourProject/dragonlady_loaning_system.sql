-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 10, 2022 at 09:02 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dragonlady_loaning_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add registration', 6, 'add_registration'),
(22, 'Can change registration', 6, 'change_registration'),
(23, 'Can delete registration', 6, 'delete_registration'),
(24, 'Can view registration', 6, 'view_registration'),
(25, 'Can add apply loan', 7, 'add_applyloan'),
(26, 'Can change apply loan', 7, 'change_applyloan'),
(27, 'Can delete apply loan', 7, 'delete_applyloan'),
(28, 'Can view apply loan', 7, 'view_applyloan'),
(29, 'Can add apply payment', 8, 'add_applypayment'),
(30, 'Can change apply payment', 8, 'change_applypayment'),
(31, 'Can delete apply payment', 8, 'delete_applypayment'),
(32, 'Can view apply payment', 8, 'view_applypayment');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'dragonladyApp', 'applyloan'),
(8, 'dragonladyApp', 'applypayment'),
(6, 'dragonladyApp', 'registration'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-29 07:53:34.451448'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-05-29 07:53:35.214279'),
(3, 'auth', '0001_initial', '2022-05-29 07:53:35.967796'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-05-29 07:53:37.813373'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-05-29 07:53:37.852607'),
(6, 'auth', '0004_alter_user_username_opts', '2022-05-29 07:53:37.883782'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-05-29 07:53:37.916143'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-05-29 07:53:37.946516'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-05-29 07:53:37.982586'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-05-29 07:53:38.035417'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-05-29 07:53:38.072148'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-05-29 07:53:38.203657'),
(13, 'auth', '0011_update_proxy_permissions', '2022-05-29 07:53:38.243550'),
(14, 'dragonladyApp', '0001_initial', '2022-05-29 07:53:39.559930'),
(15, 'admin', '0001_initial', '2022-05-29 07:53:41.062581'),
(16, 'admin', '0002_logentry_remove_auto_add', '2022-05-29 07:53:41.465545'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-29 07:53:41.538462'),
(18, 'sessions', '0001_initial', '2022-05-29 07:53:41.760111'),
(19, 'dragonladyApp', '0002_auto_20220529_1604', '2022-05-29 08:04:08.215179');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('nw77afnw2ma8jdo0h1luu0e2j3z49k3v', 'NjMzNjg2NmEwODE5MDY2YTkwOTNmMWQ3ZTQ3MTE5ZWE1ZGQxNTg1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjMWRhOTRkY2Y5NjE1Y2IyZWI1MzY4NWI4YzAwNTU5NTc2YjdlNTg3In0=', '2022-06-12 11:45:44.481640'),
('y0xz913bnv26jnhdoy1o6elemsqzw05l', 'Y2QyYTRiNTg1OTUyZDdiYzdhYzg4ZWQzZjA3YmUzMzI3NjQyOWRmNjp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYjg5ZmI2NWIzZTU5Yzg3MjRiMmI1M2MxNjU3NzYyMjZmMTkyNjQ0In0=', '2022-06-12 11:34:33.399155');

-- --------------------------------------------------------

--
-- Table structure for table `dragonladyapp_applyloan`
--

CREATE TABLE `dragonladyapp_applyloan` (
  `id` int(11) NOT NULL,
  `to_be_paid` int(11) NOT NULL,
  `loan_date` date NOT NULL,
  `amount_of_loan` int(11) NOT NULL,
  `mode_of_loan_transfer` varchar(50) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dragonladyapp_applypayment`
--

CREATE TABLE `dragonladyapp_applypayment` (
  `id` int(11) NOT NULL,
  `payment_date` date NOT NULL,
  `remaining_balance` int(11) NOT NULL,
  `amount_paid` int(11) NOT NULL,
  `mode_of_payment` varchar(50) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dragonladyapp_registration`
--

CREATE TABLE `dragonladyapp_registration` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(254) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `birthday` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `home_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dragonladyapp_registration`
--

INSERT INTO `dragonladyapp_registration` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `username`, `middle_name`, `age`, `birthday`, `gender`, `home_address`) VALUES
(7, 'pbkdf2_sha256$180000$FIywD3I2JMP8$yTNVKKC8cTiIi+9se0r9KZpZfMsrZ1A7xRi2u+kXd1k=', '2022-07-10 18:21:37.370701', 0, 'Allen', 'Lazaro', 'allenlazarojr@gmail.com', 0, 1, '2022-06-11 06:46:16.631968', 'allenlazarojr@gmail.com', 'Pagay', 20, '2001-06-27', 'M', 'Molino 4'),
(9, 'pbkdf2_sha256$180000$AatN0Fq2hE0r$4cWjEQpUGDax5xMsGkQg44cd/sratszAxMDAHIYLFqg=', NULL, 0, 'Lyn', 'Satsatin', 'lynbsatsatin@gmail.com', 0, 1, '2022-06-15 08:31:07.372967', 'lynbsatsatin@gmail.com', 'Borja', 21, '2000-10-12', 'F', 'Imus City'),
(10, 'pbkdf2_sha256$180000$hIHLr6YbgwOL$bIJvLaNS72y0MzRqAjTtYwWv5pbRO8EfYcDqumALrIA=', NULL, 0, 'admin', 'admin', 'admin@email.com', 1, 1, '2022-07-10 18:46:25.438124', 'admin@email.com', 'admin', 99, '2000-01-01', 'F', 'dragonlady');

-- --------------------------------------------------------

--
-- Table structure for table `dragonladyapp_registration_groups`
--

CREATE TABLE `dragonladyapp_registration_groups` (
  `id` int(11) NOT NULL,
  `registration_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dragonladyapp_registration_user_permissions`
--

CREATE TABLE `dragonladyapp_registration_user_permissions` (
  `id` int(11) NOT NULL,
  `registration_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_dragonlad` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `dragonladyapp_applyloan`
--
ALTER TABLE `dragonladyapp_applyloan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_address_id` (`email_address_id`);

--
-- Indexes for table `dragonladyapp_applypayment`
--
ALTER TABLE `dragonladyapp_applypayment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_address_id` (`email_address_id`);

--
-- Indexes for table `dragonladyapp_registration`
--
ALTER TABLE `dragonladyapp_registration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `dragonladyapp_registration_groups`
--
ALTER TABLE `dragonladyapp_registration_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dragonladyApp_Registrati_registration_id_group_id_9dc64d16_uniq` (`registration_id`,`group_id`),
  ADD KEY `dragonladyApp_Regist_group_id_7f252062_fk_auth_grou` (`group_id`);

--
-- Indexes for table `dragonladyapp_registration_user_permissions`
--
ALTER TABLE `dragonladyapp_registration_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dragonladyApp_Registrati_registration_id_permissi_b2e3d624_uniq` (`registration_id`,`permission_id`),
  ADD KEY `dragonladyApp_Regist_permission_id_cb9d430e_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `dragonladyapp_applyloan`
--
ALTER TABLE `dragonladyapp_applyloan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dragonladyapp_applypayment`
--
ALTER TABLE `dragonladyapp_applypayment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dragonladyapp_registration`
--
ALTER TABLE `dragonladyapp_registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `dragonladyapp_registration_groups`
--
ALTER TABLE `dragonladyapp_registration_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dragonladyapp_registration_user_permissions`
--
ALTER TABLE `dragonladyapp_registration_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_dragonlad` FOREIGN KEY (`user_id`) REFERENCES `dragonladyapp_registration` (`id`);

--
-- Constraints for table `dragonladyapp_applyloan`
--
ALTER TABLE `dragonladyapp_applyloan`
  ADD CONSTRAINT `dragonladyApp_ApplyL_email_address_id_34a353f8_fk_dragonlad` FOREIGN KEY (`email_address_id`) REFERENCES `dragonladyapp_registration` (`id`);

--
-- Constraints for table `dragonladyapp_applypayment`
--
ALTER TABLE `dragonladyapp_applypayment`
  ADD CONSTRAINT `dragonladyApp_ApplyP_email_address_id_ac77787d_fk_dragonlad` FOREIGN KEY (`email_address_id`) REFERENCES `dragonladyapp_applyloan` (`id`);

--
-- Constraints for table `dragonladyapp_registration_groups`
--
ALTER TABLE `dragonladyapp_registration_groups`
  ADD CONSTRAINT `dragonladyApp_Regist_group_id_7f252062_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `dragonladyApp_Regist_registration_id_fe318ed9_fk_dragonlad` FOREIGN KEY (`registration_id`) REFERENCES `dragonladyapp_registration` (`id`);

--
-- Constraints for table `dragonladyapp_registration_user_permissions`
--
ALTER TABLE `dragonladyapp_registration_user_permissions`
  ADD CONSTRAINT `dragonladyApp_Regist_permission_id_cb9d430e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `dragonladyApp_Regist_registration_id_2def7529_fk_dragonlad` FOREIGN KEY (`registration_id`) REFERENCES `dragonladyapp_registration` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
