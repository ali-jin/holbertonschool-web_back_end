const calculateNumber = require("./2-calcul_chai.js");
const expect = require('chai').expect;

describe('calculateNumber', function () {
  describe('Tests sum operation', function () {
    it('Return the correct sum of 2 positve integers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 2, 5)).to.equal(7);
    });
    it('Return the correct sum of 2 negative integers', () => {
      expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
      expect(calculateNumber('SUM', -3, -5)).to.equal(-8);
    });
    it('Return the correct sum of one negative and one positve integers', () => {
      expect(calculateNumber('SUM', -1, 3)).to.equal(2);
      expect(calculateNumber('SUM', -3, 9)).to.equal(6);
    });
    it('Throw an error if there are invalid values present', () => {
      expect(() => calculateNumber('SUM', "a", 5)).to.throw(Error);
      expect(() => calculateNumber('SUM', "a", "b")).to.throw(Error);
    })
  });

  describe('Tests for substract operations', function() {
    it('Return the correct substraction of 2 numbers', () => {
      expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
      expect(calculateNumber('SUBTRACT', 2, 6)).to.equal(-4);
    });
    it('Throw an error if there are invalid values present', () => {
      expect(() => calculateNumber('SUBTRACT', "a", 5)).to.throw(Error);
      expect(() => calculateNumber('SUBTRACT', 8, "b")).to.throw(Error);
    });
  });

  describe('Tests for division operations', function() {
    it('Return the correct division of 2 numbers', () => {
      expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
      expect(calculateNumber('DIVIDE', 10, 5)).to.equal(2);
    });
    it('Return error when dividing by 0', () => {
      expect(calculateNumber('DIVIDE', 8, 0)).to.equal('Error');
    });
    it('Throw an error if there are invalid values present', () => {
      expect(() => calculateNumber('SUBTRACT', "a", 5)).to.throw(Error);
      expect(() => calculateNumber('SUBTRACT', 8, "b")).to.throw(Error);
    });
  });
});
