<h3>Game Description</h3>
A game that involves the user playing music notes viewed on screen/on hand
<br>
Helpful in enabling musicians to figure out the notes
<br>
Serves as a game to teach kids how to play music
<br><br>
<h3>How to play your game</h3>
Just press and figure out the notes
<br><br>
<h3>Code Description</h3>
Sprite - Image size, inherits from the super class Widget<br>
Background - Contains the image, size, pos, inherits from Sprite. Update function scrolls the image in the -x direction, left<br>
Piano - Contains instance of background, and initiates a Clock event<br>
PianoApp - Contains several properties, 2 GridLayouts, 25 buttons that calls the music notes when on_pressed, the function is stopped when on_released, buttons are animated after released<br>
State Machine - did not use the SM lib, as an alternative, the OptionProperty is used
<br><br>
[Link to YouTube Video](https://youtu.be/knpYnUEL4Ys)
<br><br>
*Initially I wanted to convert the game into Android Apk to try to run it on my phone, but I could not troubleshoot the Buildozer in time
**The Phone Version contains my codes without the animation (since my app lags quite a bit)
