# 021: Video futures to closed-loop action

**Status:** Planned after a functioning 018 baseline and usable 019 predictor; 020 comparison recommended.

Compare (A) the baseline, (B) VLA, and (C) the same action candidates ranked with a video/world-model score. Hold initial states, instructions, seeds, action limits and episode horizon fixed. Freeze the selection rule before evaluation.

Check whether predicted object/goal changes match the simulator, and whether predicted ranking matches actual outcomes. Measure success, recovery, invalid/action-limit violations, prediction and decision latency, and episode duration. Include plausible-but-physically-wrong predictions and timeouts.

Run all candidate actions inside simulation. A video score alone must never command a real robot. The exit report should answer whether world-model ranking improves closed-loop results over B, including failures and uncertainty. If it adds latency without better outcomes, report that.
