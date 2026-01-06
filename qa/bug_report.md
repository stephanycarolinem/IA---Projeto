# Relatório de Bugs – Classificador de Flores Iris

## Informações Gerais
- Projeto: IA – Classificador de Flores Iris
- Tipo de Teste: Teste Funcional Manual
- Ambiente: Python 3
- Reportado por: Stephany Marques

---

## BUG-01 – Falha ao executar o script sem dependências instaladas

**Descrição:**  
Ao executar o script sem instalar as dependências, o sistema apresenta erro técnico.

**Pré-condição:**  
- Python instalado  
- Dependências NÃO instaladas  

**Passos para reprodução:**
1. Executar o arquivo `iris_classifier.py` sem instalar as dependências

**Resultado esperado:**  
- Exibir mensagem clara informando qual dependência está ausente

**Resultado atual:**  
- Exibição de erro técnico (stack trace)

**Severidade:** Média  
**Prioridade:** Média  
**Status:** Aberto

---

## BUG-02 – Ausência de validação de dados de entrada

**Descrição:**  
O sistema não valida corretamente dados de entrada inválidos ou incompletos.

**Passos para reprodução:**
1. Informar dados inválidos ou incompletos
2. Executar a classificação

**Resultado esperado:**  
- O sistema deveria validar os dados antes da execução

**Resultado atual:**  
- O sistema aceita dados inválidos

**Severidade:** Baixa  
**Prioridade:** Baixa  
**Status:** Aberto
