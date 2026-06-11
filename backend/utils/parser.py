import json

def safe_json_parse(text):

    try:

        if not text:
            return {}

        text = str(text)

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print(
            f"JSON Parse Error: {str(e)}"
        )

        print(
            f"Raw Response: {text}"
        )

        return {}