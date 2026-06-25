---
name: "cyber-training-lab-finder"
description: "Find and compare legal cybersecurity labs, vulnerable applications, CTFs, cyber ranges, courses, and practice platforms. Use when selecting a safe hands-on environment by topic, skill level, budget, hosting model, or learning objective."
---

# Cyber Training Lab Finder

Recommend legal, controlled cybersecurity practice environments that fit the learner's objective.

## Workflow

1. Clarify the learning goal, current level, preferred platform, budget, available hardware, and whether local installation is acceptable.
2. Search `references/training-labs.csv` or `references/training-labs.md` for candidate resources.
3. Shortlist three to five candidates based on topic fit, difficulty, setup effort, cost, and environment type.
4. Verify each shortlisted resource against its current official website before recommending it. The source catalog was last updated at commit `cc4a51028de1f2dc44c96b6004c721260b698c8e` on 2024-07-02; links and offerings may have changed.
5. Distinguish clearly between free, freemium, paid, self-hosted, downloadable, archived, and unavailable resources.
6. Explain why each option fits and provide a safe first exercise or learning sequence.

## Safety boundary

- Recommend only environments intentionally designed or explicitly authorized for security practice.
- Never treat a public production system as a practice target.
- Require the user to follow each platform's scope, rules, acceptable-use terms, and local law.
- Keep testing within the lab boundary. Do not provide instructions for pivoting from a lab into unrelated infrastructure.
- Prefer official project repositories and vendor pages over mirrors or unofficial downloads.

## Selection guidance

- For beginners, favor guided courses, browser-based labs, and intentionally vulnerable web applications.
- For web security, prioritize maintained OWASP projects and isolated vulnerable applications.
- For Active Directory, recommend dedicated lab environments with explicit attack simulation scope.
- For binary exploitation or reverse engineering, prefer downloadable challenges or local VMs with snapshots.
- For teams, compare cyber ranges by collaboration, reset capability, observability, and instructor support.
- For older or archived resources, label them as historical and suggest a maintained alternative.

## References

- Read `references/training-labs.csv` for filtering or programmatic comparison.
- Read `references/training-labs.md` for human-readable browsing.
- Preserve attribution under `references/SOURCE-LICENSE-MIT.txt`.
