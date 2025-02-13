from src.executor import execute_task

def test_format_file():
    result = execute_task("Format /data/test.md")
    assert "Formatted" in result
