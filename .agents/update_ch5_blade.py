with open("resources/views/components/layouts/app.blade.php", "r", encoding="utf-8") as f:
    text = f.read()

target = """                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                }

                if (iframe.src !== fileUrl) {"""

replacement = """                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class7-math-parallel-intersecting-lines' || type === 'chapter5-math-class7' || type === 'parallel-and-intersecting-lines' || type === 'class7-parallel-intersecting-lines' || type === 'parallel-lines-class7' || type === 'class7-math-lines-angles' || type === 'intersecting-lines-class7') {
                    fileUrl = "{{ asset('animations/class7-math-parallel-intersecting-lines.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 5: Parallel and Intersecting Lines Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                }

                if (iframe.src !== fileUrl) {"""

assert target in text, "target not found in app.blade.php"
text = text.replace(target, replacement, 1)

with open("resources/views/components/layouts/app.blade.php", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated resources/views/components/layouts/app.blade.php")
