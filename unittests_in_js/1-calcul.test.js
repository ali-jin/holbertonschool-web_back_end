const calculateNumber = require("./1-calcul.js");
var assert = require('assert');

describe('calculateNumber', function () {
  describe('Tests sum operation', function () {
    it('Return the correct sum of 2 positve integers', () => {
      assert.equal(calculateNumber('SUM', 1, 3), 4);
      assert.equal(calculateNumber('SUM', 2, 5), 7);
    }),
    it('Return the correct sum of 2 negative integers', () => {
      assert.equal(calculateNumber('SUM', -1, -3), -4);
      assert.equal(calculateNumber('SUM', -3, -5), -8);
    }),
    it('Return the correct sum of one negative and one positve integers', () => {
      assert.equal(calculateNumber('SUM', -1, 3), 2);
      assert.equal(calculateNumber('SUM', -3, 9), 6);
    }),
    it('Throw an error if there are invalid values present', () => {
      assert.throws(() => calculateNumber('SUM', "a", 5), Error);
      assert.throws(() => calculateNumber('SUM', "a", "b"), Error);
    })
  }),

  describe('Tests for substract operations', function() {
    it('Return the correct substraction of 2 numbers', () => {
      assert.equal(calculateNumber('SUBTRACT', 5, 3), 2);
      assert.equal(calculateNumber('SUBTRACT', 2, 6), -4);
    }),
    it('Throw an error if there are invalid values present', () => {
      assert.throws(() => calculateNumber('SUBTRACT', "a", 5), Error);
      assert.throws(() => calculateNumber('SUBTRACT', 8, "b"), Error);
    })
  }),

  describe('Tests for division operations', function() {
    it('Return the correct division of 2 numbers', () => {
      assert.equal(calculateNumber('DIVIDE', 8, 2), 4);
      assert.equal(calculateNumber('DIVIDE', 10, 5), 2);
    }),
    it('Return error when dividing by 0', () => {
      assert.equal(calculateNumber('DIVIDE', 8, 0), 'Error');
    }),
    it('Throw an error if there are invalid values present', () => {
      assert.throws(() => calculateNumber('SUBTRACT', "a", 5), Error);
      assert.throws(() => calculateNumber('SUBTRACT', 8, "b"), Error);
    })
  })
})
