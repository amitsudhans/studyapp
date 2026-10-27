with open('app/Http/Controllers/MultimediaController.php', 'r') as f:
    text = f.read()

text = text.replace("Freytag's narrative pyramid", "Freytag\\'s narrative pyramid")
text = text.replace("Show-Don't-Tell Imagery", "Show-Don\\'t-Tell Imagery")

with open('app/Http/Controllers/MultimediaController.php', 'w') as f:
    f.write(text)
print('English escapes fixed!')
