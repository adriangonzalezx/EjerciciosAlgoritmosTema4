import heapq
from collections import defaultdict

class Node:
    def __init__(self, symbol=None, frequency=None, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_frequency_table(symbols, frequencies):
    frequency_table = defaultdict(float)
    for symbol, frequency in zip(symbols, frequencies):
        frequency_table[symbol] = frequency
    return frequency_table

def build_huffman_tree(frequency_table):
    heap = [Node(symbol, frequency) for symbol, frequency in frequency_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(frequency=left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(heap, parent)

    return heap[0]

def generate_huffman_codes(tree, prefix="", codes={}):
    if tree.symbol is not None:
        codes[tree.symbol] = prefix
    else:
        generate_huffman_codes(tree.left, prefix + "0", codes)
        generate_huffman_codes(tree.right, prefix + "1", codes)

def compress_message(message, codes):
    compressed_message = ""
    for symbol in message:
        compressed_message += codes[symbol]
    return compressed_message

def decompress_message(compressed_message, tree):
    decompressed_message = ""
    current_node = tree
    for bit in compressed_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol is not None:
            decompressed_message += current_node.symbol
            current_node = tree

    return decompressed_message

# Define the symbol frequencies
symbols = ["A", "F", "1", "3", "0", "M", "T"]
frequencies = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

# Build the frequency table
frequency_table = build_frequency_table(symbols, frequencies)

# Build the Huffman tree
huffman_tree = build_huffman_tree(frequency_table)

# Generate the Huffman codes
huffman_codes = {}
generate_huffman_codes(huffman_tree, codes=huffman_codes)

# Compress a message
message = "AFTM"
compressed_message = compress_message(message, huffman_codes)
print("Compressed message:", compressed_message)

# Decompress a message
decompressed_message = decompress_message(compressed_message, huffman_tree)
print("Decompressed message:", decompressed_message)
