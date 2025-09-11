# Mini project 2
Game: Voces perdidas

Voces perdidas is an interactive decision-making game inspired by the video game Zork, where the player enters an ancient forgotten temple. Each step is accompanied by a soundscape with OpenAL, which envelops the player in an atmosphere of mystery and tension.

The player explores corridors, caves, and underground rivers, guided by whispers and shadows that seem to have a life of their own. The decisions determine the outcome: free the trapped voices, condemn yourself to eternal silence, or leave the temple without discovering its secrets.

## Story

The protagonist arrives at a temple covered in vines, forgotten by time. Inside, echoes of ancient voices resonate among statues, hidden passages, and shining altars.

As they advance, they must choose carefully: light the fire to ward off the shadows, follow the murmur of the river, or face the whispers calling their name. Each decision opens different paths and brings him closer to one of multiple endings.

## Objective

The objective of the game is to uncover the mystery of the temple and decide what to do with the voices trapped in its heart:

Free them and restore peace to the wasteland.

Destroy the altar and condemn the temple to eternal silence.

Stand still and be consumed by the shadows.

## Implementation

Language: Python

Audio: OpenAL for playing and spatializing sounds (left, right, behind, in front).

Structure: Graph of nodes represented in a JSON file that defines:

Narrative text.

Sound effects with position, gain, and loops.

Decision options that lead to different paths.

This approach allows for a branching narrative and an immersive experience thanks to 3D sound.
