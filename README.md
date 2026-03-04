🚀 MBA IA para Negócios: Desafio de Otimização de Prompt

Este repositório contém a solução completa para a automação e otimização da conversão de Bug Reports em User Stories. O projeto utiliza engenharia de prompt avançada, monitoramento via LangSmith e avaliação automatizada com GPT-4o.

📂 Estrutura do Entregável

  Código-fonte: Implementação completa em Python para pull de prompts e execução de avaliações.

  Prompt Otimizado: Localizado em prompts/bug_to_user_story_v2.yml (funcional e integrado ao LangSmith Hub).

  Avaliação: Dataset de teste com 20 exemplos e tracing detalhado via LangSmith.

A) Técnicas Aplicadas (Fase 2)

  Para elevar a nota de 0.0 para 1.0, apliquei as seguintes técnicas de engenharia de prompt no arquivo v2.yml:

1. Few-Shot Prompting

  O que é: Fornecer exemplos de entrada e saída esperada dentro do prompt.

  Justificativa: Modelos de linguagem aprendem padrões rapidamente por analogia. Exemplos ajudam a fixar o tom de voz e a estrutura técnica da User Story.

  Aplicação: Inseri 3 exemplos reais de Bugs transformados em Stories no corpo do prompt.

2. Role Prompting (Persona)

  O que é: Definir um papel específico para a IA.

  Justificativa: Atribuir a persona de um "Senior Product Owner/Business Analyst" força o modelo a priorizar clareza de negócio e critérios de aceitação técnicos.

  Aplicação: O prompt inicia com: "Você é um Product Owner sênior especialista em traduzir débitos técnicos para linguagem de negócio."

3. Chain-of-Thought (Cadeia de Pensamento)

  O que é: Instruir o modelo a pensar passo a passo antes de entregar a resposta final.

  Justificativa: Reduz alucinações ao garantir que o modelo identifique primeiro quem é o usuário e qual o problema real antes de escrever a Story.

  Aplicação: Adicionei a instrução: "Analise o Bug Report, identifique o impacto no usuário e então formate a saída."

4. Delimitadores e Estruturação de Markdown

  O que é: Uso de marcadores (###, ---) para separar seções.

  Justificativa: Facilita o parsing do modelo e garante que a saída seja sempre consistente e fácil de ler.

B) Resultados Finais

 📊 Performance Consolidada

     O experimento final demonstrou que a otimização atingiu o teto de performance esperado para o desafio.

     Métrica,            Prompt v1 (Ruim),      Prompt v2 (Otimizado),     Status

     Média de Correctness,       0.00,    1.00 (100%),                     ✅ Atingido
     Aderência ao Gabarito,Baixa / Inconsistente,Total (15/15 validado),   ✅ Atingido
     Custo p/ 15 Runs,           N/A,     $00016,                          ✅ Eficiente

🔗 Evidências no LangSmith

    Link Público do Dashboard: https://smith.langchain.com/public/d1a41759-ba2a-4edc-9634-441150e4cb56/d

    Dataset: prompt-optimization-challenge-resolved-eval com ≥ 20 exemplos cadastrados.

    Tracing: Tracing detalhado disponível para cada execução, mostrando o tempo de resposta médio de 2.04s.

C) Como Executar

    1. Pré-requisitos

      Python 3.10+

      Conta no LangSmith e OpenAI

      Variáveis de ambiente configuradas no .env

2. Instalação de Dependências

   Bash
   pip install -r requirements.txt

3. Fase de Execução

   Passo 1: Upload do Prompt (Hub)

   Garanta que o prompt em prompts/bug_to_user_story_v2.yml foi enviado para o seu LangSmith Hub com o slug bug_to_user_story_v2.

   Passo 2: Execução da Avaliação

   O script irá buscar o prompt no Hub, gerar as respostas com o gpt-4o-mini e avaliá-las com o gpt-4o.

   Bash

   python src/evaluate.py# Desafio-02-MBA-IA-PULL-EVALUATION-PROMPT



