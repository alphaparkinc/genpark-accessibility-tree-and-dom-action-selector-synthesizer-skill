"""Accessibility Tree & DOM Action Selector Synthesizer.
100% Python Standard Library.
"""

class AccessibilityTreeActionSynthesizer:
    """Converts raw DOM / ARIA accessibility nodes into deterministic selector action plans for browser agents."""

    @staticmethod
    def synthesize_action_targets(nodes: list, intent_keyword: str) -> dict:
        interactive_roles = {"button", "link", "textbox", "checkbox", "combobox", "menuitem"}
        candidates = []
        kw = intent_keyword.lower().strip()

        for idx, node in enumerate(nodes):
            role = node.get("role", "").lower()
            label = node.get("aria_label") or node.get("text") or ""
            node_id = node.get("id", f"el_{idx}")
            disabled = bool(node.get("disabled", False))

            if role not in interactive_roles or disabled:
                continue

            score = 0.5
            if kw and kw in label.lower():
                score += 0.45
            if node.get("id"):
                score += 0.05

            selector = f"#{node['id']}" if node.get("id") else f"[role='{role}'][aria-label='{label}']"
            candidates.append({
                "node_id": node_id,
                "role": role,
                "label": label,
                "selector": selector,
                "confidence": round(min(1.0, score), 2)
            })

        candidates.sort(key=lambda x: x["confidence"], reverse=True)
        return {
            "intent_keyword": intent_keyword,
            "interactive_candidates_count": len(candidates),
            "recommended_target": candidates[0] if candidates else None,
            "all_candidates": candidates
        }
