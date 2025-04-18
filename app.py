import base64
import os
from melo.api import TTS
import nltk

class InferlessPythonModel:    
    def initialize(self):
        nltk.download('averaged_perceptron_tagger_eng')
        self.models = {}
        self.speaker_ids = {}
        self.output_path = 'temp.wav'

    def infer(self, inputs):
        # 從 inputs dict 抓參數
        text = inputs["text"]
        language = inputs["language"]
        speed = inputs.get("speed", 1.0)

        # 如果尚未初始化該語言，才載入
        if language not in self.models:
            self.models[language] = TTS(language=language, device='auto')
            self.speaker_ids[language] = self.models[language].hps.data.spk2id

        model = self.models[language]
        speaker_id = list(self.speaker_ids[language].values())[0]

        # 合成語音
        model.tts_to_file(text, speaker_id, self.output_path, speed=speed)

        # 讀檔、轉 base64
        with open(self.output_path, 'rb') as file:
            audio_data = file.read()
            base64_message = base64.b64encode(audio_data).decode('utf-8')

        os.remove(self.output_path)

        return {
            "generated_audio_base64": base64_message
        }

    def finalize(self, args):
        self.models = None
