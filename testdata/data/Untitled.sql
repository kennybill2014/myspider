DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `uid` varchar(255) NOT NULL,
  `url` text,
  `title` text,
  `time` text,
  `summary` text,
  `content` text
);

