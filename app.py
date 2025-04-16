import base64
from melo.api import TTS
import nltk
import os

class InferlessPythonModel:    
    def initialize(self):
        #nltk.download('averaged_perceptron_tagger_eng')
        self.model = TTS(language='ZH', device='auto')
        self.speaker_ids = self.model.hps.data.spk2id
        self.output_path = 'temp.wav'
        
    def infer(self, inputs):
        text = inputs["text"]
        #speaker_key = list(self.speaker_ids.keys())[0]
        self.model.tts_to_file(text, self.speaker_ids['ZH'], self.output_path, speed=0.7)
        
        with open(self.output_path, 'rb') as file:
            audio_data = file.read()
            base64_encoded_data = base64.b64encode(audio_data)
            base64_message = base64_encoded_data.decode('utf-8')
            
        os.remove(self.output_path)
        return {
            "generated_audio_base64":base64_message
        }

    def finalize(self,args):
        self.model = None
