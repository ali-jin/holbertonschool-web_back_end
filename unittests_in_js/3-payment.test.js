const sendPaymentRequestToApi = require("./3-payment");
const Utils = require('./utils');
const expect = require('chai').expect;
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function() {
  it('Validate the usage of the Utils function', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spy.returnValues[0]).to.equal(120);

    spy.restore();
  })
})