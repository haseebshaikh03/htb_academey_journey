# Module 115 — Shells & Payloads
## BLOCKED remaining questions (52.94% reached, 9/17 sections)

- **Reverse Shells (hostname via RDP):** not resolved
- **Automating Payloads (interpreter name):** tried `cmd`, `cmd.exe`, `meterpreter`, "Meterpreter shell", "Command Prompt" — all rejected, no hint text available. Needs the exact string the grader expects — re-check section theory for how it names the interpreter.
- **Infiltrating Windows (EternalBlue flag):** target contention prevented completion
- **Infiltrating Unix/Linux (rConfig hostname):** target contention prevented completion
- **Laudanum (directory name):** not resolved
- **Antak (username):** not resolved
- **PHP Web Shells (gif filename):** not resolved
- **Live Engagement final assessment:** 6 of 7 questions unanswered

**Root cause for most of these:** account-wide single-target-slot contention (confirmed: other modules' Windows targets, all-ports-filtered/100%-ping-loss, kept appearing instead of this module's own spawn) while several modules were being run in parallel. Re-run this module alone to finish the target-gated questions.
