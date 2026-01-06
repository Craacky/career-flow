import json
import httpx
from app.core.config import settings


class AiService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.AI_API_KEY
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "mistralai/devstral-2512:free"

    def analyze_resume(self, extracted_text: str) -> dict:
        prompt = f"""
                Analyze this resume and provide feedback in JSON format:

                RESUME:
                {extracted_text}

                Respond with JSON:
                {{
                    "strengths": ["...", "..."],
                    "improvements": ["...", "..."],
                    "recommendations": ["...", "..."],
                    "score": 0-100
                }}
                """
        try:
            response = self._call_api(prompt)
            return self._parse_response(response)
        except (httpx.HTTPStatusError, json.JSONDecodeError, KeyError):
            return self._default_analysis()

    def _call_api(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a resume expert"},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500
        }

        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/chat/completions",
                json=data,
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()

            result = response.json()
            return result["choices"][0]["message"]["content"]

    def _parse_response(self, response: str) -> dict:
        try:
            start = response.find("{")
            end = response.rfind("}") + 1
            json_str = response[start:end]
            return json.loads(json_str)
        except json.JSONDecodeError:
            return self._default_analysis()

    @staticmethod
    def _default_analysis() -> dict:
        return {
            "strengths": ["Resume provided"],
            "improvements": ["Add more details"],
            "recommendations": ["Include projects", "Add links"],
            "score": 50
        }
