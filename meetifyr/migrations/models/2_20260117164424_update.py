from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participants` ADD INDEX `idx_participant_meeting_1de158` (`meeting_id`);
        ALTER TABLE `participant_dates` ADD INDEX `idx_participant_partici_ebb73d` (`participant_id`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participant_dates` DROP INDEX `idx_participant_partici_ebb73d`;
        ALTER TABLE `participants` DROP INDEX `idx_participant_meeting_1de158`;"""


MODELS_STATE = (
    "eJztmVtv4jgUx79K5KeuxI5oWkqXN2jpDjMDjFr2olmtIpO4wRpjU+ewHdTlu6/s3K9DVt"
    "DCKE+QY5/Y/h37+G/nBS2FQ5j3bkwIUO6O1RPqGS+I4yVBPaOwvGUgvFrFpcoAeM58B7+m"
    "NuK5BxLbgHrGI2YeaRnIIZ4t6Qqo4Khn8DVjyihsDyTlbmxac/q0JhYIl8CCSNQz/vq7ZS"
    "DKHfKNeOHj6qv1SAlzUl2mjmpb2y3YrLRtQN0RhztdVzU4t2zB1kse119tYCF45EA5KKtL"
    "OJEYiGoB5FqNQHUwGGw4KL+zcRW/lwkfhzziNYPEiHfEYAuuEFIOaswvyFWt/PyLaV5cdM"
    "32xdV157Lb7Vy3r1sG0l3KF3W3/oBjIP6rNJbRr6PJTA1USGz7AVSGrfbBgH0vzTsGbEui"
    "kFgY8qBvMRCgS1KMOu2ZQe4Eru/CP9kAhLirIhAa4hDEM29PMZAEO1PONkF4K/DORuPhw6"
    "w//qxGsvS8J7W20G1/NlQlprZuMtazq5/S8YheYvwxmr031KPxZToZaoLCA1fqFuN6sy9I"
    "9QmvQVhcPFvYSczE0BqC2bYSK2ctmWULh+TDerPAsjikSZ9MQD2Q/yeEB19ES/zNYoS7sE"
    "A9w+x0KiL4e//+5n3//szsdDJhmQRFpl+2TYEECqwWxchhPwh3WQUIHTVCJmysu1WDYtKn"
    "ARmA9ABLsFROLc7WxSjTXlWZegeswQJ+xSRdgVEl2gwiwp3agJI+PyAepa4eA3UVya05tr"
    "8+Y+lYqZKY4wpLoDZdYdVMXoMF3ncf7wkrW6eB3vwcvynSnMcnBQKMsTWUBAqWMEUZvnzR"
    "0lxmLZhjV/data1aKkNTINeL8JVL9mzYGtneyPZGtp+ObNe/NWRSWP/1JNLRC/bg1sIqSk"
    "LlINNeh8J5GsefnGDIwc2TvROSUJd/JBvNd8Q9wNwumpsl11BHB7dIEYSNSvwcbXuZqSO4"
    "5RBGwJ9v/Yeb/u0QbWtKLi1H96e71JbQaK9S7RXjqdZfKYw7abA4jo0Qa4RYI8ROR4jVvU"
    "PY0/3B22Xfne9XVE+L0ooQjGBedsMSeWUAzYU42K4UZZx9cxlMp59S83gwymSOyW/jwfD+"
    "7FxPYO+JUUgllPSVnqzNM+H1ijzrblxvAjS5+9bd/vK+398Kj0Krvt5mWHE2SNDbw/ngMN"
    "eGb3VGyM+suueEQ2rhPpHUXhSp36CkUu/iuM7RiNwfSOGa55fdy+uLq8toLUeWqiX8fe36"
    "D5Feza9yCZfmxikCqZZGDYhB9dMEeN5u7wDwvN0uBajL0gBtwYEU7RofHqaTkuNT7JKV3N"
    "QG41+DUQ9OTnB/eJhOUjooxHY27v+ZJXrzaTrInnzUCwb1vvntf2PZ/gdxBGOY"
)
