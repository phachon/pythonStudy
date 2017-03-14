CREATE TABLE `money` (
    `money_id` int(10) NOT NULL AUTO_INCREMENT,
    `account_id` int(10) NOT NULL DEFAULT 0,
    `money` int(10) NOT NULL DEFAULT 0,
    PRIMARY KEY (`money_id`)
)engine=InnoDB default charset=utf8