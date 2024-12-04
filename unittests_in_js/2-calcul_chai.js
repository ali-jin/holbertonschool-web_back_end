// Function that do arithmetic operations
function calculateNumber(type, a, b) {
  if (typeof a !== 'number' || typeof b !== 'number' || typeof type !== 'string') {
    throw new Error('Invalid input');
  }

  const roundA = Math.round(a);
  const roundB = Math.round(b);

  if (type === 'SUM') {
    return roundA + roundB;
  }
  else if (type === 'SUBTRACT') {
    return roundA - roundB;
  }
  else if (type === 'DIVIDE') {
    if (roundB === 0) {
      return 'Error';
    }
    return roundA / roundB;
  }
}

module.exports = calculateNumber;
