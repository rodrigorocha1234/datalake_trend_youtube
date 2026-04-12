from minio import Minio
from minio.error import S3Error


def testar_conexao_minio() -> None:
    client = Minio(
        "172.40.0.28:9000",
        access_key="minioadmin",
        secret_key="minioadmin123",
        secure=False
    )

    try:
        buckets = client.list_buckets()

        print("✅ Conexão com MinIO OK!")
        print(f"Total de buckets: {len(buckets)}")

    except S3Error as e:
        print("❌ Erro S3:")
        print(e)
    except Exception as e:
        print("❌ Erro geral:")
        print(e)


if __name__ == "__main__":
    testar_conexao_minio()
