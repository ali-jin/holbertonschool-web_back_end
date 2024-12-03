const calculateNumber = require("./0-calcul.js");
var assert = require('assert');

describe('calculateNumber', function() {
  it('Return the correct sum of two positve integers', () => {
    assert.equal(calculateNumber(1, 3), 4);
    assert.equal(calculateNumber(2, 5), 7);
  }),
  it('Return the correct sum of one positive integer a float', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
    assert.equal(calculateNumber(4.8, 3), 8);
  }),
  it('Return the correct sum of two float', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
    assert.equal(calculateNumber(1.5, 3.7), 6);
  }),
  it('Return the correct sum of two negative integers', () => {
    assert.equal(calculateNumber(-1, -3), -4);
    assert.equal(calculateNumber(-3, -5), -8);
  }),
  it('Return the correct sum of one negative and one positve integers', () => {
    assert.equal(calculateNumber(-1, 3), 2);
    assert.equal(calculateNumber(-3, 9), 6);
  }),
  it('Throw an error if there are values present', () => {
    assert.throws(() => calculateNumber("a", 5), Error);
    assert.throws(() => calculateNumber(9, "b"), Error);
    assert.throws(() => calculateNumber("a", "b"), Error);
  })
})
