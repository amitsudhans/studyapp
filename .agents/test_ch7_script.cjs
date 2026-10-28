const fs = require('fs');

const html = fs.readFileSync('public/animations/class7-math-tale-of-three-intersecting-lines.html', 'utf8');

// 1. Check prohibited text
if (html.includes('Ganita Prakash')) {
  console.error('FAIL: Found prohibited string "Ganita Prakash"');
  process.exit(1);
} else {
  console.log('PASS: Prohibited string check passed (0 occurrences)');
}

// 2. Check solutionModal inline display none
if (!html.includes('id="solutionModal" style="display: none;"')) {
  console.error('FAIL: solutionModal does not have style="display: none;" inline');
  process.exit(1);
} else {
  console.log('PASS: solutionModal has style="display: none;" inline');
}

// 3. Check lastSlideNotice
if (!html.includes('🎉 You have reached the last slide of this chapter!')) {
  console.error('FAIL: lastSlideNotice text not found');
  process.exit(1);
} else {
  console.log('PASS: lastSlideNotice has exact required message');
}

// 4. Extract script content and validate JS syntax
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>[\s\S]*?<\/body>/);
if (scriptMatch) {
  const jsCode = scriptMatch[1];
  try {
    new Function(jsCode);
    console.log('PASS: Main script block syntax is valid JavaScript');
  } catch (err) {
    console.error('FAIL: Script syntax error:', err);
    process.exit(1);
  }
} else {
  console.error('FAIL: Main script block not found');
  process.exit(1);
}

console.log('ALL STATIC CHECKS PASSED!');
