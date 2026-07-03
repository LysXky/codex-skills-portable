#!/usr/bin/env python3
"""Export local Codex user skills into a portable repository."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
from collections import Counter
from pathlib import Path


EXCLUDED_DIRS = {".runtime", "__pycache__", ".git", ".venv", "venv"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--repo", required=True, type=Path)
    return parser.parse_args()


def ignore(_directory: str, names: list[str]) -> set[str]:
    ignored = {name for name in names if name in EXCLUDED_DIRS}
    ignored.update(name for name in names if Path(name).suffix.lower() in EXCLUDED_SUFFIXES)
    return ignored


def parse_frontmatter(skill_md: Path) -> tuple[str, str]:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not match:
        return skill_md.parent.name, "No description available."
    frontmatter = match.group(1)
    name_match = re.search(r'^name:\s*["\']?([^"\'\r\n]+)', frontmatter, re.MULTILINE)
    description_match = re.search(
        r'^description:\s*(?:"([^"]*)"|\'([^\']*)\'|([^\r\n]+))',
        frontmatter,
        re.MULTILINE,
    )
    name = name_match.group(1).strip() if name_match else skill_md.parent.name
    if description_match:
        description = next(group for group in description_match.groups() if group is not None).strip()
    else:
        description = "No description available."
    return name, re.sub(r"\s+", " ", description)


def classify(name: str, description: str) -> str:
    text = f"{name} {description}".lower()
    categories = [
        ("cybersecurity", ("security", "pentest", "malware", "forensic", "threat", "vulnerability", "incident", "soc", "mitre", "credential")),
        ("testing-quality", ("test", "tdd", "verification", "quality", "benchmark", "review")),
        ("agents-ai", ("agent", "llm", "prompt", "model", "mcp")),
        ("frontend-design", ("frontend", "react", "vue", "angular", "design", "ui", "motion")),
        ("backend-data", ("backend", "api", "database", "postgres", "mysql", "redis", "django", "fastapi")),
        ("devops-platform", ("docker", "kubernetes", "deployment", "git", "github", "ci", "cloud")),
        ("content-research", ("research", "article", "content", "marketing", "seo", "brand")),
        ("language-framework", ("python", "golang", "go ", "rust", "java", "kotlin", "swift", "perl", "cpp", "csharp")),
    ]
    for category, terms in categories:
        if any(term in text for term in terms):
            return category
    return "general"


def copy_skill(source: Path, destination: Path) -> None:
    if destination.exists():
        shutil.rmtree(destination, onexc=_on_rm_error)
    shutil.copytree(source, destination, ignore=ignore)


def _on_rm_error(func, path, exc_info) -> None:
    """Clear read-only bits so Windows can remove exported skill trees."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def main() -> None:
    args = parse_args()
    source = args.source.resolve()
    repo = args.repo.resolve()
    output = repo / "skills"
    output.mkdir(parents=True, exist_ok=True)

    records = []
    source_dirs = sorted(
        path for path in source.iterdir()
        if path.is_dir() and path.name != ".system"
    )
    expected = {path.name for path in source_dirs}
    for stale in output.iterdir():
        if stale.is_dir() and stale.name not in expected:
            shutil.rmtree(stale)

    for skill_dir in source_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        name, description = parse_frontmatter(skill_md)
        copy_skill(skill_dir, output / skill_dir.name)
        records.append(
            {
                "name": name,
                "folder": skill_dir.name,
                "description": description,
                "category": classify(name, description),
            }
        )

    counts = Counter(record["category"] for record in records)
    catalog = [
        "# Skill Catalog",
        "",
        f"Total: **{len(records)} skills**.",
        "",
        "## Categories",
        "",
        "| Category | Count |",
        "|---|---:|",
    ]
    for category, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        catalog.append(f"| {category} | {count} |")
    catalog.extend(
        [
            "",
            "## Complete catalog",
            "",
            "| Skill | Category | Description |",
            "|---|---|---|",
        ]
    )
    for record in records:
        description = record["description"].replace("|", "\\|")
        catalog.append(
            f"| [`${record['name']}`](../skills/{record['folder']}/SKILL.md) | "
            f"{record['category']} | {description} |"
        )
    (repo / "docs" / "CATALOG.md").write_text("\n".join(catalog) + "\n", encoding="utf-8")
    (repo / "manifest.json").write_text(
        json.dumps({"skill_count": len(records), "skills": records}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps({"exported": len(records), "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
