import json
import re


def parse_json(text: str):

    try:
        return json.loads(text)

    except Exception:

        # Remove markdown code blocks

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        # Remove trailing commas

        text = re.sub(
            r",(\s*[}\]])",
            r"\1",
            text
        )

        # Extract JSON object

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:

            return json.loads(
                match.group()
            )

        raise ValueError(
            "Could not parse JSON response"
        )