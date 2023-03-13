/*
将以下数据插入数据库

('肖申克的救赎','肖申克的救赎/ The Shawshank Redemption/ 月黑高飞(港)  /  刺激1995(台)','导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情','9.7','1981964'),
('霸王别姬','霸王别姬/ 再见，我的妾  /  Farewell My Concubine','导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...1993 / 中国大陆 中国香港 / 剧情 爱情 同性','9.6','1466594'),
('阿甘正传','阿甘正传/ Forrest Gump/ 福雷斯特·冈普','导演: 罗伯特·泽米吉斯 Robert Zemeckis   主演: 汤姆·汉克斯 Tom Hanks / ...1994 / 美国 / 剧情 爱情','9.5','1502559'),
('这个杀手不太冷','这个杀手不太冷/ Léon/ 杀手莱昂  /  终极追杀令(台)','导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...1994 / 法国 / 剧情 动作 犯罪','9.4','1696348'),
('美丽人生','美丽人生/ La vita è bella/ 一个快乐的传说(港)  /  Life Is Beautiful','导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...1997 / 意大利 / 剧情 喜剧 爱情 战争','9.5','947714'),
('泰坦尼克号','泰坦尼克号/ Titanic/ 铁达尼号(港 / 台)','导演: 詹姆斯·卡梅隆 James Cameron   主演: 莱昂纳多·迪卡普里奥 Leonardo...1997 / 美国 / 剧情 爱情 灾难','9.4','1450471'),
('千与千寻','千与千寻/ 千と千尋の神隠し/ 神隐少女(台)  /  千与千寻的神隐','导演: 宫崎骏 Hayao Miyazaki   主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...2001 / 日本 / 剧情 动画 奇幻','9.4','1551806'),
('辛德勒的名单','辛德勒的名单/ Schindler's List/ 舒特拉的名单(港)  /  辛德勒名单','导演: 史蒂文·斯皮尔伯格 Steven Spielberg   主演: 连姆·尼森 Liam Neeson...1993 / 美国 / 剧情 历史 战争','9.5','766569'),
('盗梦空间','盗梦空间/ Inception/ 潜行凶间(港)  /  全面启动(台)','导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 莱昂纳多·迪卡普里奥 Le...2010 / 美国 英国 / 剧情 科幻 悬疑 冒险','9.3','1440335'),
('忠犬八公的故事','忠犬八公的故事/ Hachi: A Dog's Tale/ 忠犬小八(台)  /  秋田犬八千(港)','导演: 莱塞·霍尔斯道姆 Lasse Hallström   主演: 理查·基尔 Richard Ger...2009 / 美国 英国 / 剧情','9.4','996903'),
*/

show tables;

create table douban
(
    id        int(11) primary key auto_increment,
    name      varchar(255),
    nickname  varchar(255),
    star      varchar(255),
    score     float,
    followers int
);

insert into douban(name, nickname, star, score, followers)
values ('肖申克的救赎', '肖申克的救赎/ The Shawshank Redemption/ 月黑高飞(港)  /  刺激1995(台)',
        '导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...1994 / 美国 / 犯罪 剧情', '9.7', '1981964'),
       ('霸王别姬', '霸王别姬/ 再见，我的妾  /  Farewell My Concubine',
        '导演: 陈凯歌 Kaige Chen   主演: 张国荣 Leslie Cheung / 张丰毅 Fengyi Zha...1993 / 中国大陆 中国香港 / 剧情 爱情 同性', '9.6', '1466594'),
       ('阿甘正传', '阿甘正传/ Forrest Gump/ 福雷斯特·冈普',
        '导演: 罗伯特·泽米吉斯 Robert Zemeckis   主演: 汤姆·汉克斯 Tom Hanks / ...1994 / 美国 / 剧情 爱情', '9.5', '1502559'),
       ('这个杀手不太冷', '这个杀手不太冷/ Léon/ 杀手莱昂  /  终极追杀令(台)',
        '导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...1994 / 法国 / 剧情 动作 犯罪', '9.4', '1696348'),
       ('美丽人生', '美丽人生/ La vita è bella/ 一个快乐的传说(港)  /  Life Is Beautiful',
        '导演: 罗伯托·贝尼尼 Roberto Benigni   主演: 罗伯托·贝尼尼 Roberto Beni...1997 / 意大利 / 剧情 喜剧 爱情 战争', '9.5', '947714'),
       ('泰坦尼克号', '泰坦尼克号/ Titanic/ 铁达尼号(港 / 台)',
        '导演: 詹姆斯·卡梅隆 James Cameron   主演: 莱昂纳多·迪卡普里奥 Leonardo...1997 / 美国 / 剧情 爱情 灾难', '9.4', '1450471'),
       ('千与千寻', '千与千寻/ 千と千尋の神隠し/ 神隐少女(台)  /  千与千寻的神隐',
        '导演: 宫崎骏 Hayao Miyazaki   主演: 柊瑠美 Rumi Hîragi / 入野自由 Miy...2001 / 日本 / 剧情 动画 奇幻', '9.4', '1551806'),
       ('辛德勒的名单', '辛德勒的名单/ Schindler\'s List/ 舒特拉的名单(港)  /  辛德勒名单',
        '导演: 史蒂文·斯皮尔伯格 Steven Spielberg   主演: 连姆·尼森 Liam Neeson...1993 / 美国 / 剧情 历史 战争', '9.5', '766569'),
       ('盗梦空间', '盗梦空间/ Inception/ 潜行凶间(港)  /  全面启动(台)',
        '导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 莱昂纳多·迪卡普里奥 Le...2010 / 美国 英国 / 剧情 科幻 悬疑 冒险', '9.3', '1440335'),
       ('忠犬八公的故事', '忠犬八公的故事/ Hachi: A Dog\'s Tale/ 忠犬小八(台)  /  秋田犬八千(港)',
        '导演: 莱塞·霍尔斯道姆 Lasse Hallström   主演: 理查·基尔 Richard Ger...2009 / 美国 英国 / 剧情', '9.4', '996903')
;


select * from douban;