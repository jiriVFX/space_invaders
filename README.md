# Space Invaders
## My shot at the recreation of the first level of the legendary 1978 Space Invaders game.

Space Invaders is a simple looking game and does not have complicated game mechanics, so one can easily underestimate the effort that has to go into recreating it.
But there are a few hurdles one has to overcome in order to get close to the original game mechanics
## Moving the alien fleet
Moving the fleet line by line was surprisingly one of the hardest parts of the development process.
I tried using pygame.groups, lists and combinations of both, ended up using a single list and storing row and column data in each alien's object variables.
That caused other difficulties like detecting when all the rows of aliens touched side of the screen.

## Making destructable walls
Another challenging task was creating walls from separate "pixel" objects, to allow for their destruction.
All the wall blocks have to be placed in right locations to form the correct wall shapes.
In the original game, the wall "pixels" are removed on the exact location of pixels of explosion "sprite".
That would be hard to do using sprites as we have no control over separate sprite pixels location.
I solved the wall destruction by removing random wall "pixels" around the shot explosion.

The bottom HUD line is destructable too. In the original game, multiple hits are neccessary to destroy one block of the line.
I reduced this to one hit as I recreated only one level and wanted to make this effect bit more visible.
