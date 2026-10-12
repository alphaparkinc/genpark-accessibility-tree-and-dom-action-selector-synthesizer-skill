"""Example usage for Accessibility Tree & DOM Action Selector Synthesizer."""
from client import AccessibilityTreeActionSynthesizer

if __name__ == "__main__":
    nodes = [
        {"id": "nav-home", "role": "link", "text": "Home"},
        {"id": "submit-checkout", "role": "button", "aria_label": "Complete Checkout", "disabled": False}
    ]
    res = AccessibilityTreeActionSynthesizer.synthesize_action_targets(nodes, "checkout")
    print("Recommended Target:", res["recommended_target"])
