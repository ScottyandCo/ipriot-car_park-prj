# Moondalup Car Park Project

##### This project will meet the requirements set out in the Assessment Document.

### Project Description
> This project is to create a "smart car park" that is able to:
>  - track vehicles entering and exiting,
>  - log vehicle license plates, and
>  - display information to vehicles regarding car park status (available bays).
>
> 
> The above is achieved by having 3 functional items
>  - the car park,
>    - this is where the information relevant to the car park is stored (configuration)
>      - location,
>      - number of bays,
>      - list of license plates,
>      - list of entry and exit sensors, and
>      - list of displays. 
>  - entry and exit sensors,
>    - these sensors are used to scan license plates of vehicles entering and exiting the car park
>    - they return information to the car park to add or remove a vehicle from the lists and return the
>    number of available bays.
>  - display(s).
>    - the displays are used to display an initial welcome message, and
>    - show the current number of available bays to entering vehicles.
>

### Basic Project Flow
```mermaid
flowchart TD
    A(Start) --> B(Sensor detects vehicle) --> C{Vehicle is entering}
    C -- True --- T1[Add license plate to list] --> G
    C -- False --- F1[Remove license plate from list] --> G
    G[Determine number of vehicles and \n number of available bays] --> H[Update display]
    H --> E(End)
```
### Project Roadmap
> Distinguish between vehicle types.
> 
> Add emojis to license plate list (change to dict) to identify different vehicles. 🚗 🏍️
> 
> Add bays for specific types of vehicles (motorbikes/cars).
> 
> Display to scroll through information over a specified time period
>   - number of available car bays,
>   - number of available motorbike bays,
>   - current weather,
>   - advertising/customer message.

### Overview

>The City of Moondalup is progressively embracing smart city initiatives 
to enhance urban living, improve efficiency in city services, and promote 
sustainable practices. As part of this initiative, the city council is eager 
to transition to a smart parking solution to optimize car park usage, reduce 
traffic congestion, and enhance the overall parking experience for residents 
and visitors.
>
>The City of Moondalup is progressively embracing smart city initiatives to enhance 
urban living, improve efficiency in city services, and promote sustainable practices. 
As part of this initiative, the city council is eager to transition to a smart parking 
solution to optimise car park usage, reduce traffic congestion, and enhance the overall 
parking experience for residents and visitors.
>
>You have been contracted to create a prototype solution that uses sensors and displays 
to provide timely information about available parking bays as well as relevant information
about weather and other community messages.

### Application requirements

>- [x] The system must accurately track the status of each parking bay in real-time.
>- [x] The display must be updated promptly as cars enter or exit.
>- [x] The system should be robust, easy to maintain, and scalable for future enhancements.
>- [x] The application must follow best coding practices and include unit testing.
>- [x] You must use Git and Github for version management. 

### Coding requirements

>- [x] Create at least three classes.
>- [x] At least one class must include three or more parameters.
>- [x] At least one class must aggregate another class.
>- [x] You should demonstrate an example of polymorphism
>- [x] Include at least two unit cases
>- [x] Create a main.py demonstrating the core interaction between instances of your 
classes
>- [x] Use PEP8 throughout your code and docstrings for major functions within your code

### Version control requirements

>- [x] Create a new repository and configure it with a README, .gitignore, and other 
essential setup files.
>- [x] Initialize your local repository and link it to a remote repository on GitHub.
>- [x] Make initial commits with the basic structure of your car park system.
>- [x] As you develop the system, commit your changes each time you reach a significant
milestone or complete a task.
>- [x] Make at least three commits to demonstrate the evolution of your project.
>- [x] Manage any changes or improvements by committing to the repository with clear, 
descriptive commit messages.