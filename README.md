 # 🛡️ Cloud Security Auditor

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-S3-orange.svg)](https://aws.amazon.com/s3/)
[![Security](https://img.shields.io/badge/Security-DevSecOps-red.svg)]()

Um sistema automatizado de **auditoria de conformidade** para Buckets AWS S3. Projetado para detectar configurações de risco em tempo real e integrar segurança diretamente ao ciclo de desenvolvimento (CI/CD).

## 💡 O Problema
Configurações incorretas em buckets S3 são uma das maiores causas de vazamento de dados na nuvem. Revisar permissões manualmente em ambientes com dezenas de buckets é ineficiente e propenso a erros humanos.

## 🚀 A Solução
O **Cloud Security Auditor** automatiza essa verificação.
* **Detecção Automática:** Varre todos os buckets em busca de desativação do "Public Access Block".
* **Fail-Fast Security:** Integrado ao GitHub Actions, o pipeline interrompe o fluxo de trabalho se encontrar vulnerabilidades.
* **Evidência de Auditoria:** Gera relatórios detalhados (`auditoria-s3.txt`) salvos como artefatos de build para histórico de conformidade.

## 🛠️ Tecnologias
* **AWS Boto3:** Para interação programática com os serviços de infraestrutura.
* **GitHub Actions:** Orquestração de pipelines para execução de auditorias.
* **Cloud Security (DevSecOps):** Implementação de governança e controle de acesso.

## 📊 Exemplo de Output
O sistema fornece uma visão clara do estado de segurança da conta:

```text
=== RELATÓRIO DE AUDITORIA S3 ===
meu-auditor-seguranca-1781920540          | ✅ SEGURO
teste-bucket-inseguro-darlei              | ❌ RISCO: Acesso público permitido
teste-bucket-seguro-darlei3               | ✅ SEGURO
 
