import base64
from melo.api import TTS

class InferlessPythonModel:
    
    def initialize(self):
        # Speed is adjustable
        self.model = TTS(language='EN', device='auto')
        self.speaker_ids = self.model.hps.data.spk2id
        self.output_path = 'temp.wav'
        
    def infer(self, inputs):
        text = inputs["text"]
        self.model.tts_to_file(text, self.speaker_ids['EN-US'], self.output_path, speed=1.0)
        with open(self.output_path, 'rb') as file:
            # Read the file's content
            audio_data = file.read()
            # Encode the data
            base64_encoded_data = base64.b64encode(audio_data)
            # Convert bytes to string
            base64_message = base64_encoded_data.decode('utf-8')
        return {"generated_audio_base64":base64_message}
    def finalize(self,args):
        self.model = None
