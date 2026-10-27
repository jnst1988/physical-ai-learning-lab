# 019: Video world-model study on PushT

**Status:** Planned after 018 saves episodes and the baseline.

## Distinguish the prediction targets

- **Latent prediction:** an action-conditioned model predicts future representations; those outputs need not decode into video. V-JEPA 2-AC and RoboJEPA are study candidates.
- **Pixel/video prediction:** a model generates visible future frames. Boundless World Model is a candidate; its published inference uses CUDA and a Wan2.2 TI2V 5B base model.

A generic text-to-video clip is not an action-conditioned robot world model. It cannot answer whether a given action caused the predicted change.

## Procedure

1. Pin official code revision, checkpoint, terms and hardware requirements.
2. Freeze observation histories and action windows from 018 episodes.
3. Run the documented action-conditioned inference; save predicted and actual continuation side by side.
4. Confirm that the model consumes the action as an input, rather than only a text prompt.
5. Report task-state agreement separately from visual quality, plus latency, peak memory and any frame resizing.

## Local-resource gate

Check the official inference setup before downloading multi-gigabyte weights. If CUDA or memory is unavailable, record the exact blocker and keep the 018 replay/data-contract demo. A lightweight placeholder can test the interface, but label it as a pipeline prototype rather than a reproduction of the large model.

## Exit evidence

One real, pinned model run on saved task data, actual-versus-predicted clips, per-case metrics and measured resource use. Otherwise mark full inference as blocked by a named hardware/software requirement.
