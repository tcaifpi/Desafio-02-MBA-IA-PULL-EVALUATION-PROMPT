import pytest
import yaml
import os

def get_v2_prompt():
    path = "prompts/bug_to_user_story_v2.yml"
    with open(path, "r") as f:
        return yaml.safe_load(f)

def test_prompt_has_system_prompt():
    prompt = get_v2_prompt()
    assert "system_prompt" in prompt
    assert len(prompt["system_prompt"]) > 50

def test_prompt_has_role_definition():
    prompt = get_v2_prompt()
    role_keywords = ["Product Manager", "Engenheiro", "SPO"]
    assert any(keyword in prompt["system_prompt"] for keyword in role_keywords)

def test_prompt_has_few_shot_examples():
    prompt = get_v2_prompt()
    assert "few_shot_examples" in prompt
    assert len(prompt["few_shot_examples"]) >= 1

def test_prompt_no_todos():
    prompt = get_v2_prompt()
    content = str(prompt)
    assert "[TODO]" not in content
    assert "..." not in content  # Garante que não há espaços vazios