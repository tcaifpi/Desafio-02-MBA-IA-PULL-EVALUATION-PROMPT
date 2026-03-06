import os
import time
from dotenv import load_dotenv
from langsmith import Client
from langsmith.evaluation import evaluate
from langchain.evaluation import load_evaluator
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. Carrega as chaves do .env
load_dotenv()

def main():
    # Recupera chaves
    ls_key = os.getenv("LANGCHAIN_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    client = Client(api_key=ls_key)
    DATASET_NAME = "prompt-optimization-challenge-resolved-eval"
    
    # Configuração dos Modelos
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=openai_key)
    eval_llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=openai_key)
    
    # Carrega o avaliador QA (Correctness)
    qa_evaluator = load_evaluator("qa", llm=eval_llm)

    def predict(inputs: dict):
        try:
            # Puxa o prompt v2 do Hub
            prompt = client.pull_prompt("bug_to_user_story_v2")
            chain = prompt | llm | StrOutputParser()
            
            # Identifica o texto de entrada
            bug_text = inputs.get('bug_report') or inputs.get('input') or next(iter(inputs.values()), "")
            
            return {"output": chain.invoke({"bug_report": bug_text})}
        except Exception as e:
            return {"output": f"Error: {str(e)}"}

    def correctness_evaluator(run, example):
        # Captura predição e gabarito (reference)
        prediction = run.outputs.get("output") or ""
        
        # Mapeamento dinâmico para evitar o erro de 'reference string'
        reference = (
            example.outputs.get("Reference Outputs") or 
            example.outputs.get("output") or 
            (next(iter(example.outputs.values()), None) if example.outputs else None)
        )
        
        input_text = (
            example.inputs.get("bug_report") or 
            example.inputs.get("input") or 
            next(iter(example.inputs.values()), "")
        )

        if not reference:
            return {"key": "correctness", "score": 0, "comment": "Gabarito não encontrado."}

        # Avaliação semântica
        result = qa_evaluator.evaluate_strings(
            prediction=str(prediction),
            input=str(input_text),
            reference=str(reference)
        )
        
        return {
            "key": "correctness", 
            "score": 1 if result["value"] == "CORRECT" else 0,
            "comment": result.get("reasoning", "")
        }

    print("🚀 Iniciando avaliação final (OpenAI gpt-4o judge)...")
    
    # Dispara o experimento no LangSmith
    evaluate(
        predict,
        data=DATASET_NAME,
        evaluators=[correctness_evaluator],
        experiment_prefix="MBA-Final-Success-GPT4o",
    )
    
    print("\n✅ Avaliação concluída com sucesso!")

if __name__ == "__main__":
    main()