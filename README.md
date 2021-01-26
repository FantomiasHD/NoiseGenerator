# NoiseGenerator
Ein Generator für Perlinnoise ähnlichen Rauschen 

## Scipts
### NoiseMain 
A class based script
**usage**:
```python
import NoiseMain
noise = NoiseMain.Noise(size, iterations, falloff, roughness, basecolor)
```  
**Methods**: 
```python
noise.generate()
``` 
>*generates new unsmoothed image. Needs to be called*  
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
>*Draws rectangles to generate bigger areas*  
```python
noise.generatePie(size)
``` 
>*Draws Pieslices to generate bigger areas*  
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
>*Shows help - Use the Information there*
-----

### loadingBar Package
**usage**
```python
from loadingbar import LoadingBar
Bar = LoadingBar(Name, Size, Goal, Level)
```
>*Goal: Max value (100%)*   
>*Level: Spaces added to the name to level the Bars*

**Methods:**
```python
LoadingBar.draw(state)
```
>*Draws the LoadingBar State=curr. percent*
```python
LoadingBar.finish()
```
>*Draws the that doesn't get deleted on next promt. Also shows Done! instead of 100%*

### Examples
|iterations | rectangle-size | roughness | output |
|:----------:|:----------------:|:-----------:|--------|
|2|0|5|![205](https://i.imgur.com/RX32N3H.png)|
|6|2|0|![620](https://imgur.com/ZJOMRBC.png)|
|7|1|8|![718](https://imgur.com/sYIqVFX.png)|
|9|8|9|![989](https://imgur.com/oQreVbx.png)|


## requirements
Pillow over 5.3



### Copyright Simon Felix Seeger
### Created 05/07/2020
