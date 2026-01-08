from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `meetings` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `url_code` VARCHAR(255) NOT NULL UNIQUE,
    `title` VARCHAR(255) NOT NULL DEFAULT '',
    `location` VARCHAR(255) NOT NULL DEFAULT '',
    `start_date` DATE,
    `end_date` DATE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl1lv2kAQgP/Kap9SiUbEQKC8kaMNVYEqQW2VqrIWezGrrHfJetwEUf57NT7wwVGo0p"
    "RGfbPn8M584xmP59TXLpfBcY9zEMrr4R1tkzlVzOe0TdbqK4Sy6TTTogDYSMYOsWUkZKMA"
    "DHOAtsmYyYBXCHV54BgxBaEVbRMVSolC7QRghPIyUajEfcht0B6HCTe0Tb5+qxAqlMsfeZ"
    "DeTu/sseDSLYQsXDw7ktswm0ayM+F1FbyNbPHAke1oGfoqs5/OYKLV0kEoQKnHFTcMOJ4A"
    "JsQMMMAk2TSpONjMJI4y5+PyMQsl5DLeEYOjFSIUCjDnOfXwlNdvLKtWa1rV2mmrUW82G6"
    "1qq0JoFNKqqrmIE86AxI+KsHTfdftDTFQb5sQFRMEi8mHAYq+IdwbYMRyR2AxWQV8w4CB8"
    "vh510bOE3E1cj9OLcgFS3NsqkAqyEmRv3hPVwHDmDpScJeXdgnfY7V3eDDu9j5iJHwT32F"
    "v0ojO8RI0VSWcl6dHpq2I9lg8hn7vDK4K35HbQv4wI6gA8E52Y2Q1vKcbEQtC20g82c3Nv"
    "YipNwSwquc4JjbQd7fLVsp5PmFlf0rxPqaABmN8p4R9vIp892pIrDya0TaxGY0sFP3Wuz6"
    "8610dWo1EqSz9RWbFuUQAJAuReFJcOT4Nwly6g9KARSu2wKKw9KOZ9/oNMQAbADNg4U9dP"
    "6/Uoi17bJvUOWJMGfsYhvQUjDtoSIq7cvQHlfV4gHtyuxsl2tVy3Rsy5e2DGtVc02tKbbF"
    "dVvuWXJUwxL8oU48Xokr2zw41wJus20kSzdRdlmc3BbKIvaA21TurNeqt2Wl9un0vJtqXz"
    "1wvmd26CPUd/zuX5Jv/B7yHYGntATMz/TYAn1eoOAE+q1Y0AI10RoKMV8LgHixDf3wz6G/"
    "5xMpfyd0E4QH4QKQI4TKCLzfww38JfTIrtqNf5UiZ6/mFwVv49wQec/e0Py+InR2ZoDA=="
)
