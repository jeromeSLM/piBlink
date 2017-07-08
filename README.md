# piBlink
LED Blink system for raspberry

Ce projet décrit l'utilisation de leds avec un rapsberry type 1 à 3 avec broches GPIO

Langage utilisé :  
**Python**

Composants utilisés : 

1 raspberry Pi (avec broches GPIO) avec raspbian installé sur la µSD  
1 breadboard  
3 leds (1 rouge, 1 jaune, 1 bleue)  
3 résistances 100 ohm ou + jusqu'à 330 ohm  
5 cables male/male  
4 cables femelle/femelle  

Temps nécessaire au cablage : **environ 5 minutes**  
Temps nécessaire au codage : **environ 10 minutes**  

**électronique & connectique :**  
La masse est commune sortie de la borne GND (6)  
La première LED (rouge) sera alimentée via la borne 7  
La seconde LED (jaune) sera alimentée via la borne 11  
La troisième LED (bleue) sera alimentée via la borne 13  

**coding :**  
Le script blink_3led.py se lance via :  
> sudo python blink_3led.py

le script peut être trouvé ici : ![Script python](/scripts/blink_3led.py "Script python")

**Cablage**  
![Cablage breadboard](/images/schema_blinkled3.png?raw=true "Cablage breadboard")


![Alt text](/images/montage%203%20leds.jpg?raw=true "Optional Title")
