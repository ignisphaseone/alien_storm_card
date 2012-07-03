This is a digital version of a card and die game I plan on making.

Here's a modification from my mac! Here's another modification from my mac.

Now I want to push some stuff from Eclipse...

Okay, physical things to emulate and code, no timing programming required.

Dice. They're just cubes. Sometimes they're rolled and sometimes they show faces.

Ships. They will have actions, but they're primarily about their static data. What dice they have.

Difficult stuff to tackle; actions need to handle timing, and actions need to aggregate results.

Because programming things is easier for me to do, and allows me to have multiple playsessions regardless of physical location, and I can easily edit values and test quickly, I am using this as a method to test the structure and content of the game.

Dice have:
--name
--color
--sides
--faceup
--roll()
--reset()

Ships have:
--name
--description
--dice
--special actions

Turn Order:
--Recon (find new events, scan for targets)
--Scramble (Spend Dice for special actions)
--Attack (Roll dice)
--Resolve (Destroy Aliens)

Game Setup:
--One attack frigate, civilian ship card. (2 red dice, one black die.)
--select a game mode card to use. (survival, destination, etc.)
--grab 6 missiles and 6 civilians.
--Select a fleet card.
--Shuffle the events deck, and put five cards facedown onto the fleet card.

License
===
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" property="dct:title" rel="dct:type">Alien Storm</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.ignisphaseone.com" property="cc:attributionName" rel="cc:attributionURL">Eric Fong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.
