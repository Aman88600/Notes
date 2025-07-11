from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Words or short phrases
words = ["king", "queen", "man", "woman", "apple", "banana"]

# Get embeddings
embeddings = model.encode(words, convert_to_tensor=True)

# Print embeddings
print(embeddings)
# # Compare similarities
# similarity = util.cos_sim(embeddings[0], embeddings[1])  # king vs queen
# print(f"Similarity between 'king' and 'queen': {similarity.item():.4f}")
