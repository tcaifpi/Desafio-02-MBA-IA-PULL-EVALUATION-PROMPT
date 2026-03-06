import os
from dotenv import load_dotenv
from langsmith import Client
from langchain_core.prompts import PromptTemplate

load_dotenv()

def push_to_hub():
    client = Client()
    
    # IMPORTANTE: Use apenas o nome do prompt, SEM prefixos ou IDs longos.
    # O LangSmith usará automaticamente a conta dona da LANGSMITH_API_KEY.
    repo_name = "bug_to_user_story_v2" 
    
    template = """Converta o BUG REPORT em uma User Story técnica.
    
### REGRAS:
- Inicie DIRETAMENTE com "**User Story**: Como..."
- NÃO use saudações ou introduções.
- Seja técnico e direto.

### FORMATO:
**User Story**: Como [persona], eu quero [ação] para que [valor].
**Critérios de Aceite**:
- [Critério 1]
- [Critério 2]

BUG REPORT:
{bug_report}"""

    prompt_obj = PromptTemplate.from_template(template)
    
    print(f"🚀 Enviando prompt diretamente para o seu Hub...")
    try:
        # Enviamos apenas o nome. A biblioteca cuida do tenant via API KEY.
        client.push_prompt(repo_name, object=prompt_obj)
        print(f"✅ Sucesso! Prompt publicado como: {repo_name}")
    except Exception as e:
        print(f"❌ Erro ao subir: {e}")

if __name__ == "__main__":
    push_to_hub()