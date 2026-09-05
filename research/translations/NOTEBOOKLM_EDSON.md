# NotebookLM Edson — English Capability Summary

This project automates dense educational audio generation from NotebookLM notebooks, especially for humanities and technical books. Its central pattern is a two-phase fire-and-forget workflow: create many audio artifacts while recording IDs and status, then poll separately and download completed artifacts. This avoids holding a process open for each multi-minute generation job.

The Hub can generalize that pattern into provider-neutral job states (`created`, `processing`, `completed`, `downloaded`, `error`) with persisted metadata and rate-limit handling. The source README contains personal account, notebook, plan, and project identifiers; those details are deliberately omitted here and must never enter the Hub.
