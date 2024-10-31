import heapq
from collections import Counter
import tkinter as tk
from tkinter import filedialog, Toplevel, Scrollbar, Text
import os

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def calculate_character_frequencies(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().replace('\ufeff', '')
    return Counter(content), content

def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return heapq.heappop(priority_queue)

def generate_huffman_codes(root, current_code='', huffman_codes={}):
    if root is None:
        return
    if root.character is not None:
        huffman_codes[root.character] = current_code
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)
    return huffman_codes

def encode_text(content, codes):
    return ''.join(codes[char] for char in content)

def decode_text(encoded_content, root):
    decoded_content = []
    node = root
    for bit in encoded_content:
        node = node.left if bit == '0' else node.right
        if node.character is not None:
            decoded_content.append(node.character)
            node = root
    return ''.join(decoded_content)

def display_message(title, message, bg_color, fg_color):
    message_window = Toplevel()
    message_window.title(title)
    message_window.configure(bg=bg_color)
    text_widget = Text(message_window, wrap="word", height=10, width=50, bg=bg_color, fg=fg_color)
    text_widget.insert("end", message)
    text_widget.config(state="disabled")
    text_widget.pack(pady=10, padx=10)

def display_frequencies_and_codes(frequencies, huffman_codes):
    window = Toplevel()
    window.title("Frecuencias y Códigos de Huffman")
    text_widget = Text(window, wrap="none", width=50)
    scrollbar = Scrollbar(window, orient="vertical", command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)
    text_widget.insert("end", f"{'Character':<10} {'Frecuencia':<10} {'Código Huffman':<20}\n")
    text_widget.insert("end", "-" * 40 + "\n")
    for char, freq in frequencies.items():
        code = huffman_codes[char]
        text_widget.insert("end", f"{repr(char):<10} {freq:<10} {code:<20}\n")
    text_widget.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def compress_file(file_path):
    frequencies, original_content = calculate_character_frequencies(file_path)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_content = encode_text(original_content, huffman_codes)

    #Guardar frecuencias como encabezado en el archivo comprimido
    output_path = os.path.splitext(file_path)[0] + "_comprimido.txt"
    with open(output_path, 'w') as file:
        file.write(str(frequencies) + "\n")
        file.write(encoded_content)
    
    original_size = len(original_content) * 8  # En bits
    compressed_size = len(encoded_content)  # En bits
    display_message("Compresión completada", f"Compresión exitosa.\nTamaño original: {original_size} bits\nTamaño comprimido: {compressed_size} bits\nArchivo guardado en: {output_path}", bg_color="PaleGreen3", fg_color="black")
    display_frequencies_and_codes(frequencies, huffman_codes)

def decompress_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    #Recuperar frecuencias desde el encabezado
    frequencies = eval(lines[0].strip())
    encoded_content = ''.join(lines[1:])
    huffman_tree = build_huffman_tree(frequencies)
    decoded_content = decode_text(encoded_content, huffman_tree)
    
    output_path = file_path.replace("_comprimido.txt", "_decodificado.txt")
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(decoded_content)
    display_message("Decodificación completada", f"El archivo fue decodificado correctamente y guardado en: {output_path}", bg_color="PaleGreen3", fg_color="black")

def select_and_compress_file():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        if not file_path.endswith(".txt"):
            display_message("Error de formato", "Solamente se permiten archivos .txt", bg_color="red3", fg_color="white")
            return
        compress_file(file_path)

def select_and_decompress_file():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto comprimidos", "*_comprimido.txt")])
    if file_path:
        if not file_path.endswith("_comprimido.txt"):
            display_message("Error de formato", "Seleccione un archivo comprimido (_comprimido.txt)", bg_color="red", fg_color="white")
            return
        decompress_file(file_path)

#Interfaz gráfica
root = tk.Tk()
root.title("Compresor & Descompresor de archivos Huffman")
root.geometry("400x180")
root.configure(bg="#34495e")
button_color = "#ecf0f1"
text_color = "#34495e"

compress_button = tk.Button(root, text="Seleccionar archivo y comprimir", command=select_and_compress_file, bg=button_color, fg=text_color, font=("Arial", 10, "bold"))
compress_button.pack(pady=15)
decompress_button = tk.Button(root, text="Seleccionar archivo y decodificar", command=select_and_decompress_file, bg=button_color, fg=text_color, font=("Arial", 10, "bold"))
decompress_button.pack(pady=15)
root.mainloop()
