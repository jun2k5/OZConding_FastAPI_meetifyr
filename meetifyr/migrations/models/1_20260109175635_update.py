from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `participants` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `name` VARCHAR(255) NOT NULL,
    `meeting_id` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `participant_dates` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `date` DATE NOT NULL,
    `enabled` BOOL NOT NULL DEFAULT 1,
    `starred` BOOL NOT NULL DEFAULT 0,
    `participant_id` BIGINT NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `participants`;
        DROP TABLE IF EXISTS `participant_dates`;"""


MODELS_STATE = (
    "eJztmW1vGjkQx7/Kyq9SiVZkE0KOd5CQK22BKqG9U0+nldl1FqvGJt6hCcrx3St7nx/Lng"
    "iFllfJjj1r+zf2zH/NM5oLhzDvzZAQoNwdqifUMZ4Rx3OCOkZhe8NAeLGIW5UB8JT5Dn5P"
    "bcRTDyS2AXWMe8w80jCQQzxb0gVQwVHH4EvGlFHYHkjK3di05PRhSSwQLoEZkahj/PNvw0"
    "CUO+SJeOHj4qt1TwlzUlOmjhpb2y1YLbStR90BhxvdVw04tWzBlnMe91+sYCZ45EA5KKtL"
    "OJEYiBoB5FKtQE0wWGy4KH+ycRd/lgkfh9zjJYPEijfEYAuuEFIOas3PyFWjvP7DNM/O2m"
    "bz7OKydd5uty6blw0D6Snlm9prf8ExEP9VGsvgz8FoohYqJLb9ACrDWvtgwL6X5h0DtiVR"
    "SCwMedDXGAjQOSlGnfbMIHcC1zfhP9kAhLirIhAa4hDEO29LMZAEO2POVkF4K/BOBsP+3a"
    "Q7/KhWMve8B3W20HV30lctprauMtaTi1fpeEQvMf4aTN4a6tH4Mh71NUHhgSv1iHG/yRek"
    "5oSXICwuHi3sJHZiaA3BrBuJk7OUzLKFQ/JhvZphWRzSpE8moB7I/xPCFz9Ec/xkMcJdmK"
    "GOYbZaFRH83L29etu9PTFbrUxYRkGT6betUyCBAqtFMXLYDsJNTgFCe42QCRvradWgmPQ5"
    "ggxAeoAlWCqnFmfrYpRpr6pMvQHW4ADvMElXYFSJNoOIcKc2oKTPL4hHqav7QF1FcmuK7a"
    "+PWDpWqiXmuMASqE0XWA2T12CB9837W8LKzmmgNz/Gb4o05/5JgQBjbA0lgYIlTFGGL980"
    "N+dZC+bY1bNWY6uRytAUyPUifOWSPRu2o2w/yvajbD8c2a7/1pBJYf/dSaS9F+zBrYVVlI"
    "TKQaa9fnOcOcWQo5tHeyMkoS5/T1Ya8IB7gLldtDlL7qEOQxOEY0j8GBW+zOYR3HIII+Dv"
    "uO7dVfe6j9Y1RZcWpNtTXqooHBjpXaqvGE+1Akth3EiFxXE8SrGjFDtKscORYnVvEbZ0g/"
    "Dzsu/GNyxqpkVpRQhGMC+7Y4m8MoCmQrxYVYoyzra59MbjD6l93BtkMsfo07DXvz051RvY"
    "e2AUUgklfakna/NMeO2QZ93C9VOAJqtv3fKX9/1xKdyPQ7y7aljxdZDAt4UvhMO9OSz8Ss"
    "jvrbpfCi+phrtEUntWpH+DlkrFi+M+eyNzfyGNa56et88vzy7Oo8McWarO8I/V6zcivZq/"
    "zCVcfvNrkmTRUUejBsSg+2ECPG02NwB42myWAtRtaYC24ECKysa7u/Go5AMqdsmKbmqD8Z"
    "/BqLen1Xpdzk+tN6WEQmwnw+7fWaJXH8a97LePekGv3u9+2y8s6+9qc2TE"
)
