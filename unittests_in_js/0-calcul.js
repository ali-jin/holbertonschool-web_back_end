// Function that returns the sum of t a and b
function calculateNumber(a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Invalid input');
  }

  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
