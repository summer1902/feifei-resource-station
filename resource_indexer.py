"""资源索引工具：扫描目录并生成结构化索引，供资源站使用。"""
from __future__ import annotations
import json
import sys
from pathlib import Path

def index_directory(root: str) -> list[dict]:
    entries = []
    for path in sorted(Path(root).rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        entries.append({"path": rel, "size": path.stat().st_size, "ext": path.suffix})
    return entries

def main() -> None:
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    data = index_directory(root)
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

