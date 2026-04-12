from minio import Minio

# Conexão com o servidor MinIO
client = Minio(
    "172.40.0.28:9000",  # endpoint (host:port)
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False  # True se usar HTTPS
)
print(type(client))
# Teste simples: listar buckets
buckets = client.list_buckets()

for bucket in buckets:
    print(bucket.name)