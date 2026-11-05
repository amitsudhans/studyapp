# -*- coding: utf-8 -*-
with open('resources/views/components/layouts/app.blade.php', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''                } else if (type === 'class4-maths-measuring-length' || type === 'chapter6-maths-class4' || type === 'class4-maths-chapter6' || type === 'class4-measuring-length' || type === 'measuring-length-class4' || type === 'class4-maths-measuring-length-lab' || type === 'class4-math-measuring-length' || type === 'class4-measuring-length-lab') {
                    fileUrl = "{{ asset('animations/class4-maths-measuring-length.html') }}";
                    titleText = "NCERT Class 4 Mathematics — Chapter 6: Measuring Length Master Lab";
                    badgeText = "Class 4 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";'''

replacement = '''                } else if (type === 'class4-maths-measuring-length' || type === 'chapter6-maths-class4' || type === 'class4-maths-chapter6' || type === 'class4-measuring-length' || type === 'measuring-length-class4' || type === 'class4-maths-measuring-length-lab' || type === 'class4-math-measuring-length' || type === 'class4-measuring-length-lab') {
                    fileUrl = "{{ asset('animations/class4-maths-measuring-length.html') }}";
                    titleText = "NCERT Class 4 Mathematics — Chapter 6: Measuring Length Master Lab";
                    badgeText = "Class 4 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class4-maths-the-cleanest-village' || type === 'chapter7-maths-class4' || type === 'class4-maths-chapter7' || type === 'class4-the-cleanest-village' || type === 'the-cleanest-village-class4' || type === 'class4-maths-the-cleanest-village-lab' || type === 'class4-math-the-cleanest-village' || type === 'class4-cleanest-village-lab') {
                    fileUrl = "{{ asset('animations/class4-maths-the-cleanest-village.html') }}";
                    titleText = "NCERT Class 4 Mathematics — Chapter 7: The Cleanest Village Master Lab";
                    badgeText = "Class 4 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";'''

assert target in content, 'Target not found in app.blade.php!'
content = content.replace(target, replacement, 1)

with open('resources/views/components/layouts/app.blade.php', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully updated app.blade.php with Chapter 7 modal mapping!')
