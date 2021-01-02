# NoiseGenerator

## Scipts
### NoiseMain 
A class based script
**usage**:
```python
import NoiseMain
noise = NoiseMain.Noise(size, iterations,  smoothVal)
```  
**Methods**: 
```python
noise.generate()
``` 

*generates new unsmoothed image*  
```python
noise.smooth()
``` 
*smoothes the generated image*  
```python
noise.generateEllipse(size)
``` 
*Draws ellipses to generate bigger areas*  
```python
noise.generateRect(size)
``` 
*Draws ellipses to generate bigger areas*  
```python
noise.seed(seed)
``` 
*Defines a seed for noise generation*  
```python
noise.save(path, name)
``` 
*Saves the Image with an png extension*  
```python
noise.show(title)
``` 
*Previews the image with given title*  
