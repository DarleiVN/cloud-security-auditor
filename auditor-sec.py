import boto3
import sys
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def auditar_bucket(nome_bucket):
    try:
        config = s3.get_public_access_block(Bucket=nome_bucket)
        # Verifica se o bloqueio está ativo
        if config['PublicAccessBlockConfiguration']['BlockPublicAcls']:
            return " SEGURO"
        else:
            return " RISCO: Acesso público permitido"
    except ClientError:
        return " RISCO: Sem configuração de bloqueio"

def main():
    relatorio = ["=== RELATÓRIO DE AUDITORIA S3 ===\n"]
    falha_encontrada = False
    
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        nome = bucket['Name']
        status = auditar_bucket(nome)
        
        # Adiciona ao relatório
        linha = f"{nome:<40} | {status}"
        relatorio.append(linha)
        
        if "RISCO" in status:
            falha_encontrada = True
            
    # Salva o relatório
    with open("auditoria-s3.txt", "w") as f:
        f.write("\n".join(relatorio))
    
    print("Auditoria concluída. Relatório gerado: auditoria-s3.txt")
    
    # Se encontrou risco, o script sai com erro para o GitHub Actions
    if falha_encontrada:
        sys.exit(1)

if __name__ == "__main__":
    main()
