# ProjectPangu

## Abstract

```
天地浑沌如鸡子，盘古生其中。
万八千岁，天地开辟，阳清为天，阴浊为地。
盘古在其中，一日九变，神于天，圣于地。
天日高一丈，地日厚一丈，盘古日长一丈，如此万八千岁。
天数极高，地数极深，盘古极长，后乃有三皇。
数起于一，立于三，成于五，盛于七，处于九，故天去地九万里。
```

This is a random world generator which would create an Earth-like world.

Steps towards a random world:

### Cast from Sphere to Grid
- Coordinate
- Cosine correct

### Continental Drift
- Determine the composition of the planet
- How many plate
- How the plates move
- How their relative motion
- Where to raise, where to sink
- How 'raising' and 'sinking' spread further

### Water Coverage
- Mountains, sea level, and oceans
- Three-cell circulation
- Temperature assumption
- Change of season
- Wind, rain, and iced lands
- Finally, we can generate rivers and lakes

### Ecological Communities
- Nature environment based on terrain
- Plants
- Animals
- Resources

### Additional Events
- Earthquake and volcano activities
- Comet strike
- ???

### Born of Intelligent Creatures
- Project Nvwa


## Design

### Core Library

The core of this project is a library (package) to generate a "map" in the form of list.  
Each element of the "map" describes the status of the position.  
The status of the "map" at the next time tick should be derived from current status.  
The status of elements in the "map" are affected by adjacent elements (Cellular Automata).  
Map element may have periodic status, which changes periodically.  

The library would provide:  
- the definition of the "map";  
- an api to initialize a "map" randomly from scratch;  
- an api to initialize a "map" by parsing a text file;  
- an api to "merge" two "map"s of the same size (for editing the "map" manually);  
- an api to derive the status of a given "map" at the next time tick (stepwise);  
- an api to derive the status of a given "map" at a specific time in future;  
- an api to add periodic effects on the map (the effect not suit to described by element status).  

### Visualizing and Controlling

Besides the core library, we need some tools to monitor and control the generation and derivation process.  
We can make use of these modules in other projects in the future.  

#### Screen

- Assign an area of the window for a specific use.  
- Register multiple screens to the application.  
- Layer management.  
- When user actions are caught by the application, the actions are forwarded to affected screen.  

#### Button and Button Group

- Including different control elements, including button, scroller, and so on.  
- Some items are mutual exclusive or strongly related, they should be managed as a group.  
- Register multiple button groups to the screen they are allocated.  
- When user actions are forwarded to the screen, the actions are forwarded to affected button group.  

#### Action Simulator

- Simulate a series of designed actions to the application.  

#### Video Recorder

- Record the whole or part of the application window, and generate a video file in selected format to be uploaded to social media platform.  
- Enable adding subtitiles if possible.  

### Demonstration Application

- 

## Implementation


## Tutorial


## Troubleshooting


## References


