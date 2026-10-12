"""MCP server for Accessibility Tree & DOM Action Selector Synthesizer."""
import sys
import json
from client import AccessibilityTreeActionSynthesizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "synthesize_dom_action_selector",
                "description": "Synthesizes deterministic CSS/ARIA selectors from accessibility tree nodes",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "nodes": {"type": "array"},
                        "intent_keyword": {"type": "string"}
                    },
                    "required": ["nodes", "intent_keyword"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "synthesize_dom_action_selector":
            args = params.get("arguments", {})
            res = AccessibilityTreeActionSynthesizer.synthesize_action_targets(
                args.get("nodes", []),
                args.get("intent_keyword", "")
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
