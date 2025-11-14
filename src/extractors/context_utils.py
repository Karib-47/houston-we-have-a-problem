thondef extract_context(raw_line: str) -> str:
    """
    Extract simple contextual metadata around a problem message.
    """
    if ":" in raw_line:
        parts = raw_line.split(":", 1)
        return parts[0].strip()
    return "general"