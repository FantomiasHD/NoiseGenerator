# NoiseGenerator

## Scipts
### NoiseMain 
A class based script
**usage**:
```python
import NoiseMain
noise = NoiseMain.Noise(size, iterations,  roughness)
```  
**Methods**: 
```python
noise.generate()
``` 
>*generates new unsmoothed image*  
```python
noise.smooth()
``` 
>*smoothes the generated image*  
```python
noise.generateEllipse(size)
``` 
>*Draws ellipses to generate bigger areas*  
```python
noise.generateRect(size)
``` 
>*Draws ellipses to generate bigger areas*  
```python
noise.seed(seed)
``` 
>*Defines a seed for noise generation*  
```python
noise.save(path, name)
``` 
>*Saves the Image with an png extension*  
```python
noise.show(title)
``` 
>*Previews the image with given title*  
   
### GenerateNose
Generator with argparse
**usage**
```batch
python3 GenerateNose.py -h
```
>*Shows help*

### Examples
|iterations | rectangle-size | roughness | output |
|:----------:|:----------------:|:-----------:|--------|
|2|0|5|![205](https://i.imgur.com/RX32N3H.png)|
|6|2|0|![620](https://imgur.com/ZJOMRBC.png)|
|7|1|8|![718](https://imgur.com/sYIqVFX.png)|
|9|8|9|![989](https://imgur.com/oQreVbx.png)|
