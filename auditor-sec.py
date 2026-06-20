import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def auditar_bucket(nome_bucket):
    try:
        # Tenta pegar a configuração de bloqueio de acesso público
        config = s3.get_public_access_block(Bucket=nome_bucket)
        bloqueado = config['PublicAccessBlockConfiguration']['BlockPublicAcls']
        
        if bloqueado:
            return "✅ SEGURO"
        else:
            return "❌ RISCO: Acesso público permitido"
            
    except ClientError:
        # Se não tiver configuração de bloqueio, ele está exposto por padrão
        return "❌ RISCO: Sem configuração de bloqueio"

# Listagem com auditoria
response = s3.list_buckets()

print(f"{'NOME DO BUCKET':<40} | {'STATUS'}")
print("-" * 60)

for bucket in response['Buckets']:
    nome = bucket['Name']
    status = auditar_bucket(nome)
    print(f"{nome:<40} | {status}")
