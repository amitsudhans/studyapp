with open('app/Http/Controllers/MultimediaController.php', 'r') as f:
    text = f.read()

text = text.replace("'Newton's First Law of Motion: Inertia and Mass'", "'Newton\\'s First Law of Motion: Inertia and Mass'")
text = text.replace("'Newton's Second Law of Motion: Momentum & F = ma'", "'Newton\\'s Second Law of Motion: Momentum & F = ma'")
text = text.replace("'Newton's Third Law of Motion: Action & Reaction Pairs'", "'Newton\\'s Third Law of Motion: Action & Reaction Pairs'")

with open('app/Http/Controllers/MultimediaController.php', 'w') as f:
    f.write(text)
print('Escapes fixed!')
