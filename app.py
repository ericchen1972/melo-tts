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
        return {"generated_audio":"Done"}
    def finalize(self,args):
        self.model = None
