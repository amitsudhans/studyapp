with open("resources/views/components/layouts/app.blade.php", "r", encoding="utf-8") as f:
    text = f.read()

target = """                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                }

                if (iframe.src !== fileUrl) {"""

replacement = """                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class7-math-number-play' || type === 'chapter6-math-class7' || type === 'number-play' || type === 'class7-number-play' || type === 'number-play-class7' || type === 'class7-math-playing-with-numbers' || type === 'playing-with-numbers-class7') {
                    fileUrl = "{{ asset('animations/class7-math-number-play.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 6: Number Play Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 shrink-0";
                }

                if (iframe.src !== fileUrl) {"""

assert target in text, "target not found in app.blade.php"
text = text.replace(target, replacement, 1)

with open("resources/views/components/layouts/app.blade.php", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated resources/views/components/layouts/app.blade.php")
