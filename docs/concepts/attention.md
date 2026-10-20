# Self-attention, cross-attention and transformer blocks

**Status: concept syllabus / no code implemented.**

## Key questions
- What are Q, K, V and the effect of scaling, masking and softmax in attention?
- Self-attention versus cross-attention: where do the queries and keys/values come from?
- What information is encoded by positional embeddings or positional geometry?
- How do attention variants control compute or constrain sampling in perception?

## Minimal exercise (future)
1. Work through a 2-token attention matrix by hand.
2. Implement a tiny scaled dot-product attention module with tensor-shape assertions and a numerical reference.
3. Compare self-attention and cross-attention with controlled inputs.
4. Trace one transformer-based detection or BEV model to show where features enter and queries update.

**Use in:** Grounding DINO, BEVFormer, SparseDrive. This is a *prerequisite concept* for those studies, **not** a claim that YOLO requires a Transformer.

**Evidence to add:** Q/K/V shape table, gradient sanity check, memory scaling and a measurable ablation.
