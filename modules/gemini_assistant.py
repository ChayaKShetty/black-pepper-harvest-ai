"""
Gemini AI Assistant Module for Pepper Harvest AI
Connects to Google Gemini API to provide expert black pepper farming guidance.
Uses genuine Gemini responses strictly aligned with agronomic science.
"""

import os
from typing import List, Dict, Any, Tuple, Optional
import dotenv

dotenv.load_dotenv(override=True)

PEPPER_SYSTEM_INSTRUCTION = """You are 'Pepper Farming Assistant', a dedicated, highly knowledgeable agricultural expert in black pepper (Piper nigrum) cultivation and harvest management.

Your primary purpose is to help farmers, plantation managers, and students with practical, scientific, and actionable guidance specifically focused on:
1. Black pepper maturity identification and harvest timing.
2. Propagation techniques (serpentine layering, bamboo split method, rapid multiplication, single-node stem cuttings).
3. Soil and climate requirements (laterite, sandy loam, pH 5.5-6.5, high humidity, warm tropical climate).
4. Support tree standards (Erythrina indica, Garuga pinnata, Silver Oak, teak) and vine training/pruning.
5. Irrigation and moisture conservation (drip irrigation, mulching).
6. Organic manure, biofertilizers (Trichoderma, VAM), and balanced NPK fertilizer management.
7. Integrated pest management (pollu beetle, scale insects, top shoot borer, nematodes).
8. Critical disease prevention and treatment (Quick Wilt / Phytophthora foot rot, Slow Decline, Anthracnose / Pollu disease, stunt virus).
9. Post-harvest operations (threshing, hot water blanching at 80°C for 1 minute for rapid uniform blackening, sun-drying to 10-12% moisture, sorting, grading, vacuum packaging, and storage).

Guidelines:
- Explain answers in clear, accessible, respectful English that any beginner farmer can understand.
- Provide step-by-step instructions where actionable.
- Prioritize safety, sustainable practices, and biological controls before advising chemical treatments.
- If a user asks a question completely unrelated to black pepper, agriculture, farming, crops, botany, or spice processing, politely reply:
  "I am specialized specifically as the Pepper Farming Assistant. I can only assist with questions regarding black pepper cultivation, harvest readiness, crop health, processing, and related agricultural practices. Please let me know how I can help with your pepper plantation!"
- Never fabricate responses. Provide accurate agronomic guidance.
"""

SUGGESTED_QUESTIONS = [
    "How do I grow black pepper?",
    "Which soil is suitable for black pepper?",
    "How can I control foot rot?",
    "When should I harvest black pepper?",
    "How should black pepper be dried?",
    "What are the different propagation methods?"
]


class GeminiAssistant:
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
        self._client = None
        self._initialized = False

    def is_configured(self) -> Tuple[bool, str]:
        """Checks if GEMINI_API_KEY is configured."""
        if not self.api_key:
            return False, "GEMINI_API_KEY is not configured. Please enter your API key to connect to the Pepper Farming Assistant."
        return True, "Configured"

    def _get_client(self):
        """Initializes Google GenAI client."""
        if self._client is None and self.api_key:
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                # Fallback to google.generativeai if genai fails
                try:
                    import google.generativeai as genai_legacy
                    genai_legacy.configure(api_key=self.api_key)
                    self._client = genai_legacy
                except Exception as inner_e:
                    raise RuntimeError(f"Failed to initialize Gemini client: {e} / {inner_e}")
        return self._client

    def generate_response(self, user_prompt: str, history: Optional[List[Dict[str, str]]] = None) -> Tuple[bool, str]:
        """
        Generates genuine AI response from Gemini API using conversation history.
        history format: list of {'role': 'user'|'assistant'|'model', 'content': '...'}
        """
        configured, msg = self.is_configured()
        if not configured:
            return False, msg

        client = self._get_client()
        if not client:
            return False, "Gemini client could not be initialized."

        try:
            # Modern google-genai approach
            from google import genai
            if isinstance(client, genai.Client):
                # Build contents list
                contents = []
                if history:
                    for msg in history:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append({
                            "role": role,
                            "parts": [{"text": msg["content"]}]
                        })
                # Add current user prompt
                contents.append({
                    "role": "user",
                    "parts": [{"text": user_prompt}]
                })

                # Models ordered by current availability & speed
                models_to_try = [
                    self.model_name,
                    "gemini-flash-lite-latest",
                    "gemini-3.5-flash-lite",
                    "gemini-flash-latest",
                    "gemini-3.8-flash",
                    "gemini-2.5-flash",
                ]
                # Filter duplicates while preserving order
                unique_models = []
                for m in models_to_try:
                    if m and m not in unique_models:
                        unique_models.append(m)

                last_err = ""
                for m in unique_models:
                    try:
                        response = client.models.generate_content(
                            model=m,
                            contents=contents,
                            config={
                                "system_instruction": PEPPER_SYSTEM_INSTRUCTION,
                                "temperature": 0.3,
                            }
                        )
                        if response and response.text:
                            return True, response.text
                    except Exception as err:
                        last_err = str(err)
                        continue
                return False, f"Gemini API error: {last_err}"

            else:
                # Legacy google.generativeai approach
                import google.generativeai as genai_legacy
                model = genai_legacy.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=PEPPER_SYSTEM_INSTRUCTION
                )
                chat = model.start_chat(history=[])
                response = chat.send_message(user_prompt)
                return True, response.text

        except Exception as e:
            return False, f"Failed to generate response from Gemini API: {str(e)}"

