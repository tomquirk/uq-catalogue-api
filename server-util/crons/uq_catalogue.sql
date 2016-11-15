

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tqstudio_uq_catalogue`
--

-- --------------------------------------------------------

--
-- Table structure for table `Course`
--

CREATE TABLE IF NOT EXISTS `Course` (
  `course_code` varchar(8) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `raw_prerequisites` varchar(500) NOT NULL,
  `units` int(1) NOT NULL,
  `course_profile_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------


--
-- Table structure for table `Course_Semester_Offering`
--

CREATE TABLE IF NOT EXISTS `Course_Semester_Offering` (
  `course_code` varchar(8) NOT NULL,
  `semester_offering` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Plan`
--

CREATE TABLE IF NOT EXISTS `Plan` (
  `plan_code` varchar(10) NOT NULL,
  `program_code` int(4) NOT NULL,
  `title` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Plan_Course_list`
--

CREATE TABLE IF NOT EXISTS `Plan_Course_list` (
  `course_code` varchar(8) NOT NULL,
  `plan_code` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Program_Course_list`
--

CREATE TABLE IF NOT EXISTS `Program_Course_list` (
  `course_code` varchar(8) NOT NULL,
  `program_code` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Program`
--

CREATE TABLE IF NOT EXISTS `Program` (
  `program_code` int(4) NOT NULL,
  `title` varchar(100) NOT NULL,
  `level` varchar(45) NOT NULL,
  `abbreviation` varchar(20) NOT NULL,
  `durationYears` int(1) NOT NULL,
  `units` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Course`
--
ALTER TABLE `Course`
  ADD PRIMARY KEY (`course_code`);

--
-- Indexes for table `Course_Semester_Offering`
--
ALTER TABLE `Course_Semester_Offering`
  ADD PRIMARY KEY (`course_code`,`semester_offering`);

--
-- Indexes for table `Plan`
--
ALTER TABLE `Plan`
  ADD PRIMARY KEY (`plan_code`), ADD KEY `program_code` (`program_code`);

--
-- Indexes for table `Plan_Course_list`
--
ALTER TABLE `Plan_Course_list`
  ADD PRIMARY KEY (`course_code`,`plan_code`), ADD KEY `plan_code_fk` (`plan_code`);

  --
-- Indexes for table `Plan_Course_list`
--
ALTER TABLE `Plan_Course_list`
  ADD PRIMARY KEY (`course_code`,`program_code`), ADD KEY `program_code_fk_1` (`program_code`);

--
-- Indexes for table `Program`
--
ALTER TABLE `Program`
  ADD PRIMARY KEY (`program_code`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Course_Semester_Offering`
--
ALTER TABLE `Course_Semester_Offering`
ADD CONSTRAINT `course_code_fk` FOREIGN KEY (`course_code`) REFERENCES `Course` (`course_code`);

--
-- Constraints for table `Plan`
--
ALTER TABLE `Plan`
ADD CONSTRAINT `program_code_fk` FOREIGN KEY (`program_code`) REFERENCES `Program` (`program_code`);

--
-- Constraints for table `Plan`
--
ALTER TABLE `Program_Course_list`
ADD CONSTRAINT `course_code_fk_2` FOREIGN KEY (`course_code`) REFERENCES `Course` (`course_code`),
ADD CONSTRAINT `program_code_fk_1` FOREIGN KEY (`program_code`) REFERENCES `Program` (`program_code`);

--
-- Constraints for table `Plan_Course_list`
--
ALTER TABLE `Plan_Course_list`
ADD CONSTRAINT `course_code_fk_1` FOREIGN KEY (`course_code`) REFERENCES `Course` (`course_code`),
ADD CONSTRAINT `plan_code_fk` FOREIGN KEY (`plan_code`) REFERENCES `Plan` (`plan_code`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
