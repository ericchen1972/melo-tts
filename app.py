import base64
from melo.api import TTS
import nltk
import os

class InferlessPythonModel:    
    def initialize(self):
        nltk.download('averaged_perceptron_tagger_eng')
        self.models = {}
        self.speaker_ids = {}
        self.output_path = 'temp.wav'
        
        # 預先載入所有語言的模型
        for lang in ['EN', 'ZH', 'FR', 'JP', 'KR']:
            model = TTS(language=lang, device='auto')
            self.models[lang] = model
            self.speaker_ids[lang] = model.hps.data.spk2id
        
    def infer(self, inputs):
        text = inputs["text"]
        language = inputs.get("language", "EN")  # 預設使用英文
        
        model = self.models.get(language)
        speakers = self.speaker_ids.get(language)
        
        if not model or not speakers:
            raise ValueError(f"Unsupported language: {language}")
        
        speaker_id = list(speakers.values())[0]  # 預設取第一個 speaker
        
        model.tts_to_file(text, speaker_id, self.output_path, speed=0.75)
        
        with open(self.output_path, 'rb') as file:
            audio_data = file.read()
            base64_encoded_data = base64.b64encode(audio_data)
            base64_message = base64_encoded_data.decode('utf-8')
            
        os.remove(self.output_path)
        return {
            "generated_audio_base64": base64_message
        }

    def finalize(self, args):
        self.models = None
