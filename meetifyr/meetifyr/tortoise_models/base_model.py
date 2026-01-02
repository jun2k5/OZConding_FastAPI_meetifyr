from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL: primary key 를 정할떄 주의해야할 점
# MySQL version 8 이상 부터
# inodb가 default engine (옛날엔 MyISAM)

# innodb의 특징 중 하나 -> clustering index
# primary key를 기준으로
# primary key 값이 비슷한 row 들끼리 disk 에서도 실제로 모여있음

# HDD
# 랜덤 IO 가 느리고, 순차 IO 가 빠르다.

# 그냥 int 가 아니라, 비즈니스 적 의미가 있고
# 계속해서 증가하는 어떤 값으로 설정하면
# 굉장히 빠르게 읽을 수 있다.

# primary key를 아주 랜덤한 id값으로 정하면
# 밀어내는 연산이 지속되면서 성능 문제가 생긴다.
