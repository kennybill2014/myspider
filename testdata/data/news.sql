DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `uid` varchar(255) NOT NULL,
  `url` text,
  `title` text,
  `time` text,
  `summary` text,
  `content` text,
  PRIMARY KEY (`uid`)
)DEFAULT CHARSET=utf8;

INSERT INTO `news` (`uid`,`url`,`title`,`time`,`summary`,`content`) VALUES ('0dee4043347130fce7cb5479f07c430d','http://sports.ynet.com/2017/04/11/87357t1062.html','国乒男女队杀入亚锦赛男女团四强','2017/04/11 09:54','2017年乒乓球亚锦赛10日在无锡展开男女团四分之一决赛争夺，中国男女队分别战胜朝鲜男队、中华台北女队，双双晋级四强。中国女队当天派出了丁宁、刘诗雯、朱雨玲的最强阵容。首场比赛，新科大满贯得主丁宁迎战...','[{"content": "4月4日，白洋淀岸边的河北省安新县留通村村民杜锁良划着自己的小船穿行在白洋淀里。60岁的杜锁良从6岁起就跟着家人开始了船上生活。清明几天，他已经连续接待了几波北京天津来的客人。中新社记者 刘关关 摄", "type": "1"}, {"content": "4月4日，白洋淀岸边的河北省安新县留通村村民杜锁良划着自己的小船穿行在白洋淀里。60岁的杜锁良从6岁起就跟着家人开始了船上生活。清明几天，他已经连续接待了几波北京天津来的客人。中新社记者 刘关关 摄", "type": "1"}, {"content": "4月4日，河北省白洋淀岸边的安新县留通村村民杜锁良将小船停靠在岸边。", "type": "1"}, {"content": "4月4日，河北省白洋淀岸边的安新县留通村村民杜锁良将小船停靠在岸边。", "type": "1"}, {"content": "4月4日，白洋淀岸边的河北省保定市安新县留通村，69岁的村民李福禄坐在自家的船上。除非天气不好，每天她都会在白洋淀劳作。", "type": "1"}, {"content": "4月4日，白洋淀岸边的河北省保定市安新县留通村，69岁的村民李福禄坐在自家的船上。除非天气不好，每天她都会在白洋淀劳作。", "type": "1"}, {"content": "4月4日，白洋淀岸边的河北省保定市安新县大阳村，村民陈羽站在自己家的车和墙画前留影。", "type": "1"}, {"content": "4月4日，白洋淀岸边的河北省保定市安新县大阳村，村民陈羽站在自己家的车和墙画前留影。", "type": "1"}, {"content": "4月4日，乘客走进河北省保定市雄县汽车站。", "type": "1"}, {"content": "4月4日，乘客走进河北省保定市雄县汽车站。", "type": "1"}, {"content": "4月3日，民众在河北省保定市雄县政府大楼前进行休闲活动。", "type": "1"}, {"content": "4月3日，民众在河北省保定市雄县政府大楼前进行休闲活动。", "type": "1"}]');