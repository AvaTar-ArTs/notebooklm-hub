# AcademIA — English Capability Summary

AcademIA is a local academic-study platform designed as a NotebookLM-like system. It imports complete books and media (PDF, EPUB, DOCX, text, images, audio, and video), indexes them for semantic and hybrid retrieval, and exports study materials as Markdown.

Its most valuable design lesson is resilience: when an LLM or embedding service is unavailable, it falls back to offline hash embeddings, keyword search, or chat without tool calling. It also emphasizes local-first storage, interchangeable Ollama/OpenAI-compatible providers, persisted progress for long-running jobs, and artifact outputs that remain exportable.

Useful Hub adaptations are fallback policies, multimodal source metadata, chapter-aware map/reduce jobs, clickable citation identifiers, and provider health checks. The snapshot itself is not vendored.
