
import json, os
import openal

class Node:
    def __init__(self, id, text, sounds, options):

        self._id = id
        self._text = text
        self._sounds = sounds
        self._options = options

    def get_id(self): 
        return self._id
    
    def get_text(self): 
        return self._text
    
    def get_options(self): 
        return self._options

    def play(self, audio_path):

        files = []
        for i in self._sounds:

            route = os.path.join(audio_path, i["file"])
            src = openal.oalOpen(route)
            if "gain" in i:
                src.set_gain(float(i["gain"]))
            if "pos" in i:  
                src.set_position(tuple(i["pos"]))
            if "loop" in i: 
                src.set_looping(bool(i["loop"]))
            src.play()
            files.append(src)
        return files


    def stop(self, fuentes):

        for src in fuentes:
            src.stop()

class Graph:
    def __init__(self):
        self._nodes = {} 

    def add(self, node): 
        self._nodes[node.get_id()] = node

    def get(self, node_id): 
        return self._nodes[node_id]

def story(path_json, audio_path):
    with open(path_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    g = Graph()
    start = data["start"]

    for node_id, content in data["nodes"].items():
        text = content["text"]
        sounds = content["sounds"]  
        options = list(content["options"].items())
        g.add(Node(node_id, text, sounds, options))

    return g, start, audio_path

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    story_path = os.path.join(base, "story.json")
    audio_path = os.path.join(base, "audio")

    g, current, audio_path = story(story_path, audio_path)
    sources = []
    playing = True 

    while playing:
        nodo = g.get(current)
        if not nodo:
            print("(error) nodo no encontrado:", current)
            playing = False

        if sources:
            nodo.stop(sources)
            sources = []

        print(f"\n===== {nodo.get_id().upper()} =====\n")
        for line in nodo.get_text():
            print(" -", line)

        sources = nodo.play(audio_path)

        options = nodo.get_options()

        print("\nOpciones:")
        for i, (label, _) in enumerate(options, 1):
            print(f" {i}. {label}")
        print("\nEscribe 'salir' para terminar.")

        command = input("\n> ").strip().lower()

        if command in ("salir", "exit", "quit"):
            playing = False
        elif command.isdigit():
            index = int(command) - 1
            if 0 <= index and index < len(options):
                current = options[index][1]
            else:
                print("Número inválido.")

if __name__ == "__main__":
    main()

