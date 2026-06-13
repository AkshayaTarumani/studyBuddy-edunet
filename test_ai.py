from ai_engine import explain_topic, summarize_text, generate_quiz, generate_flashcards

text = "Photosynthesis is the process by which plants make food using sunlight."

print("\n=== EXPLAIN ===")
print(explain_topic(text))

print("\n=== SUMMARY ===")
print(summarize_text(text))

print("\n=== QUIZ ===")
print(generate_quiz(text))

print("\n=== FLASHCARDS ===")
print(generate_flashcards(text))