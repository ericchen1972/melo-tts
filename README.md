# Deploy MeloTTS using Inferless
MeloTTS is an open-source multi-lingual text-to-speech (TTS) library developed by MyShell.ai. It delivers high-quality, natural-sounding speech synthesis across a range of languages—including various English accents (American, British, Indian, and Australian), Spanish, French, Chinese, Japanese, and Korean. Optimized for fast, real-time inference.

## TL;DR:
- GitHub/GitLab template creation with `app.py`,`input_schema.py` and `inferless.yaml`.
- Model class in `app.py` with `initialize`, `infer`, and `finalize` functions.
- Recommended GPU: NVIDIA T4 for optimal performance.
- Final review and deployment on the Inferless platform.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the `Add a custom model` button.

- Select `Github` as the method of upload from the Provider list and then select your Github Repository and the branch.
- Choose the type of machine, and specify the minimum and maximum number of replicas for deploying your model.
- Choose Volume, Secrets and set Environment variables like Inference Timeout / Container Concurrency / Scale Down Timeout
- Once you click “Continue,” click Deploy to start the model import process.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.

## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.

```bash
curl --location '<your_inference_url>' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <your_api_key>' \
    --data '{
              "inputs": [
                  {
                      "name": "prompt",
                      "shape": [
                          1
                      ],
                      "data": [
                          "Hello there! How are you doing?"
                      ],
                      "datatype": "BYTES"
                  }
              ]
}'
```
---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu.

For more information refer to the [Inferless docs](https://docs.inferless.com/).
