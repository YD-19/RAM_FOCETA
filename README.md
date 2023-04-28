# RAM for FOCETA
Reliability assessment for FOCETA Object detection Models

## Environment Installation
First of all, please set up a conda environment
```
conda env create -f environment.yml 
conda activate UWVFOCETA
pip install torchsummary==1.5.1
pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
```

## Fetch the Code
Fetch the source code for the reliabity assessment of UWV by run:
```
git clone https://github.com/Solitude-SAMR/UWV_RAM
```

## Prepare the Dataset
Download the dataset and trained model weight from FOCETA project:

Unzip the folder and add to the directory follow by the config file at "data/foceta.data"

The label format of our demo code is different from original FOCETA Prescan dataset, but it can be automatically transferred by using the following script:

```
python data/FOCETA/labelswitch.py
```

## Train the UWV Model and VAE Model
To train the yoloV3 model by yourself for UWV object detection, run
```
python -m pytorchyolo.train
```
To train the variantional autoencoder model by yourself to compress the UWV simulation images, run
```
python uwv_vae.py
```

hint: You can use the following script to control the GPU id:
```
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```

## Test the Reliability of Object Detection Model 
run the following command to start testing:
```
python uwv.py
```
When the program is running, all test result for each demand (image) is saved to the output folder with format (latent_represenation, x_class, pmi). pmi is the abbreviation probabity of misclassification per input. Then you can visualize the robustness verification results of all the inputs, the update of reliability (pmi) by running
```
python plot.py
```

