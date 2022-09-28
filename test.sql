
CREATE SCHEMA IF NOT EXISTS test_spm_db DEFAULT CHARACTER SET utf8 ;
use test_spm_db;
-- Job_role Table 
DROP TABLE IF EXISTS `Job_Role`;
CREATE TABLE Job_Role (
    Job_ID int NOT NULL auto_increment,
    Job_Role varchar(20) NOT NULL,
    Job_Title varchar(20) NOT NULL,
    PRIMARY KEY (Job_ID)
);
-- population of data
insert into Job_Role values (1,"CEO","The big boss"),(2,"Operations manager","Manager"),(3,"Operations Slave","Staff");

DROP TABLE IF EXISTS `skill`;
CREATE TABLE IF NOT EXISTS `skill` (
  `Skill_ID` char(13) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `skill` (`Skill_ID`, `name`) VALUES
('S001', 'Critical Thinking'),
('S002', 'People Management');


DROP TABLE IF EXISTS `Role_has_Skill`;
CREATE TABLE Role_has_Skill (
    Job_ID int NOT NULL,
    Skill_ID char(13) NOT NULL,
    CONSTRAINT Job_ID FOREIGN KEY (Job_ID)
    REFERENCES Job_Role(Job_ID),
    CONSTRAINT Skill_ID FOREIGN KEY (Skill_ID)
    REFERENCES skill(Skill_ID)
);

INSERT INTO `Role_has_Skill` VALUES
(1,'S001'),
(1,'S002'),
(2,'S002'),
(2,'S001')


