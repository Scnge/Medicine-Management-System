/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3306
 Source Schema         : medicine

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 02/06/2024 00:24:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 供应商
-- ----------------------------
DROP TABLE IF EXISTS `供应商`;
CREATE TABLE `供应商`  (
  `供应商ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `供应商名称` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `负责人` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `联系方式` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`供应商ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 供应商
-- ----------------------------
INSERT INTO `供应商` VALUES ('0', '1', '1', '1');
INSERT INTO `供应商` VALUES ('10', '华东医药股份有限公司', '俞佳俊', '13269463082');
INSERT INTO `供应商` VALUES ('11', '绍兴市上虞区梁湖镇康宁大药房', '王加乐', '13454049693');
INSERT INTO `供应商` VALUES ('12', '兰溪市云龙大药房连锁有限公司德济堂连锁店', '童亚飞', '13216143974');
INSERT INTO `供应商` VALUES ('13', '台州市老百姓好心情医药连锁有限公司开发区界牌店', '吴泼', '15816279705');
INSERT INTO `供应商` VALUES ('14', '诸暨市盛唐医药连锁有限公司元亨药房', '洪筱瑜', '15791135259');
INSERT INTO `供应商` VALUES ('15', '宁波明天科技有限公司', '李正日', '18942258012');
INSERT INTO `供应商` VALUES ('16', '华东医药股份有限公司广通分公司', '张秀红', '15584706818');
INSERT INTO `供应商` VALUES ('17', '临海市延年堂药店 ', '朱丽娅', '15233793959');
INSERT INTO `供应商` VALUES ('18', '杭州树兰弘毅大药房有限公司', '龚晓涛', '18827917647');
INSERT INTO `供应商` VALUES ('19', '华东医药股份有限公司', '梁霖锋', '15856685664');
INSERT INTO `供应商` VALUES ('2', '苍南县桥墩镇百信药店有限公司', '薛小苹', '18585262376');
INSERT INTO `供应商` VALUES ('20', '余姚市同济堂药品零售连锁有限公司舜水南路店', '俞青青', '15194211241');
INSERT INTO `供应商` VALUES ('3', '温州一洲医药连锁有限公司同济店', '黄纪元', '13344497620');
INSERT INTO `供应商` VALUES ('4', '浙江麦斯康莱医药有限公司', '段平浩', '15522442642');
INSERT INTO `供应商` VALUES ('5', '瑞安市瑞诚大药房有限公司', '林瑞道', '15614675932');
INSERT INTO `供应商` VALUES ('6', '杭州萧山同春堂医药零售有限责任公司', '胡贝贝', '13304043258');
INSERT INTO `供应商` VALUES ('7', '温岭市泽国广源药店', '江云琴', '15541169138');
INSERT INTO `供应商` VALUES ('8', '浙江普泽医药有限公司', '黄炜明', '13567438211');
INSERT INTO `供应商` VALUES ('9', '遂昌慈福堂便民药店有限公司', '陈敏芳', '18615291784');

-- ----------------------------
-- Table structure for 医保卡
-- ----------------------------
DROP TABLE IF EXISTS `医保卡`;
CREATE TABLE `医保卡`  (
  `医保卡ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `患者ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `余额` double NOT NULL,
  PRIMARY KEY (`医保卡ID`) USING BTREE,
  INDEX `患者ID`(`患者ID` ASC) USING BTREE,
  CONSTRAINT `YB-HZ` FOREIGN KEY (`患者ID`) REFERENCES `患者` (`患者ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 医保卡
-- ----------------------------
INSERT INTO `医保卡` VALUES ('00001', '00001', 56.7);
INSERT INTO `医保卡` VALUES ('00003', '00003', 577);
INSERT INTO `医保卡` VALUES ('1', '1', 99999);

-- ----------------------------
-- Table structure for 医生
-- ----------------------------
DROP TABLE IF EXISTS `医生`;
CREATE TABLE `医生`  (
  `医生ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `医生姓名` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `科室` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `联系方式` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`医生ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 医生
-- ----------------------------
INSERT INTO `医生` VALUES ('1', 'test', 'test', 'test');
INSERT INTO `医生` VALUES ('Oph001', '李泽元', '眼科', '13586744156');
INSERT INTO `医生` VALUES ('Ped001', '陈新平', '儿科', '18726513134');
INSERT INTO `医生` VALUES ('Ped002', '陈慧', '儿科', '18587689026');
INSERT INTO `医生` VALUES ('Uro001', '李继红', '泌尿科', '18551888617');

-- ----------------------------
-- Table structure for 处方
-- ----------------------------
DROP TABLE IF EXISTS `处方`;
CREATE TABLE `处方`  (
  `处方ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `开具日期` datetime NOT NULL,
  `医生ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `患者ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`处方ID`) USING BTREE,
  INDEX `CF-YS-1`(`医生ID` ASC) USING BTREE,
  INDEX `CF-HZ-1`(`患者ID` ASC) USING BTREE,
  CONSTRAINT `CF-HZ-1` FOREIGN KEY (`患者ID`) REFERENCES `患者` (`患者ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `CF-YS-1` FOREIGN KEY (`医生ID`) REFERENCES `医生` (`医生ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 处方
-- ----------------------------
INSERT INTO `处方` VALUES ('0000001', '2024-05-23 15:18:36', '1', '1');
INSERT INTO `处方` VALUES ('0000002', '2024-05-23 15:18:36', '1', '00001');
INSERT INTO `处方` VALUES ('0000003', '2024-05-23 23:29:12', '1', '00003');

-- ----------------------------
-- Table structure for 处方内容
-- ----------------------------
DROP TABLE IF EXISTS `处方内容`;
CREATE TABLE `处方内容`  (
  `处方ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `药品ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `数量` int NOT NULL,
  PRIMARY KEY (`处方ID`, `药品ID`) USING BTREE,
  INDEX `CFNR-YP-1`(`药品ID` ASC) USING BTREE,
  CONSTRAINT `CFNR-CF-1` FOREIGN KEY (`处方ID`) REFERENCES `处方` (`处方ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `CFNR-YP-1` FOREIGN KEY (`药品ID`) REFERENCES `药品` (`药品ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 处方内容
-- ----------------------------
INSERT INTO `处方内容` VALUES ('0000001', '0000001', 2);
INSERT INTO `处方内容` VALUES ('0000003', '0000002', 2);

-- ----------------------------
-- Table structure for 患者
-- ----------------------------
DROP TABLE IF EXISTS `患者`;
CREATE TABLE `患者`  (
  `患者ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `患者姓名` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `身份证号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `年龄` int NOT NULL,
  `患者联系方式` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`患者ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 患者
-- ----------------------------
INSERT INTO `患者` VALUES ('00001', '冯君', 'a', 21, '15967983431');
INSERT INTO `患者` VALUES ('00003', '潘蕾', 'a', 25, '18988843283');
INSERT INTO `患者` VALUES ('1', 'test', 'test', 0, 'test');
INSERT INTO `患者` VALUES ('2', 'test', 'test', 2, 'test');

-- ----------------------------
-- Table structure for 药品
-- ----------------------------
DROP TABLE IF EXISTS `药品`;
CREATE TABLE `药品`  (
  `药品ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `药品名称` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `批准文号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `供应商ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `药品类型` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `库存地址` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `保质期` int NOT NULL,
  `进货价` double NOT NULL,
  `售价` double NOT NULL,
  `库存数量` int NOT NULL,
  `主要成分` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `储存方式` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `适用症状` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`药品ID`) USING BTREE,
  INDEX `YP-GYS-1`(`供应商ID` ASC) USING BTREE,
  CONSTRAINT `YP-GYS-1` FOREIGN KEY (`供应商ID`) REFERENCES `供应商` (`供应商ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 药品
-- ----------------------------
INSERT INTO `药品` VALUES ('0000001', '同仁堂(清心明目上清丸)', '0000001', '0', '内服', '1-1-1', 24, 21, 29, 276, ' aa', '常温', '清热散风，明目止痛。用于上焦火盛引起的：暴发火眼，红肿痛痒，热泪昏花，云翳遮睛，头痛目眩，烦燥口渴，大便燥结。');
INSERT INTO `药品` VALUES ('0000002', '盐酸哌仑西平片', '0000002', '3', '内服', '1-1-1', 12, 35, 49, 1098, 'aa', '常温', '临床主要用于各种酸相关性疾患，如：十二指肠溃疡、胃溃疡、胃-食管反流症、高酸性胃炎、应激性溃疡、急性胃粘膜出血、胃泌素瘤等。');
INSERT INTO `药品` VALUES ('0000003', '加味白药丸', '0000003', '9', '内服', '1-3-5', 6, 9, 12, 567, 'aa', '常温', '健胃消食。用于消化不良，胃腹胀痛，肠鸣，食欲不振。');
INSERT INTO `药品` VALUES ('0000004', '对乙酰氨基酚片', '0000004', '12', '内服', '2-3-3', 24, 49, 59, 498, 'bb', '常温', '抑制血小板聚成，防止血栓形成，治疗和预防短暂脑缺血发作、脑血栓、冠心病、心肌梗塞、偏头疼、人工心脏瓣膜，动静脉漏和其他手术后的血栓形成，血栓闭塞性脉管');

-- ----------------------------
-- Table structure for 药品销售记录
-- ----------------------------
DROP TABLE IF EXISTS `药品销售记录`;
CREATE TABLE `药品销售记录`  (
  `记录ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `药品ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `医生ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `患者ID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `数量` int NOT NULL,
  `销售日期` datetime NOT NULL,
  PRIMARY KEY (`记录ID`) USING BTREE,
  INDEX `JL-YP`(`药品ID` ASC) USING BTREE,
  INDEX `JL-YS`(`医生ID` ASC) USING BTREE,
  INDEX `JL-HZ`(`患者ID` ASC) USING BTREE,
  CONSTRAINT `JL-HZ` FOREIGN KEY (`患者ID`) REFERENCES `患者` (`患者ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `JL-YP` FOREIGN KEY (`药品ID`) REFERENCES `药品` (`药品ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `JL-YS` FOREIGN KEY (`医生ID`) REFERENCES `医生` (`医生ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 药品销售记录
-- ----------------------------

-- ----------------------------
-- Table structure for 账号密码医生
-- ----------------------------
DROP TABLE IF EXISTS `账号密码医生`;
CREATE TABLE `账号密码医生`  (
  `医生账号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `医生密码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`医生账号`, `医生密码`) USING BTREE,
  CONSTRAINT `ZH-YS` FOREIGN KEY (`医生账号`) REFERENCES `医生` (`医生ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 账号密码医生
-- ----------------------------
INSERT INTO `账号密码医生` VALUES ('1', '1');
INSERT INTO `账号密码医生` VALUES ('Oph001', 'Oph001');
INSERT INTO `账号密码医生` VALUES ('Ped001', 'Ped001');
INSERT INTO `账号密码医生` VALUES ('Ped002', 'Ped002');
INSERT INTO `账号密码医生` VALUES ('Uro001', 'Uro001');

-- ----------------------------
-- Table structure for 账号密码患者
-- ----------------------------
DROP TABLE IF EXISTS `账号密码患者`;
CREATE TABLE `账号密码患者`  (
  `患者账号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `患者密码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`患者账号`, `患者密码`) USING BTREE,
  CONSTRAINT `ZH-HZ` FOREIGN KEY (`患者账号`) REFERENCES `患者` (`患者ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 账号密码患者
-- ----------------------------
INSERT INTO `账号密码患者` VALUES ('00001', '00001');
INSERT INTO `账号密码患者` VALUES ('00003', '00003');
INSERT INTO `账号密码患者` VALUES ('1', '1');
INSERT INTO `账号密码患者` VALUES ('2', '2');

-- ----------------------------
-- Table structure for 账号密码管理员
-- ----------------------------
DROP TABLE IF EXISTS `账号密码管理员`;
CREATE TABLE `账号密码管理员`  (
  `管理员账号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `管理员密码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `管理员姓名` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`管理员账号`, `管理员密码`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of 账号密码管理员
-- ----------------------------
INSERT INTO `账号密码管理员` VALUES ('admin1', 'admin1', 'abb');

-- ----------------------------
-- View structure for 药品患者
-- ----------------------------
DROP VIEW IF EXISTS `药品患者`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `药品患者` AS select `药品`.`药品名称` AS `药品名称`,`药品`.`批准文号` AS `批准文号`,`药品`.`药品类型` AS `药品类型`,`药品`.`保质期` AS `保质期`,`药品`.`售价` AS `售价`,`药品`.`主要成分` AS `主要成分`,`药品`.`储存方式` AS `储存方式`,`药品`.`适用症状` AS `适用症状` from `药品`;

-- ----------------------------
-- Triggers structure for table 供应商
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateSupplierIDInMedicine`;
delimiter ;;
CREATE TRIGGER `UpdateSupplierIDInMedicine` AFTER UPDATE ON `供应商` FOR EACH ROW BEGIN
    IF OLD.供应商ID <> NEW.供应商ID THEN
        UPDATE 药品
        SET 供应商ID = NEW.供应商ID
        WHERE 供应商ID = OLD.供应商ID;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 医生
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateDoctorAccount`;
delimiter ;;
CREATE TRIGGER `UpdateDoctorAccount` AFTER UPDATE ON `医生` FOR EACH ROW BEGIN
    IF OLD.`医生ID` <> NEW.`医生ID` THEN
        UPDATE `账号密码医生`
        SET `医生账号` = NEW.`医生ID`
        WHERE `医生账号` = OLD.`医生ID`;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 医生
-- ----------------------------
DROP TRIGGER IF EXISTS `CheckDoctorIDBeforeInsert`;
delimiter ;;
CREATE TRIGGER `CheckDoctorIDBeforeInsert` BEFORE INSERT ON `医生` FOR EACH ROW BEGIN
    DECLARE cnt INT;
    SELECT COUNT(*) INTO cnt FROM 医生 WHERE 医生ID = NEW.医生ID;
    IF cnt > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate doctor ID';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 处方
-- ----------------------------
DROP TRIGGER IF EXISTS `DeletePrescriptionContents`;
delimiter ;;
CREATE TRIGGER `DeletePrescriptionContents` AFTER DELETE ON `处方` FOR EACH ROW BEGIN
    DELETE FROM 处方内容
    WHERE 处方ID = OLD.处方ID;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 患者
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateParentAccount`;
delimiter ;;
CREATE TRIGGER `UpdateParentAccount` AFTER UPDATE ON `患者` FOR EACH ROW BEGIN
    IF OLD.`患者ID` <> NEW.`患者ID` THEN
        UPDATE `账号密码患者`
        SET `患者账号` = NEW.`患者ID`
        WHERE `患者账号` = OLD.`患者ID`;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 患者
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdateParentCard`;
delimiter ;;
CREATE TRIGGER `UpdateParentCard` AFTER UPDATE ON `患者` FOR EACH ROW BEGIN
    IF OLD.`患者ID` <> NEW.`患者ID` THEN
        UPDATE `医保卡`
        SET `患者ID` = NEW.`患者ID`
        WHERE `患者ID` = OLD.`患者ID`;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 患者
-- ----------------------------
DROP TRIGGER IF EXISTS `CheckDuplicatePatientID`;
delimiter ;;
CREATE TRIGGER `CheckDuplicatePatientID` BEFORE INSERT ON `患者` FOR EACH ROW BEGIN
    IF EXISTS (SELECT * FROM 患者 WHERE 患者ID = NEW.患者ID) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate patient ID';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 患者
-- ----------------------------
DROP TRIGGER IF EXISTS `DeletePatientPrescriptions`;
delimiter ;;
CREATE TRIGGER `DeletePatientPrescriptions` AFTER DELETE ON `患者` FOR EACH ROW BEGIN
    DELETE FROM 处方
    WHERE 患者ID = OLD.患者ID;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 患者
-- ----------------------------
DROP TRIGGER IF EXISTS `CheckPatientAgeBeforeInsert`;
delimiter ;;
CREATE TRIGGER `CheckPatientAgeBeforeInsert` BEFORE INSERT ON `患者` FOR EACH ROW BEGIN
    IF NEW.年龄 <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid age: Age must be greater than zero.';
    END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
