# Casos de Teste – Classificador de Flores Iris

## Informações Gerais
- Projeto: IA – Classificador de Flores Iris
- Tipo de Teste: Teste Funcional Manual
- Ambiente: Python 3
- Responsável: Stephany Marques

---

## CT-01 – Executar o script com dados válidos
**Prioridade:** Alta  
**Pré-condições:**  
- Python instalado  
- Dependências instaladas via requirements.txt  

**Passos:**
1. Executar o arquivo `iris_classifier.py`

**Dados de teste:**
- Dataset Iris padrão

**Resultado esperado:**
- O script executa sem erros
- Exibe o resultado da classificação

**Status:** PASS

---

## CT-02 – Executar o script sem dependências instaladas
**Prioridade:** Média  
**Pré-condições:**  
- Python instalado  
- Dependências NÃO instaladas  

**Passos:**
1. Executar o arquivo `iris_classifier.py`

**Dados de teste:**
- Ambiente sem bibliotecas necessárias

**Resultado esperado:**
- O sistema exibe mensagem clara informando a dependência ausente

**Status:** FAIL

---

## CT-03 – Execução repetida do script
**Prioridade:** Baixa  
**Pré-condições:**  
- Ambiente configurado corretamente  

**Passos:**
1. Executar o script três vezes consecutivas

**Dados de teste:**
- Dataset padrão

**Resultado esperado:**
- O sistema mantém comportamento consistente
- Não ocorre falha ou travamento

**Status:** PASS
