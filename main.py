import redis_settings
import redis

redis_cli = redis.Redis(
            host = redis_settings.HOST,
            port = redis_settings.PORT,
            db = redis_settings.DB_ID
        )

redis_cli.set('hoge', 'fuga')
print(redis_cli.get('hoge').decode())
print(redis_cli.delete('hoge'))
